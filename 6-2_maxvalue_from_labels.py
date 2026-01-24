from typing import List
from collections import Counter


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        # Zip values and labels, then sort them in descending order based on values.
        options = sorted(zip(values, labels), reverse=True)  # Sorts by value descending

        # Counter to track how many times each label is used.
        used_labels = Counter()

        # List to keep the selected values
        res = []

        # Iterate through sorted options and pick items based on constraints.
        for value, label in options:
            # Stop if we've already selected the desired number of items
            if len(res) >= num_wanted:
                break

            # Only add the value if the label's count is below the use limit
            if used_labels[label] < use_limit:
                used_labels[label] += 1
                res.append(value)

        # Return the sum of selected values
        return sum(res)


def main():
    solution = Solution()

    # Test Case 1
    values1 = [5, 4, 3, 2, 1]
    labels1 = [1, 1, 2, 2, 3]
    num_wanted1 = 3
    use_limit1 = 1
    result1 = solution.largestValsFromLabels(values1, labels1, num_wanted1, use_limit1)
    print(f"Test Case 1 Result: {result1} (Expected: 9)")

    # Test Case 2: Multiple items with the same label
    values2 = [9, 8, 8, 7, 6]
    labels2 = [1, 1, 2, 2, 2]
    num_wanted2 = 3
    use_limit2 = 2
    result2 = solution.largestValsFromLabels(values2, labels2, num_wanted2, use_limit2)
    print(f"Test Case 2 Result: {result2} (Expected: 25)")

    # Test Case 3: No restrictions (use_limit higher than number of items)
    values3 = [5, 4, 3, 2, 1]
    labels3 = [1, 1, 1, 1, 1]
    num_wanted3 = 5
    use_limit3 = 10
    result3 = solution.largestValsFromLabels(values3, labels3, num_wanted3, use_limit3)
    print(f"Test Case 3 Result: {result3} (Expected: 15)")

    # Test Case 4: Single item wanted
    values4 = [5, 4, 3]
    labels4 = [1, 1, 2]
    num_wanted4 = 1
    use_limit4 = 1
    result4 = solution.largestValsFromLabels(values4, labels4, num_wanted4, use_limit4)
    print(f"Test Case 4 Result: {result4} (Expected: 5)")

    # Test Case 5: Edge case with num_wanted = 0
    values5 = [5, 4, 3, 2]
    labels5 = [1, 2, 3, 4]
    num_wanted5 = 0
    use_limit5 = 1
    result5 = solution.largestValsFromLabels(values5, labels5, num_wanted5, use_limit5)
    print(f"Test Case 5 Result: {result5} (Expected: 0)")


main()
