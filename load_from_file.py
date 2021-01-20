import pickle


def load_tree():
    print("Loading the files....")
    with open('auto_complete_tree_word_avigail.obj', 'rb') as f:
        return pickle.load(f)