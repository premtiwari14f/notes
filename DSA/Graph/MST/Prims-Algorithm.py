import heapq
from typing import List

class Solution:
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[List[int]]]) -> int:
        vis = set()
        mst_hq = [(0, 0, -1)]  # (cost, node, parent)
        heapq.heapify(mst_hq)
        sm = 0
        mst_edges = []

        while len(mst_hq) > 0:
            cost, node, parent = heapq.heappop(mst_hq)
            if node in vis:
                continue
            vis.add(node)
            sm += cost
            if parent != -1:
                mst_edges.append((parent, node, cost))
            
            for neighbor, edge_cost in adj[node]:
                if neighbor not in vis:
                    heapq.heappush(mst_hq, (edge_cost, neighbor, node))
        print(mst_edges)
        return sm

# Test cases
# Function to run test cases
def run_test_case(test_num, V, adj, expected):
    sol = Solution()
    result = sol.spanningTree(V, adj)
    if result == expected:
        print(f"Test Case {test_num}: ✅ Passed")
    else:
        print(f"Test Case {test_num}: ❌ Failed (Expected {expected}, Got {result})")

# Running test cases
if __name__ == "__main__":
    # Test Case 1: Basic case
    run_test_case(1, 
        3, 
        [
            [[1, 5], [2, 1]],  # Node 0 -> (1,5), (2,1)
            [[0, 5], [2, 3]],  # Node 1 -> (0,5), (2,3)
            [[0, 1], [1, 3]]   # Node 2 -> (0,1), (1,3)
        ], 
        4
    )

    # Test Case 2: Single edge
    run_test_case(2, 
        2, 
        [
            [[1, 5]],  # Node 0 -> (1,5)
            [[0, 5]]   # Node 1 -> (0,5)
        ], 
        5
    )

    # Test Case 3: Graph with multiple equal weight edges
    run_test_case(3, 
        4, 
        [
            [[1, 1], [2, 2]],  # Node 0
            [[0, 1], [2, 1], [3, 1]],  # Node 1
            [[0, 2], [1, 1], [3, 1]],  # Node 2
            [[1, 1], [2, 1]]   # Node 3
        ], 
        3
    )

    # Test Case 4: Large graph
    run_test_case(4, 
        6, 
        [
            [[1, 3], [2, 1]],  # Node 0
            [[0, 3], [2, 3], [3, 6]],  # Node 1
            [[0, 1], [1, 3], [3, 5], [4, 4]],  # Node 2
            [[1, 6], [2, 5], [4, 2], [5, 7]],  # Node 3
            [[2, 4], [3, 2], [5, 9]],  # Node 4
            [[3, 7], [4, 9]]  # Node 5
        ], 
        17
    )

    # Test Case 5: Graph with a cycle
    run_test_case(5, 
        4, 
        [
            [[1, 1], [2, 5]],  # Node 0
            [[0, 1], [2, 2], [3, 3]],  # Node 1
            [[0, 5], [1, 2], [3, 4]],  # Node 2
            [[1, 3], [2, 4]]  # Node 3
        ], 
        6
    )
