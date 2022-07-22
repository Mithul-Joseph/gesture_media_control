# Gesture control media player using Machine Learning

This project aims at controlling media player in YouTube using hand gestures. 

## Demo
First let's see how this works (the fun part😅).  

![gif](https://github.com/Mithul-Joseph/gesture_media_control/blob/main/static/Animation.gif)  

The implementation is divided into two parts. One for training and creating the model and the other for programming the gestures.

## Part 1: Teachable Machines

First, lets build a model for recognizing our gestures. There are pre-built models that are available which can be used. For eg: hand pose detection model from media pipe. This model outputs the landmarks from our hand which can be used for recognizing gestures. Since that would be a bit more complicated, I decided to use Google’s [Teachable Machine](https://teachablemachine.withgoogle.com/) to create a machine learning model. The model is created using the images from the webcam or custom images.

For this, open teachable machine website and click on image project. Then click on standard image model. You would get a page like this.

<img src="https://github.com/Mithul-Joseph/gesture_media_control/blob/main/static/Teachable_interface.png" width="350" height="200">

Then use your webcam to add multiple images for each class. Here, I created 3 classes:

Class 1: next song

<img src="https://github.com/Mithul-Joseph/gesture_media_control/blob/main/static/class_1.jpg" width="350" height="200">

Class 2: play/pause

<img src="https://github.com/Mithul-Joseph/gesture_media_control/blob/main/static/class_2.jpg" width="350" height="200">

Class 3: Normal case

<img src="https://github.com/Mithul-Joseph/gesture_media_control/blob/main/static/class_3.jpg" width="350" height="200">

Click on train the model. The training time increases as the number of images in each class increase and the model becomes better with more images since our model has more data to train on. After training the model, I exported the model in .h5 format which is used in the program. 

## Part 2: Programming the gestures

I then used open-cv to retrieve the images from the webcam. These images were resized and normalized. After that the images are passed to the model to get the prediction. Based on these predictions, keyboard inputs were simulated using [keyboard](https://pypi.org/project/keyboard/) package. Since I was trying it out on YouTube, the keyboard shortcuts are ‘Shift+n’ for next song, ‘k’ for play/pause. So, if the model predicted class one, a keyboard press of ‘Shift+n’ is sent to play the next song. If the model predicted class two, a keyboard press of ‘k’ is sent to play/pause the music. 

## How to run?

- Install the requirements from the requirements file.
- Open [YouTube](https://www.youtube.com/).
- Play a video of your choice.
- Run the program and switch back to the YouTube window.
- Use gestures to control the media.
- To quit: switch to the window opened by the program. Press ‘q’ on your keyboard.
