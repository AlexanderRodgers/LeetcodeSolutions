from typing import List

"""
Time Complexity:
    O(n) for creating the sparse vector
    O(L + L2) for calculating the dot product
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0
        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result

nums = [1,0,0,2,3]
tc = SparseVector([0,3,0,4,0])
sv = SparseVector(nums)
res = sv.dotProduct(tc)
print(res)