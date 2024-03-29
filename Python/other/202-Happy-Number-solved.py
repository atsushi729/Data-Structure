class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0

        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output


"""
Version 2
"""
class SolutionV2:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumSquareDigits(n)

            if n == 1:
                return True

        return False

    def sumSquareDigits(self, n):
        output = 0

        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output


if __name__ == "__main__":
    solution = Solution()
    n = 19
    print(solution.isHappy(n))
