from AutoCompleteData import *

def update_list_exactly_text(user_txt, loaded_tree, res_list):
    list_completions = get_all_completions(user_txt, loaded_tree)
    for completition in list_completions:
        completition.set_score(len(user_txt) * 2)
        res_list.append(completition)
   

def get_score_of_swap_text(index):
    switcher = {
        0: 5,
        1: 4,
        2: 3,
        3: 2
    }
    return switcher.get(index, 1)

def get_score_of_miss_add_text(index):
    switcher = {
        0: 10,
        1: 8,
        2: 6,
        3: 4
    }
    return switcher.get(index, 2)

def update_list_swap_text(user_txt, loaded_tree, res_list):
    chars_list = [asci_char for asci_char in range(ord('a'), ord('z')+1)]
    chars_list.append(ord(' '))
    source_txt = user_txt
    for char_index in range(len(user_txt)):
        source_char = user_txt[char_index]
        minus_score = get_score_of_swap_text(char_index)
        for asci_char in chars_list:
            if source_char.lower() != chr(asci_char):
                user_txt = source_txt[:char_index]   + chr(asci_char) + source_txt[char_index +1:] 
                list_completions = get_all_completions(user_txt, loaded_tree)
                for comletion in list_completions:
                    comletion.set_score((len(user_txt)-1) * 2 - minus_score)
                    res_list.append(comletion)
        user_txt = source_txt

                
def update_list_adding_text(user_text, loaded_tree, res_list):
    source_txt = user_text
    for char_index in range(1, len(source_txt) -1):
        user_txt = source_txt[:char_index]  + source_txt[char_index +1:] 
        list_completions = get_all_completions(user_txt, loaded_tree)
        minus_score = get_score_of_miss_add_text(char_index)
        
        for comletion in list_completions:
            comletion.set_score(len(user_txt) * 2 - minus_score)
            res_list.append(comletion)


def update_list_missing_text(user_text, loaded_tree, res_list):
    source_txt = user_text
    for char_index in range(len(source_txt)):
        minus_score = get_score_of_miss_add_text(char_index)
        for asci_char in range(ord('a'), ord('z')+1):
                adding_char = chr(asci_char)
                user_txt = source_txt[:char_index]  + adding_char + source_txt[char_index:] 
                list_completions = get_all_completions(user_txt, loaded_tree)
                for comletion in list_completions:
                    comletion.set_score((len(source_txt)) * 2 - minus_score)
                    res_list.append(comletion)

def get_5_high_score(res_list):

    high_score_list = []
    
    for i in range(5):
        if res_list:
            highly_index = 0
            for index in range(len(res_list)):
                if res_list[index].get_score() > res_list[highly_index].get_score():
                    highly_index = index
                elif res_list[index].get_score() == res_list[highly_index].get_score(): 
                    if res_list[index].get_offset() < res_list[highly_index].get_offset():
                        highly_index = index
            high_score_list.append(res_list[highly_index])
            res_list.pop(highly_index)
    return high_score_list
    
def get_top_5_sentences(user_text, loaded_tree):
    res_list = []
    update_list_exactly_text(user_text, loaded_tree, res_list)
    update_list_swap_text(user_text, loaded_tree, res_list)
    update_list_adding_text(user_text, loaded_tree, res_list)
    update_list_missing_text(user_text, loaded_tree, res_list)
    
    if res_list:
        res_list = get_5_high_score(res_list)

    return res_list

def print_sentences(top_5_sentences):
    for i in range(len(top_5_sentences)):
        print(str(i+1) + '. ', top_5_sentences[i])

