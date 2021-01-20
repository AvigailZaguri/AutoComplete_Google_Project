from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score
    
    def set_score(self, score):
        self.score = score
    
    def get_score(self):
        return self.score
    
    def get_offset(self):
        return self.offset

    def __str__(self):
        return self.completed_sentence + self.source_text.__str__()
  

class Node(object):
    def __init__(self, prefix):
        self.prefix = prefix  # sentance
        self.complete_senteces = []
        self.children = dict()


    def add_child(self, char, line_data = None):
        if self.prefix != '' and self.prefix[-1] == ' ' and char == ' ':
            return self
        if not self.children.get(char.lower()):    
            self.children[char.lower()] = Node(self.prefix + char)
        if line_data:
            self.children[char.lower()].complete_senteces.append(line_data)

        return self.children[char.lower()]  

    def __str__(self):
        res = self.prefix + "  children: \n"
        for k in self.children:
            res += self.children[k].__str__() + " "
        return res

    def get_leaves(self):
        list_res = []
        self.get_leaves_recursive(list_res)
        return list_res

    def get_leaves_recursive(self, lst):
        for sentence in self.complete_senteces:
                lst.append(sentence)

        if self.children:
            for v in self.children.values():
                v.get_leaves_recursive(lst)


def get_all_completions(txt, root: Node):
    if txt == "":
        return root.get_leaves()
    if root.children:
       
        if txt[0].isalnum() or (txt[0] == ' ' and (len(txt)==1 or (len(txt)>1 and txt[1] !=' '))):   
            cur_node = root.children.get(txt[0].lower())    
        else:
            cur_node = root
             
        if cur_node:
            return get_all_completions(txt[1:], cur_node)

    return []

