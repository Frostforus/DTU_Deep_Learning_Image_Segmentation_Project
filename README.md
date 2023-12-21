# Segmenting car parts using internal dataset - DTU_Deep_Learning_Image_Segmentation_Project
Deep learning project 2023, DTU.

# Project description

## Project code
The project code can be found in Master_Final_NoteBook.ipynb. Be aware that this notebook only contains the cleaned, readable version of our work, thus this file does not contain the results of the specific section. Instead, we include the links of the separate notebooks that have the results for each part of the code. These links can also be reached from here:

 - Enhanced labeling of real photos:
 - Data Augmentation: [Colab Link](https://colab.research.google.com/drive/1fslwnPv_Lq_hmmiZrmQg6VYrtTGMAyCM#scrollTo=NN9GT7dz4iYG)
 - Adding background images to CAD images: [Colab Link Link](https://colab.research.google.com/drive/1EDB2RnDnX4fKyJiQDGjDHAg4gL0Xmnlj?usp=sharing)
 - Model training and results:


# Project synopsis

## Project name: Segmenting car parts using internal dataset

## Motivation and background:
Image segmentation is a very interesting and relevant part of computer vision, it can be used in a variety of fields. The end model will be segmenting parts of the car, marking each relevant piece with its own colored filter. In this case, the long-term goal is to help insurance companies process damage claims.

## Goals and plans:
We will be using one of the sub-datasets provided to us by our project supervisor, this will probably be the black 5-door one, as it is pretty clean and the neural network should have a good time training on it.

We will start by analyzing relevant architectures, U-net being the best candidate so far. Once the initial architecture is selected and constructed, we can start preprocessing the images, using the non-segmented images as inputs, and the segmented images as outputs. As the data is big enough, we don't have to worry about the initial train-validation-test split too much, so we will start around a 70-15-15 split. Once the first training is done we can tweak the model using hyperparameter optimization techniques, and further optimize the structure of the net. We will be observing different metrics in the testing phase, aiming for an average accuracy of 80%. Further goals would be to use transfer learning on the other available dataset and increase the overall accuracy of the model, on totally new data points.

## References:
 - Semantic Shapes segmentation (Seth Adams): [Github Link](https://github.com/seth814/Semantic-Shapes)
 - Brain Tumor Segmentation using UNET (Idiot Programmer): [Github Link](https://github.com/nikhilroxtomar/Brain-Tumor-Segmentation-in-TensorFlow-2.0)
 - Image Segmentation Videos (Computer Vision Engineer): [Youtube Video Link](https://www.youtube.com/watch?v=aVKGjzAUHz0)
 - Further Reading: [https://paperswithcode.com/task/image-segmentation](https://paperswithcode.com/task/image-segmentation)
