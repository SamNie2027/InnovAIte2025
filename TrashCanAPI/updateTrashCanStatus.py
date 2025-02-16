from config import DATABASE_PATH, IMAGES_PATH
from PIL import Image
import os
import sqlite3

def updateTrashCanStatusMain(image, latitude, longitude, full_likelihood, model):
    '''
    Finds and updates the status of a trashcan in trashcan database. 
    '''

    # get labeled images for nearby trash cans
    image_folder_paths, trash_can_ids = getNearbyTrashCanImages(latitude, longitude)
    print("image_folder_paths:", image_folder_paths)
    print("IDs:", trash_can_ids)

    # determine which trash can id to update
    if (len(trash_can_ids) > 1):
        trash_can_id = matchTrashCanID(image, image_folder_paths, trash_can_ids, model)
    elif (len(trash_can_id) == 1):
        trash_can_id = trash_can_ids[0]
    else:
        # no nearby trashcans
        return
    print("ID:", trash_can_id)

    # Update Database
    updateTrashCanStatus(trash_can_id, full_likelihood)

    return 

def matchTrashCanID(image, image_folder_paths, trash_can_ids, model):
    '''
    Determines which trash can ID the given image matches with by 
    comparing it to labeled trash can images. 
    
    Params:
    image: the unlabeled image.
    image_folder_paths: list of paths to folders containing images.
    trash_can_ids: list of trash can IDs corresponding to the folder paths.
    model: the comparison model.
    
    Returns:
    The trash can ID that best matches the given image.
    '''
    matched_id = -1

    ranking = {}

    image = cutOutTrashCan(image)

    for i, folder_path in enumerate(image_folder_paths):
        # TODO: get all paths for all images in this folder
        image_paths = [os.path.join(folder_path, fname) for fname in os.listdir(folder_path) if fname.endswith(('.png', '.jpg', '.jpeg'))]


        trash_can_id = trash_can_ids[i]
        for image_path in image_paths:
            stored_image = cutOutTrashCan(Image.open(image_path))
            similarity = model.predict(image, stored_image)
            if trash_can_id in ranking:
                ranking[trash_can_id] = max(ranking[trash_can_id], similarity)
            else:
                ranking[trash_can_id] = similarity

    # TODO: get the key from ranking with highest similarity value
    if ranking:
        matched_id = max(ranking, key=ranking.get)

    return matched_id

def cutOutTrashCan(image):
    '''
    Cuts out the trash can from image to leave only the background.

    Currently not Implemented (Stretch Goal)
    '''
    return image

def updateTrashCanStatus(trash_can_id, full_likelihood):
    """
    Update the 'is_full' status of a trash can in the 'trash_cans' table.

    :param trash_can_id: ID of the trash can to update.
    :param full_likelihood: 
        - -1 indicates the trash can is emptied (is_full = false).
        - Any other value indicates the trash can is full (is_full = true).
    """
    connection = None
    cursor = None
    try:
        # 1. Connect to the SQLite database
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()

        # 2. Determine whether to mark as empty or full
        if full_likelihood <= 0:
            query = """
                UPDATE trash_cans
                SET is_full = FALSE,
                    last_updated = CURRENT_TIMESTAMP
                WHERE trash_can_id = ?
            """
            print(f"Marking trash can {trash_can_id} as EMPTY.")
        else:
            query = """
                UPDATE trash_cans
                SET is_full = TRUE,
                    last_updated = CURRENT_TIMESTAMP
                WHERE trash_can_id = ?
            """
            print(f"Marking trash can {trash_can_id} as FULL.")

        # 3. Execute the update
        cursor.execute(query, (trash_can_id,))
        connection.commit()

    except Exception as e:
        print(f"Error updating trash can {trash_can_id}: {str(e)}")

    finally:
        # 4. Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def getNearbyTrashCanImages(latitude, longitude, range=0.001):
    '''
    Queries a database to find trashcans that are with longitude and latitude 
    of a given range. Then returns the folder path for the trash can ids that
    are given from the query.
    
    '''
    image_paths = []
    trash_can_ids = []

    connection = None
    cursor = None
    try:
        # 1. Connect to the SQLite database
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()

         # 2. Query to find trash cans within the given latitude/longitude range
        query = """
        SELECT trash_can_id 
        FROM trash_cans
        WHERE gps_latitude BETWEEN ? AND ?
          AND gps_longitude BETWEEN ? AND ?;
        """

        # Calculate boundary values
        min_lat, max_lat = latitude - range, latitude + range
        min_long, max_long = longitude - range, longitude + range

        print(f"min lat: {min_lat} max_lat: {max_lat}")
        print(f"min long: {min_long} max long: {max_long}")

        # Execute the query
        cursor.execute(query, (min_lat, max_lat, min_long, max_long))
        trash_can_ids = [row[0] for row in cursor.fetchall()]

        if trash_can_ids:
            # 3. Query to retrieve image URLs along with their trash_can_id
            query = """
            SELECT trash_can_id, image_url 
            FROM images
            WHERE trash_can_id IN ({});
            """.format(",".join("?" * len(trash_can_ids)))  # Dynamically format query with placeholders

            cursor.execute(query, trash_can_ids)
            
            # Store image paths in a dictionary with trash_can_id as key
            image_dict = {tc_id: [] for tc_id in trash_can_ids}  # Initialize empty lists
            for tc_id, image_url in cursor.fetchall():
                image_dict[tc_id].append(image_url)  # Append in case of multiple images per trash can

            # 4. Ensure indexes match: extract images in the same order as trash_can_ids
            # image_paths = [image_dict[tc_id] if tc_id in image_dict else [] for tc_id in trash_can_ids]
            image_paths = [img for tc_id in trash_can_ids for img in image_dict.get(tc_id, [])]

            # 5. Clean the paths:
            for i, path in enumerate(image_paths):
                path_temp = os.path.dirname(path)  # Get directory name
                cleaned_path = os.path.join(IMAGES_PATH, path_temp)  # Join paths correctly
                image_paths[i] = cleaned_path

    except Exception as e:
        print(f"Error getting nearbyTrashCans: {str(e)}")

    finally:
        # 4. Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return image_paths, trash_can_ids