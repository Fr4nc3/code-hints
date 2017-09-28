class BinaryTreeNode:
    def __init__(self, a_name, a_left_child=None, a_right_child=None):
        self.name = a_name
        self.left_child = a_left_child
        self.right_child = a_right_child

    def add_left_child(self, a_left_child):
        self.left_child = a_left_child

    def add_right_child(self, a_right_child):
        self.right_child = a_right_child

    def print_pre_order(self):
        print(self.name)
        if self.left_child:
            self.left_child.print_pre_order()
        if self.right_child:
            self.right_child.print_pre_order()

binary_tree_111 = BinaryTreeNode("111")
binary_tree_112 = BinaryTreeNode("112")
binary_tree_121 = BinaryTreeNode("121")
binary_tree_122 = BinaryTreeNode("122")
binary_tree_211 = BinaryTreeNode("211")
binary_tree_212 = BinaryTreeNode("212")
binary_tree_221 = BinaryTreeNode("221")
binary_tree_222 = BinaryTreeNode("222")
binary_tree_11 = BinaryTreeNode("11", binary_tree_111, binary_tree_112)
binary_tree_12 = BinaryTreeNode("12", binary_tree_121, binary_tree_122)
binary_tree_21 = BinaryTreeNode("21", binary_tree_211, binary_tree_212)
binary_tree_22 = BinaryTreeNode("22", binary_tree_221, binary_tree_222)
binary_tree_1 = BinaryTreeNode("1", binary_tree_11, binary_tree_12)
binary_tree_2 = BinaryTreeNode("2", binary_tree_21, binary_tree_22)
binary_tree = BinaryTreeNode("binary_tree", binary_tree_1, binary_tree_2)

binary_tree.print_pre_order()