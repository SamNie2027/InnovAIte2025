from config import DATABASE_PARAM

def updateTrashCanStatus(image, longitude, latitude, full_likelihood, model):
    '''
    Finds and updates the status of a trashcan in trashcan database. 
    '''

    # get labeled images for nearby trash cans
    image_folder_path, trash_can_id = getNearbyTrashCanImages(longitude, latitude)

    if (len(trash_can_id) > 1):
        pass

    return 

def getNearbyTrashCanImages(longitude, latitude, radius=100):
    '''
    Queries a database to find trashcans that are with longitude and latitude 
    of a given radius. Then returns the folder path for the trash can ids that
    are given from the query.
    
    '''


    return [], []