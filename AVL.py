# Set a threshold to determine when to rotate the tree
THRESHOLD = 1


class NodeAVL:
    """
    Define a Node class to represent nodes in an AVL tree
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0



class BST_AVL:
    """
    Define a BST_AVL class to represent the AVL tree
    """
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
        """
        Insert a new node into the tree
        """
        # If the tree is empty, create a new root node
        if self.root is None:
            self.root = NodeAVL(value)
        else:
            # Call the recursive insert helper function
            self.root = self._insert(self.root, value, THRESHOLD)

    def _insert(self, node, key, threshold):
        # If the current node is None, create a new node with the given key
        if not node:
            return NodeAVL(key)

        # Recursively insert the key into the left or right subtree
        if key < node.value:
            node.left = self._insert(node.left, key, threshold)
        elif key > node.value:
            node.right = self._insert(node.right, key, threshold)
        else:
            # If the key is already in the tree, return the current node
            return node

        # Update the height of the current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Check if the tree is unbalanced and rotate as necessary
        balance = self.get_balance(node)

        if balance > threshold:
            if self.get_balance(node.left) >= 0:
                node = self.rotate_right(node)
            else:
                node = self.rotate_left_right(node)  # node.left is right-heavy
        elif balance < -threshold:
            if self.get_balance(node.right) <= 0:
                node = self.rotate_left(node)
            else:
                node = self.rotate_right_left(node)  # node.right is left-heavy

        return node


    def rotate_right(self, node):
        """
        Perform a right rotation to balance the tree
        """
        left_temp = node.left

        node.left = left_temp.right
        left_temp.right = node

        # Update heights of rotated nodes based on subtree heights
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_temp.height = 1 + max(self.get_height(left_temp.left), self.get_height(left_temp.right))

        return left_temp

    def rotate_left(self, node):
        """
        Perform a left rotation to balance the tree
        """
        right_temp = node.right

        node.right = right_temp.left
        right_temp.left = node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_temp.height = 1 + max(self.get_height(right_temp.left), self.get_height(right_temp.right))

        return right_temp

    def rotate_left_right(self, node):
        # Perform a left rotation on the node's left child
        node.left = self.rotate_left(node.left)
        # Then perform a right rotation on the node itself
        return self.rotate_right(node)

    def rotate_right_left(self, node):
        # Perform a right rotation on the node's right child
        node.right = self.rotate_right(node.right)
        # Then perform a left rotation on the node itself
        return self.rotate_left(node)

    def get_balance(self, node):
        # Check if node is empty
        if not node:
            return 0
        # Calculate the balance factor of the node
        return self.get_height(node.left) - self.get_height(node.right)

    def get_height(self, node):
        # Check if node is empty
        if not node:
            return -1
        # Return the height of the node
        return node.height

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
    b = BST_AVL()
    example = [4, 5, 3, 2, 4, 5, 7, 3, 11, 2222, 44, 6, -1, -6, -9]
    for e in example:
        b.insert(e)

    b.display()

