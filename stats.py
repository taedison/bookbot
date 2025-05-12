def count_words(text):
    text_list = text.split()
    text_num = 0
    for words in text_list:
        text_num += 1
    return text_num

def count_characters(text):
    text_lowcase = text.lower()
    character_dict = {}
    for char in text_lowcase:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    sorted_dict = []

    for char, count in dict.items():
        char_data = {"char": char, "num": count}
        sorted_dict.append(char_data)

    sorted_dict.sort(reverse = True, key = sort_on)

    return sorted_dict

