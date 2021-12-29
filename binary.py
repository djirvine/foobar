# Create Node class for binary tree structure
class Node():
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None


# function to build perfect binary tree of height h given a root node
def build_tree(h, node):

    # If another level can be added, then add a left and right node
    if h > 0:
        # add left node and record parent then recurse to add next level
        node.left = Node(h)
        node.left.parent = node
        build_tree(h-1, node.left)

        # add right node and record parent then recurse to add next level
        node.right = Node(h)
        node.right.parent = node
        build_tree(h-1, node.right)

    # success
    return 0


# function to label tree in post order
def post_order_name(tree_root,n):
    # recursively search left branch to leaf found
    if tree_root.left != None:
        n = post_order_name(tree_root.left, n)
    # then search right branch
    if tree_root.right != None:
        n = post_order_name(tree_root.right, n)
    # set name of current node
    tree_root.name = n
    # increment n after naming branch and return
    n += 1
    return n

# function to do post order search of tree
def search_post_order(tree_root, node):
    # initialize above
    above = None
    # recurse downthe left branch
    if tree_root.left != None:
        above = search_post_order(tree_root.left, node)
        # if we have found the node then skip the rest of the search
        if above != None:
            return above
    if tree_root.right != None:
        above = search_post_order(tree_root.right, node)
        # if we have found the node then skip the rest of the search
        if above != None:
            return above

    # check if we have found the searched for node
    if tree_root.name == node:

        # get the parent node
        if tree_root.parent == None:
            above = -1
        else:
            above = tree_root.parent.name
        # print(f"Found it, above = {above}")

    return above


def solution(h, q):

    # create root node for tree
    root = Node(h)

    # build tree of the required height
    build_tree(h - 1, root)

    # set name for first node
    n = 1

    # traverse tree in post_order and name nodes starting with n = 1
    post_order_name(root, n)

    # search tree for node from list
    # number of highest node number is 2^h - 1
    # initialize p to blank list
    p = []

    # search for all nodes in the list q
    for node in q:
        above = search_post_order(root, node)
        p.append(above)

    return p

# test cases
# print(solution(3,[7, 3, 5,1]))
# print(solution(5,[19, 14, 28]))


