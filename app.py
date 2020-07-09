import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import streamlit as st 
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.feature_selection import RFECV
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.metrics import accuracy_score


def main():

	data = pd.read_csv('data/data.csv')
	y = data.diagnosis          
	drop_cols = ['Unnamed: 32','id','diagnosis']
	x = data.drop(drop_cols,axis = 1 )
	pca = PCA()



	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

	x_train_N = (x_train-x_train.mean())/(x_train.max()-x_train.min())
	x_test_N = (x_test-x_test.mean())/(x_test.max()-x_test.min())

	pca.fit(x_train_N)
	st.title("Tumour Diagnosis: Feature Selection and Classification")

	st.header("About Dataset")
	st.write("Ten real-valued features are computed for each cell nucleus:")

	st.write("1) radius (mean of distances from center to points on the perimeter)")
	st.write("2) texture (standard deviation of gray-scale values)")
	st.write("3) perimeter")
	st.write("4) area")
	st.write("5) smoothness (local variation in radius lengths)")
	st.write("6) compactness (perimeter^2 / area - 1.0)")
	st.write("7) concavity (severity of concave portions of the contour)")
	st.write("8) concave points (number of concave portions of the contour)")
	st.write("9) symmetry")
	st.write("10) fractal dimension")

	st.write("""
	# View Data
	""")
	st.dataframe(data.head())

	df=pd.DataFrame(data=np.cumsum(pca.explained_variance_ratio_))
	drop_list1 = ['perimeter_mean','radius_mean','compactness_mean',
              'concave points_mean','radius_se','perimeter_se',
              'radius_worst','perimeter_worst','compactness_worst',
              'concave points_worst','compactness_se','concave points_se',
              'texture_worst','area_worst']
	x_1 = x.drop(drop_list1,axis = 1 )    

	st.write("""
	# After Dropping all Correlated Columns
	""")
	st.dataframe(x_1.head())

	x_train, x_test, y_train, y_test = train_test_split(x_1, y, test_size=0.3, random_state=42)

	clf_rf = xgb.XGBClassifier(random_state=43)      
	clr_rf = clf_rf.fit(x_train,y_train)

	ac = accuracy_score(y_test,clf_rf.predict(x_test))
	print('Accuracy is: ',ac)
	st.write('Accuracy is: ' ,ac)
	cm = confusion_matrix(y_test,clf_rf.predict(x_test))
	sns.heatmap(cm,annot=True,fmt="d");
	st.pyplot()

	clf_rf_4 = xgb.XGBClassifier()
	rfecv = RFECV(estimator=clf_rf_4, step=1, cv=5,scoring='accuracy')   
	rfecv = rfecv.fit(x_train, y_train)

	num_features = [i for i in range(1, len(rfecv.grid_scores_) + 1)]
	cv_scores = rfecv.grid_scores_

	sns.set(style="whitegrid")
	ax = sns.lineplot(x=num_features, y=cv_scores)
	ax.set(xlabel="Number of features selected", ylabel="CV scores of selected features");
	st.write("""
	#  Plot number of features VS. cross-validation scores
	""")
	st.pyplot()


	st.write("""
	#  Feature Extraction using Principal Component Analysis
	""")
	x_train_N = (x_train-x_train.mean())/(x_train.max()-x_train.min())
	x_test_N = (x_test-x_test.mean())/(x_test.max()-x_test.min())

	sns.set()
	plt.figure(1, figsize=(10, 9))
	sns.lineplot(data=np.cumsum(pca.explained_variance_ratio_))
	plt.xlabel('number of components')
	plt.ylabel('cumulative explained variance');

	st.pyplot()


if __name__ == '__main__':
    main()