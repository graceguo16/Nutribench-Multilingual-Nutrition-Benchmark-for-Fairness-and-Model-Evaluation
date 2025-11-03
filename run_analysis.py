import data_loader as dl
import analysis_functions as af

LANGUAGE_PATHS = {
    'english': {
        'path': 'language_outputs/english_output.csv',
        'resource': 'high',
        'include': True
    },
    'russian': {
        'path': 'language_outputs/russian_output.csv',
        'resource': 'high',
        'include': True
    },
    'german': {
        'path': 'language_outputs/german_output.csv',
        'resource': 'high',
        'include': True
    },
    'chinese': {
        'path': 'language_outputs/chinese_output.csv',
        'resource': 'high',
        'include': True
    },
    'japanese': {
        'path': 'language_outputs/japanese_output.csv',
        'resource': 'high',
        'include': True
    },
    'french': {
        'path': 'language_outputs/french_output.csv',
        'resource': 'high',
        'include': True
    },
    'spanish': {
        'path': 'language_outputs/spanish_output.csv',
        'resource': 'high',
        'include': True
    },
    'italian': {
        'path': 'language_outputs/italian_output.csv',
        'resource': 'high',
        'include': True
    },
    'portuguese': {
        'path': 'language_outputs/portuguese_output.csv',
        'resource': 'high',
        'include': True
    },
    'vietnamese': {
        'path': 'language_outputs/vietnamese_output.csv',
        'resource': 'high',
        'include': True
    },
    'turkish': {
        'path': 'language_outputs/turkish_output.csv',
        'resource': 'medium',
        'include': True
    },
    'indonesian': {
        'path': 'language_outputs/indonesian_output.csv',
        'resource': 'medium',
        'include': True
    },
    'swedish': {
        'path': 'language_outputs/swedish_output.csv',
        'resource': 'medium',
        'include': True
    },
    'arabic': {
        'path': 'language_outputs/arabic_output.csv',
        'resource': 'medium',
        'include': True
    },
    'persian': {
        'path': 'language_outputs/persian_output.csv',
        'resource': 'medium',
        'include': True
    },
    'korean': {
        'path': 'language_outputs/korean_output.csv',
        'resource': 'medium',
        'include': True
    },
    'greek': {
        'path': 'language_outputs/greek_output.csv',
        'resource': 'medium',
        'include': True
    },
    'thai': {
        'path': 'language_outputs/thai_output.csv',
        'resource': 'medium',
        'include': True
    },
    'hindi': {
        'path': 'language_outputs/hindi_output.csv',
        'resource': 'medium',
        'include': True
    },
    'ukrainian': {
        'path': 'language_outputs/ukrainian_output.csv',
        'resource': 'medium',
        'include': True
    },
    'bengali': {
        'path': 'language_outputs/bengali_output.csv',
        'resource': 'low',
        'include': True
    },
    'tamil': {
        'path': 'language_outputs/tamil_output.csv',
        'resource': 'low',
        'include': True
    },
    'urdu': {
        'path': 'language_outputs/urdu_output.csv',
        'resource': 'low',
        'include': True
    },
    'burmese': {
        'path': 'language_outputs/burmese_output.csv',
        'resource': 'low',
        'include': True
    },
    'swahili': {
        'path': 'language_outputs/swahili_output.csv',
        'resource': 'low',
        'include': True
    },
}

INDEXES_TO_EXCLUDE = {
    # Ex: 1, 15, 23, 45
}

CARB_RANGE = (0, 99999) # Determines what queries are included in analysis. Almost always include all of them.

CARB_THRESHOLDS = [(0, 99999), (0, 25), (25, 75), (75, 99999)] # Will analyze these ranges regardless of CARB_RANGE



def main():
    data = dl.load_csvs_from_dict(LANGUAGE_PATHS, carb_range=CARB_RANGE, indexes_to_exclude=INDEXES_TO_EXCLUDE)
    af.analyze_mae(data, CARB_THRESHOLDS, LANGUAGE_PATHS)

if __name__ == "__main__":
    main()