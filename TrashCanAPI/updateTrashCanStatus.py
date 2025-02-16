from config import DATABASE_PATH
from PIL import Image
import os
import sqlite3
import cv2
import numpy as np

def updateTrashCanStatus(image, longitude, latitude, full_likelihood, model):
    '''
    Finds and updates the status of a trashcan in trashcan database. 
    '''

    # get labeled images for nearby trash cans
    image_folder_paths, trash_can_ids = getNearbyTrashCanImages(longitude, latitude) # NOT IMPLEMENTED

    # determine which trash can id to update
    if (len(trash_can_ids) > 1):
        trash_can_id = matchTrashCanID(image, image_folder_paths, trash_can_ids, model)
    elif (len(trash_can_id) == 1):
        trash_can_id = trash_can_ids[0]
    else:
        # no nearby trashcans
        return
    
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

def CutOutTrashCan(image: Image.Image) -> Image.Image:
    """
    Blacks out the middle portion of the image, assuming the object to be removed is in the center.
    Adjusts dynamically based on image size.
    """

    # Convert PIL (RGB) to OpenCV (BGR)
    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    (h, w) = open_cv_image.shape[:2]

    # Define the central area (adjust percentage as needed)
    center_x, center_y = w // 2, h // 2
    box_width, box_height = int(w * 0.4), int(h * 0.5)  # 40% width, 50% height

    # Compute box coordinates
    x1, y1 = center_x - box_width // 2, center_y - box_height // 2
    x2, y2 = center_x + box_width // 2, center_y + box_height // 2

    # Black out the middle section
    open_cv_image[y1:y2, x1:x2] = (0, 0, 0)  # Fill with black

    # Convert back to PIL
    output_pil = Image.fromarray(cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB))
    
    return output_pil

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


def getNearbyTrashCanImages(longitude, latitude, range=0.4):
    '''
    Queries a database to find trashcans that are with longitude and latitude 
    of a given range. Then returns the folder path for the trash can ids that
    are given from the query.
    
    '''


    return [], []