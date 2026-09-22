class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_count = [[0] * k for _ in range(4 * n)]

        def merge(node: int, left_child: int, right_child: int):
            tree_prod[node] = (tree_prod[left_child] * tree_prod[right_child]) % k
            lp = tree_prod[left_child]
            
            cnt = list(tree_count[left_child])
            r_cnt = tree_count[right_child]
            for r in range(k):
                if r_cnt[r]:
                    cnt[(lp * r) % k] += r_cnt[r]
            tree_count[node] = cnt

        def build(node: int, l: int, r: int):
            if l == r:
                val = nums[l] % k
                tree_prod[node] = val
                tree_count[node][val] = 1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            merge(node, 2 * node, 2 * node + 1)

        def update(node: int, l: int, r: int, idx: int, val: int):
            if l == r:
                v = val % k
                tree_prod[node] = v
                tree_count[node] = [0] * k
                tree_count[node][v] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, r, idx, val)
            merge(node, 2 * node, 2 * node + 1)

        def query(node: int, l: int, r: int, ql: int, qr: int, cur_prod: int, cur_counts: list[int]) -> int:
            if ql <= l and r <= qr:
                for rem in range(k):
                    if tree_count[node][rem]:
                        cur_counts[(cur_prod * rem) % k] += tree_count[node][rem]
                return (cur_prod * tree_prod[node]) % k

            mid = (l + r) // 2
            if ql <= mid:
                cur_prod = query(2 * node, l, mid, ql, qr, cur_prod, cur_counts)
            if qr > mid:
                cur_prod = query(2 * node + 1, mid + 1, r, ql, qr, cur_prod, cur_counts)
            return cur_prod

        build(1, 0, n - 1)

        ans = []
        for idx, val, start, x in queries:
            nums[idx] = val
            update(1, 0, n - 1, idx, val)
            
            res_counts = [0] * k
            query(1, 0, n - 1, start, n - 1, 1, res_counts)
            ans.append(res_counts[x])

        return ans