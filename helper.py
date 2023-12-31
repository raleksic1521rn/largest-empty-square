import bisect

class MergeSortTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [[] for _ in range(4 * len(arr))]
        self.build_tree(0, 0, len(arr) - 1)

    def build_tree(self, node, start, end):
        if start == end:
            self.tree[node].append(self.arr[start])
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self.build_tree(left_child, start, mid)
            self.build_tree(right_child, mid + 1, end)

            left_idx, right_idx = 0, 0
            left_len, right_len = len(self.tree[left_child]), len(self.tree[right_child])

            while left_idx < left_len and right_idx < right_len:
                if self.tree[left_child][left_idx] < self.tree[right_child][right_idx]:
                    self.tree[node].append(self.tree[left_child][left_idx])
                    left_idx += 1
                else:
                    self.tree[node].append(self.tree[right_child][right_idx])
                    right_idx += 1

            while left_idx < left_len:
                self.tree[node].append(self.tree[left_child][left_idx])
                left_idx += 1

            while right_idx < right_len:
                self.tree[node].append(self.tree[right_child][right_idx])
                right_idx += 1

    def query_util(self, node, start, end, left, right, a, b):
        if start > right or end < left:
            return 0

        if left <= start and right >= end:
            return bisect.bisect_right(self.tree[node], b) - bisect.bisect_left(self.tree[node], a)
         
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        val_left = self.query_util(left_child, start, mid, left, right, a, b)
        val_right = self.query_util(right_child, mid + 1, end, left, right, a, b)

        return val_left + val_right

    def query(self, left, right, a, b):
        if left < 0 or right >= len(self.arr) or left > right:
            return None  

        return self.query_util(0, 0, len(self.arr) - 1, left, right, a, b)
    
   