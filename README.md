# Tumour-Detection

## About Dataset

Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.

Ten real-valued features are computed for each cell nucleus:

1) radius (mean of distances from center to points on the perimeter)
2) texture (standard deviation of gray-scale values)
3) perimeter
4) area
5) smoothness (local variation in radius lengths)
6) compactness (perimeter^2 / area - 1.0)
7) concavity (severity of concave portions of the contour)
8) concave points (number of concave portions of the contour)
9) symmetry
10) fractal dimension ("coastline approximation" - 1)

**For Downloading Dataset**
In data, you can download csv file Breast Cancer Feature Dataset. 

## About Project
This project is originally divided into to sections. First Section is of Exploratory Data analysis and second section is of Statistic Data Visualization with Seaborn. 
Our Dataset has 33 columns and Diagnosis column is our target variable whose value we want to predict. So, the values in this column can take only two unique values. And it can be either M and B. 

M indicates malignant tumour
B indicates Benign tumour

So, this makes it Binary Classification problem, sice target variable is binary.

**Heading towards Data Visualization**

For Data Visualization Section, here **seaborn** library is used. Seaborn is Fantastic Data Visualization library. In this phase, you will see how to produce and customize various chart types ith seaborn and also apply **feature selection** and **feature extraction** method with sickit learn. And lastly, there is also gradient boosted Decision tree classifier built with **xgBoost** and classify tumours as either malignant or benign.
And all while using seaborn as primary tool for Data Visualization.



## About Requirements.txt

This text file can be generated in two ways. 
First of all move into your working directory. And then choose either of the below mentioned ways.
One of the way is by using folling command:
  pip freeze > requirements.txt.
  
Another way is using pipreqs
Firstly, install pipreqs by **pip install pipreqs**
And then move into your working directory and type following command:
  **pipreqs "directory path"**
  
Now you have genereated your **requirements.txt** file. This file contains all the necessary libraries you used in your project.

## About Streamlit

Streamlit api is simple and fastest way to create web app of your machine learning model.

You can simply install streamlit by opening Anaconda prompt and type
  **pip install streamlit**
 
To run 
  **streamlit run appname.py**

## ProcFile

For Procfile download it as it is. This file should not contain any extension. And if it contains Heroku will through an exception.
Save this file into your working project directory.

## setup.sh

This script file contains the email statement. Download it and Replace email with yours.
Save this file into working project directory.

These procfile, requirements.text and setup.sh file are for deployment purpose. If you want to deploy your project, use them otherwise just ignore.

## For deployment on Heroku

###### Steps
1) Create Heroku account
2) Installing Heroku Command Line interface (CLI)
3) Open Anaconda Prompt and go to your project directory and type **Heroku Login**
4) Deploy application by following commands
  
  ###### heroku create 
   
   then type ###### git add .
   
   then type ###### git commit -m "some message"
   
   and then ###### git push heroku master
   
   And Tada!! you have deployed your app.
  



