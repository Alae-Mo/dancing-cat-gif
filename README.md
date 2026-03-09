# Dancing Cat GIF with Python

This is a mini project that creates a GIF of a dancing cat using Python.

## How it works
- I used `PIL.Image` to resize all images to (656, 656). Without this, the code raises a `ValueError('all input arrays must have the same shape')`.
- The list of filenames is written so the GIF loops the cat dancing from right to left and back.
- `imageio.v3` is used to save the GIF with a frame duration of 0.25s and infinite looping.

## How to run
1. Install dependencies:  
pip install pillow imageio
2. Make sure the `images/` folder contains `image_1.jpg` to `image_4.jpg`.
3. Run:
python create_gif.py


## Notes
- The GIF will be saved as `dancing_cat.gif`.
- You can replace the images with your own as long as they have the same dimensions.