import numpy as np

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
    #TODO: change this to black later
    "no color": 0,
    "white": 1,
}

#, row[1] this can be put into the thing too
value_mapping = {row[2]: color_to_hue.get(row[0], row[0]) for row in data}


# Map the values in the last channel using the dictionary
y = np.vectorize(value_mapping.get)(array[..., -1])

# Expand the last dimension of y to have shape (256, 256, 3)
y = np.expand_dims(y, axis=-1)
# Print the shapes of x and y
print("Shape of x:", x.shape)
print("Shape of y:", y.shape)