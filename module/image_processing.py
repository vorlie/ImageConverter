import os
from PIL import Image

def resize_image(image, max_width, max_height):
    width, height = image.size
    if width > max_width or height > max_height:
        if width > height:
            new_width = max_width
            new_height = int((height / width) * max_width)
        else:
            new_width = int((width / height) * max_height)
            new_height = max_height
        return image.resize((new_width, new_height))
    else:
        return image

def convert_image(input_file_path, output_format, max_width=None, max_height=None):
    try:
        output_folder = os.path.dirname(input_file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(input_file_path))

        # Create output file name with size if resizing is applied
        if max_width is not None and max_height is not None:
            output_file_name = f"{file_name}_{max_width}x{max_height}_converted.{output_format}"
        else:
            output_file_name = f"{file_name}_converted.{output_format}"

        output_file_path = os.path.join(output_folder, output_file_name)
        im = Image.open(input_file_path)
        
        # Resize the image if max dimensions are provided
        if max_width is not None and max_height is not None:
            im = resize_image(im, max_width, max_height)
        
        im.save(output_file_path, output_format.upper())
        print(f"File converted successfully.\nOutput: {output_file_path.replace('/', os.path.sep)}")
    except Exception as e:
        print(f"An error occurred while converting the image: {str(e)}")

