
## Python package for easy spearman's rank/Cramer's V correlation coef comparison for continuous & categorical features in Pandas DataFrames (similar to data.corr() for default pearson's coef in Pandas) 

<h4> Automatically detects continuous features. Also has custom feature addition/removal option. </h4>

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
<h3>Open any Notebook/IDE: </h3>

<h3> Spearman's Correlation for Continuous features </h3>

```
import pandas as pd
from dfcorrs import spearcorr
from sklearn import datasets

iris = datasets.load_iris()
data=pd.DataFrame(iris.data)
data.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']


dfcorrs.spear(data) #if not using notebooks, please use print()

```
<img width="233" alt="image" src="https://user-images.githubusercontent.com/59755186/194780467-953738b6-760f-45dc-81f1-82b1fead00c7.png">

```
dfcorrs.spear(data)['sepal_len']

```
<img width="149" alt="image" src="https://user-images.githubusercontent.com/59755186/194780556-b233ce49-0788-4c54-bff7-739518ff94e0.png">

```
dfcorrs.spear(data,plot_htmp=True)

#Alternatively for plotting heatmap, can also use sns.heatmap(spearcorr.cal(data))

```
<img width="481" alt="image" src="https://user-images.githubusercontent.com/59755186/194782414-f2341565-cd0e-4c12-81dc-9c2ab8cafc2d.png">
<h3> Scramer's v correlation for Categorical features </h3>

```
#same as spearman's, dfcorrs.cramer(data) instead
dfcorrs.cramer(data) #cramer's v corr comparison between all categorical features

dfcorrs.cramer(data, plot_htmp=True) #plots heatmap using seaborn

dfcorrs.cramer(data)[#feature_name] #one-to-all comparison 

```


<h3> For custom adding numerical columns for spearman corr comparison use: </h3>

```
dfcorrs.spear(data, add_cols=['target'])

```

# added column should be present in the dataset provided 

<h3> For custom removing numerical(or redundant) columns for spearman corr comparison, use: </h3>

```
spearcorr.cal(data, rem_cols=['sepal_width'])

```
<h3> For custom adding categorical columns for cramers corr comparison use: </h3>

```
dfcorrs.spear(data, add_cols=['target'])

```

# added column should be present in the dataset provided 


<h3> For custom removing categorical(or redundant) columns for cramers corr comparison, use: </h3>

```
spearcorr.cal(data, rem_cols=['feature_name'])

```





