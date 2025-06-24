def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')  
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {}
    
    print("Enter your graph (adjacency list). Type 'done' when finished.")
    while True:
        node = input("Enter node (or 'done' to finish): ")
        if node.lower() == 'done':
            break
        neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
        graph[node] = neighbors
    
    start_node = input("Enter the starting node: ")
    
    print("\nDFS traversal from the starting node:")
    visited = set()  
    dfs(graph, start_node, visited)
