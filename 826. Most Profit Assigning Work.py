class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dnp = sorted(zip(difficulty, profit))
        worker.sort()

        maximum = 0
        total = 0
        i = 0

        for k in range(len(worker)):
            while i < len(dnp) and dnp[i][0] <= worker[k]:
                maximum = max(maximum, dnp[i][1])
                i += 1
            total = total + maximum

        return total


