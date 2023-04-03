
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def display(self):
        """
        Display the tree using a pre-order traversal
        """
        self._display_helper(self.root)

    def _display_helper(self, current_node, level=0, direction=None):
        if current_node is not None:
            # Recursively display right subtree
            self._display_helper(current_node.right, level=level + 1, direction='R')

            # Print node and its position in the tree
            if direction == 'R':
                print('     ' * level, '┌──', current_node.value)
            elif direction == 'L':
                print('     ' * level, '└──', current_node.value)
            else:
                print('     ' * level, current_node.value)

            # Recursively display left subtree
            self._display_helper(current_node.left, level=level + 1, direction='L')

    def insert(self, value):
        # Check if the tree is empty, if so set the new node as the root node
        if self.root is None:
            self.root = Node(value)
        else:
            # Start inserting the node from the root node
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        # Check if the new node value is less than the current node value
        if value < current_node.value:
            # Check if the left child of the current node is empty, if so insert the new node as the left child
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                # Recursively insert the new node in the left subtree
                self._insert(value, current_node.left)
        # Check if the new node value is greater than the current node value
        elif value > current_node.value:
            # Check if the right child of the current node is empty, if so insert the new node as the right child
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                # Recursively insert the new node in the right subtree
                self._insert(value, current_node.right)
        # If the value already exists in the tree, do not insert
        # else:
        #     print("Value already exists in the tree")

    def find_min(self, node):
        # Traverse to the leftmost child node to find the minimum value in the subtree
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, value):
        # Check if the tree is empty
        if self.root is None:
            print("Tree is empty")
        else:
            # Start deleting the node from the root node
            self.root = self._delete(value, self.root)

    def _delete(self, value, current_node):
        # Check if the current node is empty
        if current_node is None:
            return current_node

        # Check if the node to be deleted is in the left subtree
        if value < current_node.value:
            current_node.left = self._delete(value, current_node.left)
        # Check if the node to be deleted is in the right subtree
        elif value > current_node.value:
            current_node.right = self._delete(value, current_node.right)
        else:
            # case 1: Node to be deleted has no children
            if current_node.left is None and current_node.right is None:
                current_node = None

            # case 2: Node to be deleted has one child
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left

            # case 3: Node to be deleted has two children
            else:
                # find the minimum value in the right subtree
                temp = self.find_min(current_node.right)

                # replace the value of the node to be deleted with the minimum value
                current_node.value = temp.value

                # delete the minimum node in the right subtree
                current_node.right = self._delete(temp.value, current_node.right)

        return current_node

    def search(self, value):
        # Check if the tree is empty
        if self.root is None:
            print("Tree is empty")
            return None
        # Start searching from the root node
        return self._search(value, self.root)

    def _search(self, value, current_node):
        # Check if the current node contains the value we are searching for
        if current_node.value == value:
            return current_node
        # If the value is less than the current node, search in the left subtree
        if value < current_node.value:
            # Check if the left child of the current node is empty
            if not current_node.left:
                print("No value in tree")
                return None
            # Recursively search in the left subtree
            return self._search(value, current_node.left)
        # If the value is greater than the current node, search in the right subtree
        else:
            # Check if the right child of the current node is empty
            if not current_node.right:
                print("No value in tree")
                return None
            # Recursively search in the right subtree
            return self._search(value, current_node.right)


if __name__ == '__main__':
    b = BST()
    example = [4,5,3,2,4,5,7,3,11,2222,44,6,-1,-6,-9]
    for e in example:
        b.insert(e)

    b.display()




