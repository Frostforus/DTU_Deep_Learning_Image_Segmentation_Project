import colorsys

import numpy as np
from matplotlib import pyplot as plt

print("hello worls")

directory_path = './data/arrays/'

# Load the original array
array = np.load(directory_path + "black_5_doors_0001.npy")

# Extract the first 3 channels for x
x = array[..., :3]

data = [
    ["orange", "hood", 10],
    ["dark green", "front door", 20],
    ["yellow", "rear door", 30],
    ["cyan", "frame", 40],
    ["purple", "rear quarter panel", 50],
    ["light green", "trunk lid", 60],
    ["blue", "fender", 70],
    ["pink", "bumper", 80],
    ["no color", "rest of car", 90],
    ["white", "background", 0]
]

color_to_hue = {
    "orange": 30,
    "dark green": 120,
    "yellow": 60,
    "cyan": 180,
    "purple": 270,
    "light green": 150,
    "blue": 210,
    "pink": 330,
    # TODO: change this to black later
    "no color": 0,
    "white": 1,
}

# , row[1] this can be put into the thing too
hue_mapping = {row[2]: color_to_hue.get(row[0], row[0]) for row in data}

# Map the hue values using the dictionary
hue_values = np.vectorize(hue_mapping.get)(array[..., -1])

# Convert hue values to RGB values
y = np.empty_like(array[..., :3], dtype=np.uint8)
for i in range(256):
    for j in range(256):
        if hue_values[i, j] in (0, 1):
            y[i, j] = (x[i, j, 0], x[i, j, 1], x[i, j, 2])
        else:
            hsv_color = (hue_values[i, j] / 360.0, 1, 1)  # Convert hue to HSV format
            rgb_color = colorsys.hsv_to_rgb(*hsv_color)  # Convert to RGB
            y[i, j] = (int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255))

# Print the shapes of x and y
print("Shape of x:", x.shape)
print("Shape of y:", y.shape)


def show_image(image):
    # Extract the image data from the last channel (the alpha channel, for example)
    image_data = image[:, :]

    # Display the image using Matplotlib
    plt.imshow(image_data)  # Use 'gray' colormap for grayscale images
    plt.axis('off')  # Turn off the axis labels and ticks
    plt.show()


show_image(x)
show_image(y)
