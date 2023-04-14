from Node import Node, Nil

class RedBlackTree:
    def __init__(self):
        self.__root = Nil.get_instance()
        self.__size = 0
        self.__height = 0

    def get_root(self) -> Node:
        return self.__root

    def set_root(self, root:Node):
        self.__root = root
        
    def get_size(self) -> Node:
        return self.__size

    def inc_size(self):
        self.__size += 1

    def get_height(self) -> Node:
        return self.__height

    def inc_height(self, root:Node):
        self.__height += 1

    def search(self, root:Node, data):
        if root == Nil.get_instance():
            return False
        if root.get_value == data:
            return True
        elif data > root.get_value:
            return self.search(root.get_right_node, data)
        else:
            return self.search(root.get_left_node, data)
        
    def left_rotate(self, x:Node):
        y = x.get_right_node()
        x.set_right_node(y.get_left_node())

        if y.get_left_node() != Nil.get_instance():
            y.get_left_node().set_parent(x)

        y.set_parent(x.get_parent())

        if x.get_parent() == Nil.get_instance():
            self.set_root(y)
        
        elif x == x.get_parent().get_left_node():
            x.get_parent().set_left_node(y)

        else:
            x.get_parent().set_right_node(y)

        y.set_left_node(x)

        x.set_parent(y)

    def right_rotate(self, y:Node):
        x = y.get_left_node()
        y.set_left_node(x.get_right_node())

        if x.get_right_node() != Nil.get_instance():
            x.get_right_node().set_parent(y)

        x.set_parent(y.get_parent())

        if y.get_parent() == Nil.get_instance():
            self.set_root(x)
        
        elif y == y.get_parent().get_right_node():
            y.get_parent().set_right_node(x)

        else:
            y.get_parent().set_left_node(x)

        x.set_right_node(y)

        y.set_parent(x)

    def print_red_black_tree(self):
        self.print_tree_helper(self.get_root(), "", True)

    def print_tree_helper(self, node:Node, indent, last):
        if node is not Nil.get_instance():
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "

            color = 'R' if node.get_color() == 'red' else 'B'
            print(node.get_value() + "(" + color + ")")
            self.print_tree_helper(node.get_left_node(), indent, False)
            self.print_tree_helper(node.get_right_node(), indent, True)


    def insert(self, data):
        pass


rb = RedBlackTree()
rb.set_root(Node('4','B'))
rb.get_root().set_left_node(Node('2', 'R'))
rb.get_root().get_left_node().set_right_node(Node('3', 'R'))
rb.left_rotate(rb.get_root().get_left_node())
rb.print_red_black_tree()
