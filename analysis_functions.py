import pandas as pd
import numpy as np

"""
Functions to make: 

For all languages, we want to look at:
MAE (with carb ranges: 0-500, 0-25, 25-75, 75+)
Acc (with carb ranges: 0-500, 0-25, 25-75, 75+)
Token use

(How do we handle outliers?)
We need a function to find outliers, ideas:
- naively sort by highest absolute error (biased for large)
- sort by highest % absolute error (biased for small)
- (or something with standard distribution and z score)

We also want to manually look at outliers and see where issues are, either in translation or prediction
ex: ambigious unit of measurement, specific food items that consistently have trends, a language has no good translation word for some food
ex: Other "outliers" we can flag can just be anything with strange/notable behavior, not just high error. (Like manually flagging words without translation)

Once we've found outliers: we repeat analysis for...
MAE (with carb ranges and without outliers)
Acc (with carb ranges and without outliers)


Other idea: for each language: do analysis but focused on words (like cup or barley). Could be a way to find biases specific to languages:
ex: for each language, sort (all of the) WORDS by absolute error of the queries its in 
    - different versions with/without carb ranges and outliers
"""

def analyze_mae(data, thresholds, language_paths):
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()
    
    resource_colors = {'high': '#910000', 'medium': '#D64545', 'low': '#FF7A7A'}
    
    for i, t in enumerate(thresholds):
        if len(t) == 3:
            t_min, t_max, t_label = t
        else:
            t_min, t_max = t
            t_label = f"{t_min}-{t_max}g"
            
        rows = []
        for language, df in data.items():
            subset = df[(df['carb_truth'] >= t_min) & (df['carb_truth'] <= t_max)]
            if len(subset) > 0:
                y_true = subset['carb_truth'].values
                y_pred = subset['carb_prediction'].values
                rows.append({'language': language, 'mae': mae(y_true, y_pred)})
        
        if rows:
            df_res = pd.DataFrame(rows).sort_values('mae')
            colors = [resource_colors.get(language_paths.get(lang, {}).get('resource', ''), '#888888') for lang in df_res['language']]
            axes[i].bar(df_res['language'], df_res['mae'], color=colors)
            axes[i].set_ylabel('MAE (grams)')
            axes[i].set_xlabel('Language')
            axes[i].set_title(f'MAE by Language ({t_label})')
            axes[i].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()



def accuracy(y_true, y_pred, value=7.5):
    return np.mean(np.abs(y_true - y_pred) <= value)

def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))
