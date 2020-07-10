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

In this project, seaborn is used for visualization.
First of all, all irrelevant columns like unamed:32, id and diagnosis columns are dropped. THen we view all pair wise correlated columns through correlation graph. All pair wise correlated features are dropped. Because those features may effect us in learning by algorithm. 
