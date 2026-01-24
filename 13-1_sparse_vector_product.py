from typing import List


# SparseVector class as provided
class SparseVector:
    def __init__(self, nums: List[int]):
        # Store only non-zero elements as (index, value)
        self.elements = [(i, num) for i, num in enumerate(nums) if num != 0]

    def dotProduct(self, vec: 'SparseVector') -> int:
        # Use two pointers to traverse both sparse vectors
        p1 = p2 = 0
        result = 0
        elements1, elements2 = self.elements, vec.elements

        while p1 < len(elements1) and p2 < len(elements2):
            index1, value1 = elements1[p1]
            index2, value2 = elements2[p2]

            if index1 == index2:
                # If indices match, multiply values and add to result
                result += value1 * value2
                p1 += 1
                p2 += 1
            elif index1 < index2:
                # Move pointer 1 if its index is smaller
                p1 += 1
            else:
                # Move pointer 2 if its index is smaller
                p2 += 1

        return result


# Main function to test the SparseVector class
def main():
    # Example input lists
    nums1 = [1, 0, 0, 2, 3]
    nums2 = [0, 3, 0, 4, 0]

    # Create two sparse vectors
    vec1 = SparseVector(nums1)
    vec2 = SparseVector(nums2)

    # Calculate the dot product of vec1 and vec2
    result = vec1.dotProduct(vec2)

    # Print the result
    print(f"The dot product of vec1 and vec2 is: {result}")


# Run the main function
if __name__ == "__main__":
    main()
