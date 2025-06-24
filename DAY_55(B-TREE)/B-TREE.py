class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.leaf = leaf  # True if leaf node, otherwise False
        self.keys = []  # List of keys
        self.children = []  # List of child pointers

    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=' ')
        if not self.leaf:
            self.children[len(self.keys)].traverse()

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == k:
            return self
        if self.leaf:
            return None
        return self.children[i].search(k)


class BTree:
    def __init__(self, t):
        self.root = None  # Root node
        self.t = t  # Minimum degree

    def traverse(self):
        if self.root is not None:
            self.root.traverse()

    def search(self, k):
        if self.root is None:
            return None
        else:
            return self.root.search(k)

    def insert(self, k):
        if self.root is None:
            self.root = BTreeNode(self.t, leaf=True)
            self.root.keys.append(k)
        else:
            if len(self.root.keys) == 2 * self.t - 1:
                s = BTreeNode(self.t, leaf=False)
                s.children.append(self.root)
                self.split_child(s, 0)
                i = 0
                if s.keys[0] < k:
                    i += 1
                self.insert_non_full(s.children[i], k)
                self.root = s
            else:
                self.insert_non_full(self.root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and x.keys[i] > k:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and x.keys[i] > k:
                i -= 1
            i += 1
            if len(x.children[i].keys) == 2 * self.t - 1:
                self.split_child(x, i)
                if x.keys[i] < k:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(t, y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]


# User interaction
def main():
    t = int(input("Enter the minimum degree of the B-Tree: "))
    btree = BTree(t)

    while True:
        print("\nMenu:")
        print("1. Insert")
        print("2. Traverse")
        print("3. Search")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter the key to insert: "))
            btree.insert(key)
        elif choice == 2:
            print("B-Tree traversal: ", end='')
            btree.traverse()
            print()
        elif choice == 3:
            key = int(input("Enter the key to search: "))
            result = btree.search(key)
            if result:
                print(f"Key {key} found in the B-Tree")
            else:
                print(f"Key {key} not found in the B-Tree")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()