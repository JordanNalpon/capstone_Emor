# Jordan David Nalpon
# GA - DSI 19 Capstone Project
# EmoR (Emotion Recognition)
---
## Index
## [ Introduction ](#introduction)
- [Executive Summary](#i-esum)
- [Problem Statement](#i-ps)
- [Materials](#i-mat)

## [Set Up](#setup)

## [EmoR](#emor)
- [EmoR - Emor - Convolutional Neural Network (CNN)](#emor-cnn)
- [EmoR - Haar Casade Frontalface](#emor-hc)
- [EmoR - Shape Predictor 68](#emor-68)

## [Credits](#cre-dit)
---

<a id="introduction"></a>
## Introduction

<a id="i-esum"></a>
### Executive Summary 

Children with Autism often find it hard to recognise and manage emotions which can result in a lot of problems as they grow. This can result unnecessary miscommunication, confusion and confrontations. 

<a name="i_ps"></a>
### Problem Statement 

One of the major problems faced by people with Autism is reading facial emotions and reacting accordingly. Currently children with Autism are being trained in schools to read emotions with still images, photographs and mirrors to understand and learn about facial emotions. However, there is a jump between school environment to the real world on reading emotions. The goal of this project is to reduce the gap between the school environment and the real world to help better equip the students.

<a id="i-mat"></a>
### Materials 

The main dataset used in this project is from the Kaggle project, "[Face expression recognition dataset](https://www.kaggle.com/jonathanoheix/face-expression-recognition-dataset)". The dataset incldues a training and validation set of 7 emotions; angry, disgust, fear, happy, neutral, sad and surprise.

<a id="setup"></a>
## Set Up 

1. Clone the project from github https://github.com/JordanNalpon/emor
2. Create folder on the same level and name it " 05_external_folder "
3. Download the materials from gdrive link https://drive.google.com/drive/folders/1mtG6qakRYTMif618mwEKSTGrAiKCCtaN?usp=sharing
4. Place all downloaded materials in the "05_external_folder"

<a id ="emor"></a>
## Emor
EmoR is a python based programme that goes through an image, detect if there is a face and predicts what emotions the face is making. The current emotions that it can detect are; angry, fear, happy, digust, neutral, sad and surprise.

EmoR is made up of 3 major components; the Convolutional Neural Network (CNN) model, Haar Casade Frontalface pre-trained model and Shape Predictor 68 pre-trained model.

<a id ="emor-cnn"></a>
## Emor  - Convolutional Neural Network (CNN)

EmoR uses a Convolutional Neural Network (CNN) model on the Kaggle dataset and produces a model that knows the features of the different emotions. The kaggle set has over 35,000 different images over 7 emotions.

However the dataset contains a lot of noise like cartoon characters or emojis which can affect the prediction model. Using a library like face_recognition is able to sweep through the dataset and able to point out which images contain a face or not.

This comes at a cost as there are several face images that did not pass through the face_recognition library and were thrown into the negative pile. I've included the negative images in github to take a look at these images.

It will take a lot of manual sorting through the images to the correct emotions and some emotions like sad, neutral and fear can have similar facial expressions which can lead to some confusion in the model.

<a id ="emor-hc"></a>
## Emor  - Haar Casade Frontalface

This Haar Casade helps to find faces in the image and give the coordinates of the faces. It looks for features like ear, mouth, nose and chin and once it fulfill these requirements, there should be a face in the image.

<a id ="emor-68"></a>
## Emor - Shape Predictor 68

Shape Predictor 68 places 68 points on a face and able to track the distances of each point. So if the points on the eyes have their distance shorten, the eye should be closing. This will help the model to register what is the face current shape and the CNN model will predict based on the output of the 68 points.


<a id ="cre-dit"></a>
## Credits

Joyce Zheng work was a huge help for this project. You can view her work here. </br>
https://towardsdatascience.com/video-facial-expression-detection-with-deep-learning-applying-fast-ai-d9dcfd5bcf10

Ivan Tan for being the best Teacher Assistant ever

Conor Smyth for being a patient teacher for my Data Science Journey

Haresh and Terence for letting me use their office in times of need. Plese check out their podcast 'YaLahBut' on Spotify

Ramanya for always being awesome and there for me
