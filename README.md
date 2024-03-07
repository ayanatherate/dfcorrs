
<h3>Implement pairwise categorical correlations (with heatmap) of all columns in Pandas Dataframes in just one line of code.</h3>

[![Test in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1CbxvL9EytlqXzRlsMKPno6DVECDiVAUC#scrollTo=xi26-mMGdtNG)


<img width="890" alt="image" src="https://github.com/ayanatherate/dfcorrs/assets/59755186/d781b4ba-f9f5-464c-b703-f611ae83906b">
<img width="911" alt="image" src="https://github.com/ayanatherate/dfcorrs/assets/59755186/5e8752b1-e967-4e57-8a99-ce30c1197f1c">
<img width="906" alt="image" src="https://github.com/ayanatherate/dfcorrs/assets/59755186/dd10b7fa-90da-4b71-be6c-37bc52796d50">



<h4> Automatically detects categorical features and ignores numerical features. Also has custom feature addition/removal option. 

<h4> Inspiration: <a href="https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_V">Wikipedia page Cramer's v </a>

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
from dfcorrs.cramersvcorr import Cramers
import pandas as pd

cramers=Cramers()
data=pd.read_csv(r'../adatasetwithlotsofcategoricalandcontinuousfeatures.csv')

cramers.corr(data) #cramer's v corr comparison between all categorical features, 
                       #returns a Pandas datframe similar to .corr()

cramers.corr(data, plot_htmp=True) #plots correlation heatmap using plotly

cramers.corr(data)[#feature_name] #single out a categorical feature and observe correlations, returns Pandas Series

```



<h3> At times, a categorical feature might be falsely interpreted by Pandas as a continuous feature by default (Example: 'City Code', 'Candidate ID') and vice-versa. Hence, to solve that problem : </h3>

<br>



<h3> For custom adding categorical columns for cramers corr comparison use: </h3>

```
cramers.corr(data, add_cols=['feature_name'])

# added column should be present in the dataset provided
# kindly use .astype('str') to force-convert falsely identified continuous columns (if any) before using.
```




<h3> For custom removing categorical(or redundant) columns for cramers corr comparison, use: </h3>

```
cramers.corr(data, rem_cols=['feature_name'])

```





