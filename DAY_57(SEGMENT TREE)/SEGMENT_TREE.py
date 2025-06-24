class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

def main():
    data = list(map(int, input("Enter the elements of the array: ").split()))
    seg_tree = SegmentTree(data)

    while True:
        print("\nMenu:")
        print("1. Update an element")
        print("2. Range query")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            pos = int(input("Enter the position to update (0-indexed): "))
            value = int(input("Enter the new value: "))
            seg_tree.update(pos, value)
            print("Element updated.")
        elif choice == 2:
            left = int(input("Enter the left index of the range (0-indexed): "))
            right = int(input("Enter the right index of the range (exclusive): "))
            result = seg_tree.query(left, right)
            print(f"Sum of elements in range ({left}, {right}): {result}")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
