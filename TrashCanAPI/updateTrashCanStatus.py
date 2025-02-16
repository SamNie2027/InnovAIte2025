from config import DATABASE_PARAM

def updateTrashCanStatus(image, longitude, latitude, full_likelihood, model):
    '''
    Finds and updates the status of a trashcan in trashcan database. 
    '''

    # get labeled images for nearby trash cans
    image_folder_path, trash_can_ids = getNearbyTrashCanImages(longitude, latitude) # NOT IMPLEMENTED

    # determine which trash can id to update
    if (len(trash_can_ids) > 1):
        trash_can_id = matchTrashCanID(image, image_folder_path, trash_can_ids, model) # NOT IMPLEMENTED
    elif (len(trash_can_id) == 1):
        trash_can_id = trash_can_ids[0]
    else:
        # no nearby trashcans
        return
    
    # Update Database
    updateTrashCanStatus(trash_can_id, full_likelihood) # NOT IMPLEMENTED

    return 

def matchTrashCanID(image, image_folder_path, trash_can_ids, model):
    '''
    Determines which trash can ID that given a image matches with by 
    comparing to labeled trash can images. 
    
    Params:
    image is the unlabeled image.
    image_folder_path is path to a folder with images.
    trash_can_ids is the trash can id for the folder paths given.
    model is the compare model.
    '''

def updateTrashCanStatus(trash_can_id, full_likelihood):
    '''
    Update database based on full_likelihood level
    '''

    if full_likelihood == -1:
        # means trashcan was emptied
        # update as empty now
        return
    
    # actual logic

    return

def getNearbyTrashCanImages(longitude, latitude, radius=100):
    '''
    Queries a database to find trashcans that are with longitude and latitude 
    of a given radius. Then returns the folder path for the trash can ids that
    are given from the query.
    
    '''


    return [], []