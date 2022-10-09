
# Python package for easy spearman's rank correlation coef comparison for continuous features in Pandas DataFrames (similar to data.corr() for default pearson's coef in Pandas) 

<a href='https://stats.stackexchange.com/questions/8071/how-to-choose-between-pearson-and-spearman-correlation'> Why and When to choose Spearman over Pearson? </a> 

<h3>Run: </h3>

```
git clone https://github.com/ayanatherate/pdspearcorr.git
cd pdspearcorr 
pip install -r requirements.txt
```

<h3> If using ipynb notebooks:</h3>


```
!git clone https://github.com/ayanatherate/pdspearcorr.git

```



<br>
<h3>Open any Notebook/IDE: </h3>

```
import pandas as pd
from pdspearcorr import spearcorr
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

#Alternatively for plotting heatmap, can also use sns.heatmap(spearcorr.cal(data))

```
<img width="477" alt="image" src="https://user-images.githubusercontent.com/59755186/194780600-295fd3d9-6bdb-4fe7-9511-d204747f097e.png">

<h3> For custom adding numerical columns for spearcorr.cal comaprison use: </h3>

```
spearcorr.cal(data, add_cols=['target'])
# added column should be present in the dataset provided 

```
<h3> For custom removing numerical(or redundant) columns for spearcorr.cal comparison use: </h3>

```
spearcorr.cal(data, rem_cols=['sepal_width'])

```





