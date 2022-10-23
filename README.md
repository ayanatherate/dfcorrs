
## Python package for implementing Cramer's V correlation coef comparison between categorical features in Pandas DataFrames (similar to data.corr() for default pearson's coef in Pandas) 

<h4> Automatically detects categorical features and ignores numerical features. Also has custom feature addition/removal option. 

<h3> Inspiration: 'The Search for Categorical Correlation'- post in Towards Data Science by <a href='https://github.com/shakedzy'> Shakedzy</a>. Link to the post: <a href='https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9'> Click Here </a>

<h3>Run: </h3>

```
git clone https://github.com/ayanatherate/dfcorrs.git
cd dfcorrs 
pip install -r requirements.txt
```

<h3> If using ipynb notebooks:</h3>


```
!git clone https://github.com/ayanatherate/dfcorrs.git

```



<br>
<h3>Open any Python Notebook/IDE: </h3>



<h3> Cramer's v correlation for Categorical features </h3>
<h4> Would take some time to compute, depending on number of features/records. </h4>
  
  
```

from dfcorrs import cramersvcorr
import pandas as pd
  
data=pd.read_csv(r'../adatasetwithlotsofcategoricalandcontinuousfeatures.csv')

cramersvcorr.cal(data) #cramer's v corr comparison between all categorical features, 
                       #returns a Pandas datframe similar to .corr()

cramersvcorr.cal(data, plot_htmp=True) #plots correlation heatmap using plotly

cramersvcorr.cal(data)[#feature_name] #single out a categorical feature and observe correlations, returns Pandas Series

```



<h2> At times, a categorical feature might be falsely interpreted by Pandas as a continuous feature by default (Example: 'City Code', 'Candidate ID') and vice-versa. Hence, to solve that problem : </h2>

<br>



<h3> For custom adding categorical columns for cramers corr comparison use: </h3>

```
cramersvcorr.cal(data, add_cols=['feature_name'])

# added column should be present in the dataset provided
# kindly use .astype('str') to force-convert falsely identified continuous columns (if any) before using.
```




<h3> For custom removing categorical(or redundant) columns for cramers corr comparison, use: </h3>

```
cramersvcorr.cal(data, rem_cols=['feature_name'])

```





