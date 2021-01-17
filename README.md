# Mask Detector
---
In light of recent events and the significant impact that COVID-19 has had on our daily lives, our team of 4 has
decided to create an easily implementable technology that could better protect the public and reduce the spread of COVID-19. 

We have created a facial recognition software to detect whether or not someone is properly wearing a face mask using machine
learning algorithms. The associated actions could range from alerting a system operator, to opening automated doors, or 
prompting unmasked persons to put a mask on. There are numerous potential applications that may stem from this project, 
and we believe that the flexibility of our implementation could make a significant impact on public health.


## Hardware
- Raspberry Pi 3B 
- Raspberry Pi Camera
- Power Supply 

## Software
Using:
- Linux/Ubuntu
- Raspbian OS
- Python3, PIP
- Git/Github

## Packages/Libraries
- Tensorflow.keras
- OpenCV
- numPy
- Pillow


## How It Works
When activated, our Raspberry PI 3B will continously take pictures of the person in question, going through several steps
to determine if a mask is being worn properly.
1) Using OpenCV's integrated facial recognition algorithms, we first determine if there is a human face(s) present in the view
2) Upon recognizing a human face, the program then checks if you have a mask on by using a TensorFlow machine learning model
   that we trained. 
3) If the program determines that the person is not wearing a mask, you will be alerted by several blinking red LEDs. 
   If a mask is being worn correctly, then green LEDs will blink instead.


## Real Life Application
Can be used in a variety of situations to improve personal safety, hygiene, and adherence to regulations.
Potential applications range from personal use to commerical implementations. Some usages could include:

- Store fronts / Public Areas
    - Could be connected to an automated gate, removing need for human moderation 
- House / Apartment Buildings
    - Protect yourself and delivery personnel
    - Could set up reminder in case you forget to wear a mask
    - Could be further developed into facial recognition to unlock door
- Schools and Hospitals
    - Ensure students, patients, visitors are properly protected
    - Reduce spread in high-risk areas such as hospitals, schools with young children
