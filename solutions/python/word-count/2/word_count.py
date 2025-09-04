def count_words(sentence):
    DICT = {}
    words = []
    current = ""
    
    for chr in sentence.lower():
        # include letters, digits, and internal apostrophes
        if chr.isalnum() or (chr == "'" and current):
            current += chr
        else:
            if current:
                # remove leading/trailing apostrophes (but keep internal ones)
                word = current.strip("'")
                if word:             # only add if word is not empty
                    words.append(word)
                current = ""         # reset for next word

    # catch last word if sentence ends with a letter/digit
    if current:
        word = current.strip("'")
        if word:
            words.append(word)
    
    # count occurrences
    for word in words:
        if word in DICT:
            DICT[word] += 1
        else:
            DICT[word] = 1

    return DICT
