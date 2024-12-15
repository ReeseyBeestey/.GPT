from PIL import Image
import numpy as np
 # You'll need to add your paths and change the amount of colors here ↓
def save_as_gpt(image_path, output_path, palette_size=48):
    # Open image and convert to reduced color palette
    img = Image.open(image_path).convert('RGB')
    img = img.convert('P', palette=Image.ADAPTIVE, colors=palette_size)
    img_data = np.array(img)
    palette = img.getpalette()[:palette_size * 3]

    # Create .gpt file content
    with open(output_path, "wb") as f:
        # Header
        f.write(f"GPTv1\n".encode())  # File signature
        f.write(f"{img.width} {img.height}\n".encode())
        f.write(f"{palette_size}\n".encode())
        
        # Palette
        for i in range(palette_size):
            color = palette[i*3:i*3+3] if i*3 < len(palette) else [0, 0, 0]
            f.write(bytes(color))  # Write RGB values
        
        # Pixel Data
        for color_index in img_data.flatten():
            f.write(bytes([color_index]))  # Write color index

    print(f"Image saved as {output_path}!")