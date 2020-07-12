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

This project is originally divided into to sections. First Section is of Exploratory Data analysis and second section is of Statistic Data Visualization with Seaborn. 
Our Dataset has 33 columns and Diagnosis column is our target variable
First of all, all irrelevant columns like unamed:32, id and diagnosis columns are dropped. THen we view all pair wise correlated columns through correlation graph. All pair wise correlated features are dropped. Because those features may effect us in learning by algorithm. 


## About Requirements.txt

This text file can be generated in two ways. 
First of all move into your working directory. And then choose either of the below mentioned ways.
One of the way is by using folling command:
  pip freeze > requirements.txt.
  
Another way is using pipreqs
Firstly, install pipreqs by pip install pipreqs
And then move into your working directory and type following command:
  pipreqs "directory path"
  
Now you have genereated your requirements.txt file. This file contains all the necessary libraries you used in your project.

