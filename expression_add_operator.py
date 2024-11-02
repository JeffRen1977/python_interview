from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.target = target

        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res

    def dfs(self, num, fstr, fval, flast, res):
        # fstr = string of current formula
        # fval = value of current formula
        # flast = last value for +- and last computing result for * in formula.
        if not num:
            if fval == self.target:
                res.append(fstr)
            return

        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], fstr + '+' + val, fval + int(val), int(val), res)
                self.dfs(num[i:], fstr + '-' + val, fval - int(val), -int(val), res)
                self.dfs(num[i:], fstr + '*' + val, fval - flast + flast * int(val), flast * int(val), res)


def main():
    solution = Solution()

    # Test cases
    test_cases = [
        ("123", 6, ["1+2+3", "1*2*3"]),  # Example 1
        ("232", 8, ["2*3+2", "2+3*2"]),  # Example 2
        ("105", 5, ["1*0+5", "10-5"]),  # Example 3
        ("00", 0, ["0+0", "0-0", "0*0"]),  # Edge case: All zeroes, target 0
        ("3456237490", 9191, []),  # Edge case: No solution exists
        ("123456789", 45, ["12+34-5+6-7+8+9"]),  # Large input case
    ]

    # Run each test case
    for i, (num, target, expected) in enumerate(test_cases):
        result = solution.addOperators(num, target)
        result.sort()  # Sort the result to match the sorted expected for comparison
        expected.sort()  # Sort the expected as the order of expressions does not matter
        print(f"Test Case {i + 1}: Input: num='{num}', target={target}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("")


# Run the main function
if __name__ == "__main__":
    main()
