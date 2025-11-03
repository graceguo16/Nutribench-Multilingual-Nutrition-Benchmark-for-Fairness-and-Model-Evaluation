import pandas as pd

def load_csvs_from_dict(language_paths, carb_range=None, indexes_to_exclude=None):
    data = {}
    
    for language, info in language_paths.items():
        if not info['include']:
            continue
            
        df = pd.read_csv(info['path'])
        df = df.sort_values('carb_truth')
        
        if carb_range is not None:
            min_carbs, max_carbs = carb_range
            df = df[(df['carb_truth'] >= min_carbs) & (df['carb_truth'] <= max_carbs)]
        
        if indexes_to_exclude is not None:
            df = df[~df['index'].isin(indexes_to_exclude)] # masks excluded indexes
        
        data[language] = df
    
    return data