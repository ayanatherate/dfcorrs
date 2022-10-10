
## Python package for implementing Cramer's V correlation coef comparison between categorical features in Pandas DataFrames (similar to data.corr() for default pearson's coef in Pandas) 

<h4> Automatically detects categorical features and ignores numerical features. Also has custom feature addition/removal option. 


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

```

from dfcorrs import cramersvcorr

cramersvcorr.cal(data) #cramer's v corr comparison between all categorical features, returns a Pandas datframe similar to .corr()

cramersvcorr.cal(data, plot_htmp=True) #plots heatmap using plotly

cramersvcorr.cal(data)[#feature_name] #one-to-all comparison 

```







<h3> For custom adding categorical columns for cramers corr comparison use: </h3>

```
cramersvcorr.cal(data, add_cols=['feature_name'])
# added column should be present in the dataset provided 
```




<h3> For custom removing categorical(or redundant) columns for cramers corr comparison, use: </h3>

```
cramersvcorr.cal(data, rem_cols=['feature_name'])

```





