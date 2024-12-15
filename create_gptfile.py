from PIL import Image
import numpy as np
 # You'll need to add your paths and change the amount of colors here ↓
input_path =r"C:\Users\mcari\Downloads\testing_gptconversion.png"
output_path =r"C:\Users\mcari\Downloads\test.gpt"
from PIL import Image
import os

def convert_png_to_gpt(image_path, output_path, target_colors=48):
    # Open the image
    img = Image.open(image_path).convert('RGB')  # Open and convert to RGB mode

    # Convert the image to P mode (palette-based image)
    img = img.convert("P", palette=Image.ADAPTIVE, colors=target_colors)

    # Get image dimensions and pixel data
    width, height = img.size
    pixel_data = list(img.getdata())

    # Get the image's palette
    palette = img.getpalette()[:target_colors * 3]  # Only take the first `target_colors` colors

    # Save as GPT file
    with open(output_path, "wb") as f:
        f.write(b"GPTv1\n")
        f.write(f"{width} {height}\n".encode())
        f.write(f"{target_colors}\n".encode())

        # Write the palette
        for i in range(target_colors):
            f.write(bytes(palette[i * 3:i * 3 + 3]))

        # Write pixel data
        for pixel in pixel_data:
            f.write(bytes([pixel]))

    print(f"Image converted to GPT and saved as {output_path}!")
