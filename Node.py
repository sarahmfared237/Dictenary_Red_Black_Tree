class Node:

    def __init__(self, value, color = 'R'):
        self.__value = value
        self.__color = color

        # If not Nil node
        if value != None:
            self.__parent = Nil.get_instance()
            self.__left_node = Nil.get_instance()
            self.__right_node = Nil.get_instance()

    def get_grand_parent(self):
        if self.get_parent() == Nil.get_instance():
            return Nil.get_instance()
        
        return self.get_parent().get_parent()
    
    def get_uncle(self):
        if self.get_parent() == Nil.get_instance() or self.get_grand_parent() == Nil.get_instance():
            return Nil.get_instance()

        if self.get_grand_parent().get_left_node() == self.get_parent():
            return self.get_grand_parent().get_right_node()

        return self.get_grand_parent().get_left_node()

    def set_parent(self, parent:'Node'):
        self.__parent = parent

    def get_parent(self) -> 'Node':
        return self.__parent

    def set_left_node(self, left_node:'Node'):
        self.__left_node = left_node

    def get_left_node(self) -> 'Node':
        return self.__left_node

    def set_right_node(self, right_node:'Node'):
        self.__right_node = right_node

    def get_right_node(self) -> 'Node':
        return self.__right_node

    def get_value(self):
        return self.__value
    
    def change_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f"{self.get_value()}({self.get_color()})"   
    

# Singleton Nil class
class Nil():
    __instance = None

    def __init__(self):
        if Nil.__instance is not None:
            raise Exception("Nil instance already exists.")
        Nil.__instance = Node(None, 'B')
        Nil.__instance.set_parent(None)
    
    def __str__(self):
        return f"Nil"   
    
    @staticmethod
    def get_instance():
        if Nil.__instance is None:
            Nil()
        return Nil.__instance
    