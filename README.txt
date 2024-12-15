**GPT Image Format**
Scroll down for instructions on how to use this, and a Q&A section.
My code only MIGHT work, be weary that my testing efforts were not very proper.
This project introduces a custom GPT image format, the first file format designed almost entirely by ChatGPT (Idea made humanly, all code written by AI, even a large part of the file you're reading right now)! It is designed to store images with a reduced color palette and optimized pixel data using Run-Length Encoding (RLE). It supports converting PNG images to the GPT format, and decoding them back to PNG.

Features:
- Custom Image Format:** Have the novelty of your own, personal image format!
- Palette Reduction: Reduces the color palette to a specified number of colors (48 colors by default).
- Run-Length Encoding (RLE): Compress pixel data with efficient RLE compression.
- Conversion: Convert between PNG and the custom GPT format, and vice versa..

Requirements:
- Python 3.x
- Pillow (for image processing)
- NumPy (for handling pixel data arrays)

To install dependencies, run:

pip install pillow numpy

in the command prompt.

The GPT format is less efficient than PNG (about 1.8x larger), but it offers an interesting approach to custom image formats.
Slightly limited support for images with more than 48 colors (though you can experiment with other color values).

## **License:**
This project is open-source and free to use. Feel free to fork, modify, and contribute!
HOW TO USE:
First, open the file "create_gptfile.py" by right-clicking on the file and clicking the "Edit" button. Then, change the labeled placeholder paths to the path of your image. THIS FILE FORMAT ONLY WORKS WITH CONVERTING PNG FILES! Change the output path to the path to where you would like the file to be and what it should be named. Next, run this code in the Command Prompt (Administrator mode is not needed)

python C:\Users\(your username)\(what folder you put the file in)\.GPT FILE CONVERTER\create_gptfile.py

You should now have an unoptimized .GPT file! You can keep it this way, or you can optimize it, by:
1. Opening optimize.gptfile.py by the same you opened create_gptfile.py
2. Changing the input path from the placeholder to the path of your unoptimized GPT file.
3. Changing the output path from the placeholder to the path of where you'd like the folder to be and what it should be named.
4. Running this command in the Command Prompt

python C:\Users\(your username)\(what folder you put the file in)\.GPT FILE CONVERTER\optimize_gptfile/py

You should now have an optimized version of your .GPT file from earlier.
If you wish, you can also convert this file back to PNG.
How to do this:
1. Opening decode_gptfile.py
2. Changing your input path to the path of your optimized .GPT file.
3. Changing the output path to where you'd like the decoded image to be and what it should be called.
4. Running this command in the Command Prompt

python C:\Users\(your username)\(what folder you put the file converter in)\.GPT FILE CONVERTER\decode_gptfile.py

You have now decoded your GPT file back to PNG!
MIGHT-BE COMMON QUESTIONS:
Q: Why did you write code to make a .GPT file, and then to optimize one, rather than combining the two and making the optimized file first?
A: Because of the way I made this. I asked ChatGPT to make me a new image format, and it did. But I wasn't happy with how big it was (the first version was 1,297 kb) so I asked it to optimize the file so it was smaller, and it did. I couldn't find a way to merge the two, so they stay separate.
Q: Why did you make this?
A: I saw someone on YouTube create THEIR own file format, .bruh, and I wanted to do the same. But I admittedly have no python experience, so I got ChatGPT to do most of the work for me.
Q: Where did you get your idea from?
A: I remembered how Mario Paint stored its files. A dumbed down version is that they named the colors in reading order as a list.
Here's an example of what I mean.
If you had a full 1080p image that was just a red canvas, here's how it might've been stored.
pixels 1-2,073,600 255 0 0
I thought that was a good idea, so I decided to make a new file format following those rules. Then I figured the average 10k+ pixels in a regular image would be too hard to store, and I reduced the color palette for a solution.
Q: How long did it take you to make this?
A: Roughly ~7 hours.
Q: What version of ChatGPT did you use to make this
A: I have the free plan of ChatGPT, so some of it was GPT-4o, and some was GPT-4o mini.
