def transform(legacy_data):
    DICT = {}

    for key,value in legacy_data.items():
        for LETTER in value:
            DICT[LETTER.lower()] = key #assigning value is square not curly brackets 

    return DICT