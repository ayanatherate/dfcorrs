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
    num_cols=num_cols+add_cols
    
    if len(rem_cols)>0:
        for i in rem_cols:
            if i in num_cols:
                num_cols.remove(i)
                
                
    coef_scores=[]

    for i in num_cols:
        for j in num_cols:
            coef, p = spearmanr(data[i], data[j])
            coef_scores.append(coef)
            
    reshape_val=int(np.sqrt(len(coef_scores)))
    coef_scores=np.array(coef_scores).reshape(-reshape_val,reshape_val)
    
    coef_scores_df=pd.DataFrame(coef_scores)
    coef_scores_df.columns=num_cols
    coef_scores_df.index=num_cols
    
    if plot_htmp==True:
        plt.figure(figsize=(16,7))
        sns.heatmap(coef_scores_df,annot=True)
        plt.show()
    else:
        return coef_scores_df


                
    
