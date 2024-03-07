import pandas as pd
import numpy as np
import plotly.express as px
import scipy.stats as ss
import warnings
warnings.filterwarnings('ignore')


class Cramers:
    
    def __init__(self):
        self.coef_scores=[]
    
    def detect_categorical_columns(self, df, threshold_unique=0.05, threshold_distribution=0.95):
        """ auto-detects categorical columns as per thresholds"""
        categorical_columns = []

        for col in df.columns:
            dtype = df[col].dtype
            unique_count = df[col].nunique()
            value_counts = df[col].value_counts(normalize=True)

            if (dtype == 'object' or dtype.name == 'category') \
                or (unique_count / len(df) <= threshold_unique) \
                or (value_counts.max() >= threshold_distribution):
                categorical_columns.append(col)
        return categorical_columns
    
    
    def cramers_v(self, x, y):
        """ computes cramer's v correlation, given two pandas series objects"""
        confusion_matrix = pd.crosstab(x,y)
        chi2 = ss.chi2_contingency(confusion_matrix)[0]
        n = confusion_matrix.sum().sum()
        phi2 = chi2/n
        r,k = confusion_matrix.shape
        phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
        rcorr = r-((r-1)**2)/(n-1)
        kcorr = k-((k-1)**2)/(n-1)
        return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1))) 
    
    def corr(self,data,add_cols=[],rem_cols=[],plot_htmp=False):
        
        """ main function to calculate cramers correlation given the dataframe"""
        
        categorical_columns=self.detect_categorical_columns(data, threshold_unique=0.05, threshold_distribution=0.95)
        
        for col in add_cols:
            if col not in data.columns:
                raise KeyError(f'Unable to locate column {col} in the dataframe')
            data[col] = data[col].astype('object')
            categorical_columns.append(col)
        categorical_columns = list(set(categorical_columns) - set(rem_cols))
                
        for i in categorical_columns:
            for j in categorical_columns:
                
                """ temp treatment of missing values to override exceptions """
                col1=data[i].fillna(data[i].mode()[0]).values
                col2=data[j].fillna(data[j].mode()[0]).values
                
                coef= self.cramers_v(col1, col2)
                list(self.coef_scores).append(coef)
            
        reshape_val=int(np.sqrt(len(self.coef_scores)))
        self.coef_scores=np.array(self.coef_scores).reshape(-reshape_val,reshape_val)
        
        coef_scores_df=pd.DataFrame(self.coef_scores)
        coef_scores_df.fillna(0, inplace=True)
        coef_scores_df.columns=categorical_columns
        coef_scores_df.index=categorical_columns
    
        if plot_htmp==True:
            fig = px.imshow(coef_scores_df, text_auto=True)
            fig.show()   
        else:
            return coef_scores_df
    
