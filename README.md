
## Python package for easy spearman's rank/Cramer's V correlation coef comparison for continuous & categorical features in Pandas DataFrames (similar to data.corr() for default pearson's coef in Pandas) 

<h4> Automatically detects continuous/categorical features. Also has custom feature addition/removal option. </h4>

<a href='https://stats.stackexchange.com/questions/8071/how-to-choose-between-pearson-and-spearman-correlation'> Why and When to choose Spearman over Pearson? </a> 

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

<h3> Spearman's Correlation for Continuous features </h3>

```
import pandas as pd
from dfcorrs import spearcorr
from sklearn import datasets

iris = datasets.load_iris()
data=pd.DataFrame(iris.data)
data.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']


spearcorr.cal(data) #if not using notebooks, please use print()

```
<img width="233" alt="image" src="https://user-images.githubusercontent.com/59755186/194780467-953738b6-760f-45dc-81f1-82b1fead00c7.png">

```
spearcorr.cal(data)['sepal_len']

```
<img width="149" alt="image" src="https://user-images.githubusercontent.com/59755186/194780556-b233ce49-0788-4c54-bff7-739518ff94e0.png">

```
spearcorr.cal(data,plot_htmp=True)



```
<img width="530" alt="image" src="https://user-images.githubusercontent.com/59755186/194838931-b6a40317-0e80-473d-899e-15963face937.png">


<h3> Cramer's v correlation for Categorical features </h3>

```
#same as spearman's, cramersvcorr.cal(data) instead

from dfcorrs import cramersvcorr

cramersvcorr.cal(data) #cramer's v corr comparison between all categorical features

cramersvcorr.cal(data, plot_htmp=True) #plots heatmap using plotly

cramersvcorr.cal(data)[#feature_name] #one-to-all comparison 

```


<h3> For custom adding numerical columns for spearman corr comparison use: </h3>

```
spearcorr.cal(data, add_cols=['sepal_diameter'])
# added column should be present in the dataset provided 

```



<h3> For custom removing numerical(or redundant) columns for spearman corr comparison, use: </h3>

```
spearcorr.cal(data, rem_cols=['sepal_width'])

```
<h3> For custom adding categorical columns for cramers corr comparison use: </h3>

```
cramersvcorr.cal(data, add_cols=['target'])
# added column should be present in the dataset provided 
```




<h3> For custom removing categorical(or redundant) columns for cramers corr comparison, use: </h3>

```
cramersvcorr.cal(data, rem_cols=['feature_name'])

```





