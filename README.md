# Mask Detector
---
Facial recognition software to detect whether or not someone who is entering a store/home has a face mask properly on.
If not, it alerts employee's or people around them to this fact, so that they may properly position their mask for safe use. 
Makes use of a Raspberry Pi 3, Webcam, and some hardware.

## Hardware
- Raspberry Pi 3 B 
- Raspberry Pi Camera
- Power Supply 
## Software
Using:
- Raspbian OS
- Python3
- Git
- Python3-Pip
## Packages/Libraries
- Tensorflow.keras
- OpenCV
- numpy
- Pillow
## How It Works
Our Raspberry PI 3 B will continously take pictures, checking if you are wearing a mask or not. First, it recognizes 
your face, and makes sure you are a person. After, it checks if you have a mask on by using a machine learning algorithm. 
If no mask it on, it alerts you by blinking several Red LEDs. If a mask is on, then Green LEDs will blink.
## Usage
Can be used in wide applications, from personal to commerical. Some applications that may apply are:
- Store fronts, ensuring everyone entering wears a mask
- House/Apartment, so you don't forget your mask at home
- Schools and Hospitals
- Any indoor space 

