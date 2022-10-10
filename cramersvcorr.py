# -*- coding: utf-8 -*-
def cal(data,add_cols=[],rem_cols=[],plot_htmp=False):
    
    
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from scipy.stats import spearmanr
    
    import warnings
    warnings.filterwarnings('ignore')
    
    
    num_cols=list(data.corr().columns)
    cat_cols=[i for i in data.columns if not i in num_cols]
    cat_cols=cat_cols+add_cols
    
    if len(rem_cols)>0:
        for i in rem_cols:
            if i in cat_cols:
                cat_cols.remove(i)
                
    def cramers_v(x, y):
        
        import scipy.stats as ss
        
        confusion_matrix = pd.crosstab(x,y)
        chi2 = ss.chi2_contingency(confusion_matrix)[0]
        n = confusion_matrix.sum().sum()
        phi2 = chi2/n
        r,k = confusion_matrix.shape
        phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
        rcorr = r-((r-1)**2)/(n-1)
        kcorr = k-((k-1)**2)/(n-1)
        
        return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))
                
                
    coef_scores=[]

    for i in cat_cols:
        for j in cat_cols:
            coef= cramers_v(data[i], data[j])
            coef_scores.append(coef)
            
    reshape_val=int(np.sqrt(len(coef_scores)))
    coef_scores=np.array(coef_scores).reshape(-reshape_val,reshape_val)
    
    coef_scores_df=pd.DataFrame(coef_scores)
    coef_scores_df.columns=cat_cols
    coef_scores_df.index=cat_cols
    
    if plot_htmp==True:
        plt.figure(figsize=(16,16))
        sns.heatmap(coef_scores_df,annot=True)
        plt.show()
        
    else:
        return coef_scores_df


