# region Import Libraries
import os
import glob
#endregion

# region Helper Functions
def get_current_directory():
    return os.getcwd()

def find_photos(current_working_directory = get_current_directory()):
    image_extensions = ('*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff')

    photos = []
    for ext in image_extensions:
        photos.extend(glob.glob(os.path.join(current_working_directory, ext)))

    if not photos:
        return "No photos found."
    elif len(photos) > 1:
        return "More than one photo found."
    else:
        return photos




#endregion