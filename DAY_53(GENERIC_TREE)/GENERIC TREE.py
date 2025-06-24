class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def build_tree():
    """Build a generic tree based on user input."""
    nodes = {}
    print("Enter nodes in the format: Parent Child (or 'done' to finish):")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == "done":
            break
        parent, child = user_input.split()
        
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child)
        
        nodes[parent].add_child(nodes[child])
    
    root_key = next(iter(nodes.keys()))
    return nodes[root_key]


def dfs_search(node, target):
    """Perform DFS to search for a value in the tree."""
    if not node:
        return False

    print(f"Visiting node: {node.value}")
    if node.value == target:
        return True

    for child in node.children:
        if dfs_search(child, target):
            return True
    
    return False

if __name__ == "__main__":
    print("Build your tree:")
    root = build_tree()
    
    search_value = input("Enter value to search: ").strip()
    found = dfs_search(root, search_value)
    if found:
        print(f"Value '{search_value}' found in the tree!")
    else:
        print(f"Value '{search_value}' not found in the tree.")