from unit4_trees_graphs import *

# T3: BST operations [cite: 568]
bst = BST()
keys = [50, 30, 70, 20, 40, 60, 80]
for k in keys: bst.insert(k)
print("Initial BST Inorder:", bst.inorder_list(bst.root, []))

for val in [20, 30, 50]:
    bst.delete(val)
    print(f"Inorder after deleting {val}:", bst.inorder_list(bst.root, []))

# T4: Graph BFS [cite: 575]
adj_task5 = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
print("\nGraph BFS from 0:", bfs(adj_task5, 0))

# T6: Shortest Path [cite: 579]
path, dist = shortest_path_unweighted(adj_task5, 0, 4)
print(f"Shortest Path 0 to 4: {path} (Distance: {dist})")