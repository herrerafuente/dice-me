from helpers import get_current_directory, find_photos, remove_background

def main():
    print(get_current_directory())
    print(find_photos(current_working_directory=None))
    print(remove_background(image_path=None, current_working_directory=None))

if __name__ == '__main__':
    main()