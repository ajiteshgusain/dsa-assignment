class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Task 3: Tree Reconstruction
def build_tree(preorder, inorder):
    if not inorder:
        return None
    root_val = preorder.pop(0)
    root = Node(root_val)
    idx = inorder.index(root_val)
    root.left = build_tree(preorder, inorder[:idx])
    root.right = build_tree(preorder, inorder[idx+1:])
    return root

# Task 4: BST Operations 
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node: return Node(key)
        if key < node.val: node.left = self._insert(node.left, key)
        else: node.right = self._insert(node.right, key)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node: return None
        if key < node.val: node.left = self._delete(node.left, key)
        elif key > node.val: node.right = self._delete(node.right, key)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            temp = self._min_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        return node

    def _min_node(self, node):
        while node.left: node = node.left
        return node

    def inorder_list(self, node, res):
        if node:
            self.inorder_list(node.left, res)
            res.append(node.val)
            self.inorder_list(node.right, res)
        return res

# Task 6 & 7: Graph Algorithms 
def bfs(adj, start):
    visited, queue, order = {start}, [start], []
    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return order

def shortest_path_unweighted(adj, src, dst):
    queue = [[src]]
    visited = {src}
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == dst:
            return path, len(path) - 1
        for neighbor in adj.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None, 0