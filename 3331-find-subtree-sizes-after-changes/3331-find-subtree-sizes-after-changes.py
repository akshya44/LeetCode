class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[parent[node]].append(node)

        answer = [1] * n
        previous = [-1] * n
        last = [-1] * 26

        # Iterative DFS: (node, state)
        # state 0 = enter, state 1 = exit
        stack = [(0, 0)]

        while stack:
            node, state = stack.pop()
            char_index = ord(s[node]) - ord('a')

            if state == 0:
                # Find closest ancestor with the same character
                previous[node] = last[char_index]
                last[char_index] = node

                stack.append((node, 1))

                for child in reversed(children[node]):
                    stack.append((child, 0))

            else:
                # Restore the previous ancestor of this character
                last[char_index] = previous[node]

                # Determine the node's new parent
                new_parent = previous[node]

                if new_parent == -1:
                    new_parent = parent[node]

                # Add this subtree's size to its new parent
                if new_parent != -1:
                    answer[new_parent] += answer[node]

        return answer