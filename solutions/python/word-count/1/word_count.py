def count_words(sentence):

    DICT = {}

    punctuation = "_!&@$%^&.,!?;:()[]{}'\""

    clean = sentence.replace('_',' ')

    white = clean.replace(',',' ')
    
    words = [word.strip(punctuation) for word in white.lower().split()]

    for word in words:
        if word in DICT:
            DICT[word] += 1
        else:
            DICT[word] = 1

    return DICT
