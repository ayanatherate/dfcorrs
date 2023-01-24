# -*- coding: utf-8 -*-


from cramer_func import cramers_v
def cal(data,add_cols=[],rem_cols=[],plot_htmp=False):
    
    
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import scipy.stats as ss
    
    import warnings
    warnings.filterwarnings('ignore')
    
    
    num_cols=data.corr().columns
    cat_cols=[cols for cols in data.columns if not cols in num_cols]

    

    for i in add_cols:
        if i not in data.columns:
            print('Added Columns not found in Original Dataframe')
        else:
            cat_cols.append(i)
    
    
    
    if len(rem_cols)>0:
        for i in rem_cols:
            if i in cat_cols:
                cat_cols.remove(i)
            else:
                pass
                
                
    coef_scores=[]

    for i in cat_cols:
        for j in cat_cols:
            coef= cramer_func.cramers_v(data[i], data[j])
            coef_scores.append(coef)
            
    reshape_val=int(np.sqrt(len(coef_scores)))
    coef_scores=np.array(coef_scores).reshape(-reshape_val,reshape_val)
    
    coef_scores_df=pd.DataFrame(coef_scores)
    coef_scores_df.columns=cat_cols
    coef_scores_df.index=cat_cols
    
    if plot_htmp==True:
        fig = px.imshow(coef_scores_df, text_auto=True)
        fig.show()
        
    else:
        return coef_scores_df


