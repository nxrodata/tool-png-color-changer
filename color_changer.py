import os
from PIL import Image

# TODO : Fix the bug where the color of the entire 512x512 image is changed to the specified color.
def change_color(image_path, output_folder, hex_color):
    """Changes the color of flat PNG icons to the specified hex color.
    
    :param image_path: The path to the PNG image file.
    :param output_folder: The name of the folder to save the output image.
    :param hex_color: The hex color to change the image to (e.g., #FF0000).
    
    :return: None (saves the image to the output folder).
    
    >>> change_color("nacho.png", "outputs", "#FF0000)
    SUCCESS: Changed nacho.png color to #FF0000. Saved to folder: outputs
    """
    
    try:
        if not image_path.endswith(".png"):
            print("EXT ERROR: Input image must be a PNG file.")
            return
        
        # Convert hex color to RGB tuple
        color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5)) + (255,)
        
        img = Image.open(image_path)
        img = img.convert("RGBA")
        datas = img.getdata()
        
        # Changing the color of the image
        new_image_data = []
        for item in datas:
            if item[0] in range(0, 100):
                new_image_data.append(color)
            else:
                new_image_data.append(item)
        
        img.putdata(new_image_data)
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        img.save(output_path)
        print(f"SUCCESS: Changed {os.path.basename(image_path)} color to {hex_color}. Saved to folder: {output_folder}")
        
    except OSError as e:
        print(f"ERROR: {e}")