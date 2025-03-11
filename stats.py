

def get_num_words(text):
    number_of_words = len(text.split())
    return number_of_words

def get_char_count(text):
    text = text.lower()
    char_count = {key: 0 for key in set(text)}
    for i in text:
        char_count[i] += 1
    return char_count

def sorted_count(dictionary):
    sorted_dict = {key: val for key, val in sorted(dictionary.items(), key=lambda ele: ele[1], reverse=True)}
    return sorted_dict


    