class TreeNode:
    def __init__(self, data, parent=None, next_sibling=None, prev_sibling=None, children=None):
        self.data = data
        self.parent = parent
        self.next_sibling = next_sibling
        self.prev_sibling = prev_sibling
        if children is None:
            children = []
        self.children = children


# TODO implement Tree
class Tree:

    def create_node(self, data):
        return TreeNode(data)

    def insert_node(self):
        # TODO logic to insert a node
        pass

    @staticmethod
    def create_tree_from_dict(dict_data: dict):
        pass
