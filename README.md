Nutrition-Assistant-Application
================================

## Team Info ##

Team_Lead - K.Abarna

M1_Lead   - Devendra Prakash S

M2_Lead   - Govindaraj

M3_Lead   - Gowtham M

M4_Lead   - Mythily

### Introduction: 

Due to the ignorance of healthy food habits, obesity rates are increasing at an alarming speed, and this is reflective of the risks to people’s health. People need to control their daily calorie intake by eating healthier foods, which is the most basic method to avoid obesity. However, although food packaging comes with nutrition (and calorie) labels, it’s still not very convenient for people to refer to App-based nutrient dashboard systems which can analyze real-time images of a meal and analyze it for nutritional content which can be very handy and improves the dietary habits, and therefore, helps in maintaining a healthy lifestyle.

This project aims at building a web App that automatically estimates food attributes such as ingredients and nutritional value by classifying the input image of food.  Our method employs Clarifai's AI-Driven Food Detection Model for accurate food identification and Food API's to give the nutritional value of the identified food.


### Work Flow of the Project:

- User interacts with the Web App to Load an image.
- The image is passed to the server application, which uses Clarifai's AI-Driven Food Detection Model Service to analyze the images and Nutrition API to provide nutritional information about the analyzed Image.
- Nutritional information of the analyzed image is returned to the app for display. 


### Technical Architecture:
![image](https://github.com/DevaAsDev/nutrition_assistant/blob/master/src/structure.png?raw=true)
