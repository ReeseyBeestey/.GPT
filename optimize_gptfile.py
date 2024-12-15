from PIL import Image

def load_gpt_with_rle(file_path, output_image_path):
    with open(file_path, "rb") as f:
        # Read header
        signature = f.readline().decode().strip()
        if signature != "GPTv1":
            raise ValueError("Invalid .gpt file format!")
        
        dimensions = f.readline().decode().strip().split()
        width, height = int(dimensions[0]), int(dimensions[1])
        palette_size = int(f.readline().decode().strip())
        
        # Read palette
        palette = []
        for _ in range(palette_size):
            color = f.read(3)
            palette.extend(color)
        
        # Read RLE-compressed pixel data
        pixel_data = []
        while True:
            pixel = f.read(1)
            length = f.read(1)
            if not pixel or not length:
                break
            pixel_data.extend([pixel[0]] * length[0])  # Expand RLE pair

        # Ensure the pixel data matches the image size
        if len(pixel_data) != width * height:
            raise ValueError(f"Decoded pixel data does not match image dimensions ({len(pixel_data)} vs {width * height})")

    # Reconstruct image
    img = Image.new("P", (width, height))
    img.putpalette(palette)
    img.putdata(pixel_data)
    img.save(output_image_path)
    print(f"Image reconstructed and saved as {output_image_path}!")

# Paths:
input_gpt_path = r"C:\Users\YourUsername\Documents\optimized_image.gpt"  # Path to the .gpt file
output_png_path = r"C:\Users\(YourUsername\Desktop\reconstructed_image.png(3)"  # Path for the decoded image (with .png extension)

# Decode and save as a PNG
load_gpt_with_rle(input_gpt_path, output_png_path)
