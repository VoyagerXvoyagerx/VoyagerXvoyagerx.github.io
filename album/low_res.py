from PIL import Image
import os

# Define the source and target directories
src_dir = './images'  # Replace with your actual path
target_dir = './img_low_res'  # Replace with your actual path

# Function to compress images
def compress_images(src_folder, target_folder, quality=40):
    # Get all the image files in the source folder
    for image_name in os.listdir(src_folder):
        # The full file path
        file_path = os.path.join(src_folder, image_name)
        # Check if it is a file and not a directory
        if os.path.isfile(file_path):
            # Open the image
            with Image.open(file_path) as img:
                # Convert palette-based images with transparency to RGBA
                if img.mode == 'P':
                    img = img.convert('RGBA')
                # Convert to RGB before saving as JPEG
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                # Define the output file path
                output_file_path = os.path.join(target_folder, image_name)
                print(output_file_path)
                # Compress to the target folder with the specified quality
                img.save(output_file_path, 'JPEG', quality=quality)

# Run the function to compress the images
compress_images(src_dir, target_dir)
