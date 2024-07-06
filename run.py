import os
from color_changer import change_color

if __name__ == "__main__":
    HEX_COLOR = "#85A0C7"
    IMAGE_FOLDER = "pngs"
    OUTPUT_FOLDER = "outputs"
    
    for image in os.listdir(IMAGE_FOLDER):
        image_path = os.path.join(IMAGE_FOLDER, image)
        change_color(image_path, OUTPUT_FOLDER, HEX_COLOR)