from config import DATABASE_PARAM
from PIL import Image
import os

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

    for i, folder_path in enumerate(image_folder_paths):
        # TODO: get all paths for all images in this folder
        image_paths = [os.path.join(folder_path, fname) for fname in os.listdir(folder_path) if fname.endswith(('.png', '.jpg', '.jpeg'))]


        trash_can_id = trash_can_ids[i]
        for image_path in image_paths:
            stored_image = Image.open(image_path)
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
    '''
    Update database based on full_likelihood level
    '''

    if full_likelihood == -1:
        # means trashcan is empty
        # update as empty now
        return
    else:
        # Assumes trashcan is full
        # update as full now

        return


def getNearbyTrashCanImages(longitude, latitude, range=0.4):
    '''
    Queries a database to find trashcans that are with longitude and latitude 
    of a given range. Then returns the folder path for the trash can ids that
    are given from the query.
    
    '''


    return [], []