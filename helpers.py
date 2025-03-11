# region Import Libraries
import cv2
import os
import glob
#endregion

# region Helper Functions
def get_current_directory():
    return os.getcwd()

def find_photos(current_working_directory=None):
    if current_working_directory is None:
        current_working_directory = get_current_directory()
    image_extensions = ('*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff')
    photos = []
    for ext in image_extensions:
        photos.extend(glob.glob(os.path.join(current_working_directory, ext)))
    return photos


def remove_background(image_path=None, current_working_directory=None):
    if image_path is None:
        photos = find_photos(current_working_directory)
        if not photos:
            raise ValueError("No photos found.")
        if len(photos) > 1:
            raise ValueError("More than one photo found.")
        image_path = photos[0]
    # Load the image
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold to create a mask
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # Optionally, refine the mask using morphology (e.g., closing small holes)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Invert the mask (if necessary, depending on the object/background colors)
    mask_inv = cv2.bitwise_not(mask)

    # Extract object using the mask
    fg = cv2.bitwise_and(image, image, mask=mask)

    # Make the background transparent using the inverted mask
    bg = cv2.bitwise_and(image, image, mask=mask_inv)
    bg[:] = [0, 0, 0]  # Set the background to black (transparent)

    # Combine the object (fg) and the transparent background (bg)
    final_image = fg

    # Save or display the resulting image
    output_path = os.path.join(current_working_directory or get_current_directory(), "output.png")
    cv2.imwrite(output_path, final_image)

    return output_path





#endregion