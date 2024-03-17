import os
import random

def split_data(image_folder, train_ratio=0.8):
    # Get the list of all filenames in the folder
    filenames = os.listdir(image_folder)
    # Shuffle the filenames
    random.shuffle(filenames)
    # Calculate the number of samples for training
    num_train = int(len(filenames) * train_ratio)
    # Split the filenames into training and testing sets
    train_filenames = filenames[:num_train]
    test_filenames = filenames[num_train:]
    return train_filenames, test_filenames

# Specify the path to the folder containing images
image_folder = "C:\\Users\\k\\Desktop\\COC\\data"
# Split the data into training and testing sets
train_filenames, test_filenames = split_data(image_folder)

# Print the number of samples in each set
print("Number of training samples:", len(train_filenames))
print("Number of testing samples:", len(test_filenames))
