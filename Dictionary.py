
from RedBlackTree import RedBlackTree

class Dictionary:
    def __init__(self):
        self.__rbTree = RedBlackTree()

    def load(self, filename):
        with open(f'{filename}.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.__rbTree.insert(line[:-1])
    
    def look_up(self, word):
        return self.__rbTree.search(word) 

    def insert_word(self, word):
        if self.look_up(word):
            print("ERROR: Word already in the dictionary!")
        else:
            self.__rbTree.insert(word)
            print(self.size())
            print(self.rbTree_height())

    def size(self):
        return self.__rbTree.get_size()

    def rbTree_height(self):
        return self.__rbTree.get_height()