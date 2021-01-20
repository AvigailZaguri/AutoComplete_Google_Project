from AutoCompleteData import *
import os
import pickle


from datetime import datetime


# note : treat errors

def get_path_list(startpath):
    path_list = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        middle_path = os.path.basename(root)
        all_path = startpath + '/'
        if level ==1:
            all_path += middle_path
            all_path += '/'
        if level == 2:
            all_path += 'python-3.8.4-docs-text/'
            all_path +=  middle_path
            all_path += '/'
        for file_path in files:
            path_list.append(all_path + file_path)

    return path_list

def print_now_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time strart =", current_time)

def biuld_tree(file_path):
    print_now_time()

    path_list = get_path_list(file_path)
   
    auto_complete_tree = Node("")
    curr_root = auto_complete_tree

    for path in path_list:
        print(path)
        try:
            with open(path, 'r', encoding="utf8") as file:
                line = file.readline()
                line_counter = 1
                while line != '':  
                    if line != '\n':
                        if line[-1] == '\n':
                            line = line[:-1]
                        line = line[0:200]
                        index = 0
                        while (line[index] == ' '):
                            index +=1
                        
                        # splitted_list= line.split(" ")
                        # for i in range(index, len(splitted_list)):
                        #     str_sentence = " ".join(splitted_list[i:])
                        #     last_index = 1
                        #     for char in str_sentence[:-1]:
                        #         if str(char).isalnum() or char == " ":
                        #             curr_root = curr_root.add_child(char)
                        #             last_index+=1
                        #         else:
                        #             continue
                        #         if last_index == 15:
                        #             break
                        #     curr_root = curr_root.add_child(str_sentence[-1], AutoCompleteData(line, (path, line_counter), i, None))
                        #     curr_root = auto_complete_tree

                        for i in range(index , len(line)):
                            last_index = 1
                            for char in line[i:-1]:
                                if str(char).isalnum() or char == " ":
                                    curr_root = curr_root.add_child(char)
                                    last_index+=1
                                else:
                                    continue
                                if last_index == 5:
                                    break
                            curr_root = curr_root.add_child(line[-1], AutoCompleteData(line, (path, line_counter), i, None))
                            curr_root = auto_complete_tree

                        # # autoCompleteData = (path, line_counter)
                        # splitted_list= line.split(" ")
                        # for i in range(index, len(splitted_list)):
                        #     str_sentence = " ".join(splitted_list[i:])
                        #     for char in str_sentence:
                        # #     for char in line[i:-1]:
                        #         if str(char).isalnum() or char == " ":
                        #             curr_root = curr_root.add_child(char)
                        #         else:
                        #             continue
                        #     # curr_root = curr_root.add_child(line[-1], autoCompleteData)
                        #     curr_root = curr_root.add_child(line[-1], AutoCompleteData(line, (path, line_counter), i, None))
                        #     #curr_root = curr_root.add_child(line[-1], AutoCompleteData(line, (path, line_counter), 0, None))
                        #     curr_root = auto_complete_tree
                    line = file.readline()
                    line_counter += 1
        except:
            print("error: ", path)

    print_now_time()

    with open('auto_complete_tree_word_avigail.obj', 'wb') as fp:
        pickle.dump(auto_complete_tree, fp)
        
    print("end")

    print_now_time()



