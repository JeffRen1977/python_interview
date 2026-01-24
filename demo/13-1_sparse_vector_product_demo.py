from typing import List


class SparseVectorDemo:
    def __init__(self, nums: List[int]):
        print(f"\n{'='*60}")
        print(f"Creating SparseVector from: {nums}")
        print(f"{'='*60}")
        
        # Store only non-zero elements as (index, value)
        self.elements = [(i, num) for i, num in enumerate(nums) if num != 0]
        
        print(f"\nOriginal vector (length {len(nums)}):")
        print(f"  Index: {' '.join(f'{i:4}' for i in range(len(nums)))}")
        print(f"  Value: {' '.join(f'{v:4}' for v in nums)}")
        
        print(f"\nSparse representation (only non-zero elements):")
        if self.elements:
            print(f"  Elements: {self.elements}")
            for idx, (i, val) in enumerate(self.elements):
                print(f"    [{idx}] index={i}, value={val}")
        else:
            print(f"  Elements: [] (all zeros)")
        
        print(f"\nStorage efficiency:")
        print(f"  Original: {len(nums)} elements")
        print(f"  Sparse: {len(self.elements)} elements")
        print(f"  Space saved: {len(nums) - len(self.elements)} elements")

    def dotProduct(self, vec: 'SparseVectorDemo') -> int:
        print(f"\n{'='*60}")
        print(f"Computing Dot Product")
        print(f"{'='*60}")
        
        print(f"\nVector 1 sparse elements: {self.elements}")
        print(f"Vector 2 sparse elements: {vec.elements}")
        
        # Use two pointers to traverse both sparse vectors
        p1 = p2 = 0
        result = 0
        elements1, elements2 = self.elements, vec.elements
        
        print(f"\nInitial: p1={p1}, p2={p2}, result={result}")
        print(f"{'─'*60}")
        
        iteration = 0
        
        while p1 < len(elements1) and p2 < len(elements2):
            iteration += 1
            index1, value1 = elements1[p1]
            index2, value2 = elements2[p2]
            
            print(f"\n📍 Iteration {iteration}:")
            print(f"   p1={p1}, p2={p2}")
            print(f"   elements1[{p1}] = ({index1}, {value1})")
            print(f"   elements2[{p2}] = ({index2}, {value2})")
            
            self.visualize_pointers(elements1, elements2, p1, p2)
            
            if index1 == index2:
                print(f"\n   ✅ Indices MATCH! (index1={index1} == index2={index2})")
                product = value1 * value2
                print(f"   → Multiply: {value1} × {value2} = {product}")
                result += product
                print(f"   → Add to result: result = {result - product} + {product} = {result}")
                print(f"   → Move BOTH pointers: p1 = {p1 + 1}, p2 = {p2 + 1}")
                p1 += 1
                p2 += 1
            elif index1 < index2:
                print(f"\n   ⬅️  index1 < index2 ({index1} < {index2})")
                print(f"   → No match, skip index1")
                print(f"   → Move pointer 1: p1 = {p1 + 1}")
                p1 += 1
            else:
                print(f"\n   ➡️  index2 < index1 ({index2} < {index1})")
                print(f"   → No match, skip index2")
                print(f"   → Move pointer 2: p2 = {p2 + 1}")
                p2 += 1
        
        print(f"\n{'─'*60}")
        print(f"Loop complete!")
        print(f"   Final result: {result}")
        
        return result
    
    def visualize_pointers(self, elements1, elements2, p1, p2):
        """Visualize the current pointer positions"""
        print(f"\n   Pointer visualization:")
        
        # Show elements1 with pointer
        print(f"   Vector 1: ", end="")
        for i, (idx, val) in enumerate(elements1):
            if i == p1:
                print(f"[{idx}:{val}]←p1 ", end="")
            else:
                print(f"[{idx}:{val}] ", end="")
        print()
        
        # Show elements2 with pointer
        print(f"   Vector 2: ", end="")
        for i, (idx, val) in enumerate(elements2):
            if i == p2:
                print(f"[{idx}:{val}]←p2 ", end="")
            else:
                print(f"[{idx}:{val}] ", end="")
        print()


def main():
    print("╔" + "═" * 58 + "╗")
    print("║" + " SPARSE VECTOR DOT PRODUCT - DEMO ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    
    # Example 1: Basic example
    print("\n" + "█" * 60)
    print("█ EXAMPLE 1: Basic sparse vectors")
    print("█" * 60)
    nums1 = [1, 0, 0, 2, 3]
    nums2 = [0, 3, 0, 4, 0]
    
    vec1 = SparseVectorDemo(nums1)
    vec2 = SparseVectorDemo(nums2)
    
    result = vec1.dotProduct(vec2)
    
    print(f"\n🎯 Final Result: {result}")
    print(f"\n✅ Verification:")
    print(f"   Manual calculation:")
    print(f"   vec1 = {nums1}")
    print(f"   vec2 = {nums2}")
    print(f"   Dot product = 1×0 + 0×3 + 0×0 + 2×4 + 3×0")
    print(f"                = 0 + 0 + 0 + 8 + 0 = 8 ✓")
    
    # Example 2: No matching indices
    print("\n" + "█" * 60)
    print("█ EXAMPLE 2: No matching indices")
    print("█" * 60)
    nums3 = [1, 0, 0, 0, 0]
    nums4 = [0, 0, 0, 0, 5]
    
    vec3 = SparseVectorDemo(nums3)
    vec4 = SparseVectorDemo(nums4)
    
    result2 = vec3.dotProduct(vec4)
    
    print(f"\n🎯 Final Result: {result2}")
    print(f"   (No matching indices, so result is 0)")
    
    # Example 3: All matching indices
    print("\n" + "█" * 60)
    print("█ EXAMPLE 3: All matching indices")
    print("█" * 60)
    nums5 = [1, 0, 3, 0, 5]
    nums6 = [2, 0, 4, 0, 6]
    
    vec5 = SparseVectorDemo(nums5)
    vec6 = SparseVectorDemo(nums6)
    
    result3 = vec5.dotProduct(vec6)
    
    print(f"\n🎯 Final Result: {result3}")
    print(f"\n✅ Verification:")
    print(f"   Manual calculation:")
    print(f"   vec5 = {nums5}")
    print(f"   vec6 = {nums6}")
    print(f"   Dot product = 1×2 + 0×0 + 3×4 + 0×0 + 5×6")
    print(f"                = 2 + 0 + 12 + 0 + 30 = 44 ✓")
    
    # Example 4: One vector is all zeros
    print("\n" + "█" * 60)
    print("█ EXAMPLE 4: One vector is all zeros")
    print("█" * 60)
    nums7 = [1, 2, 3]
    nums8 = [0, 0, 0]
    
    vec7 = SparseVectorDemo(nums7)
    vec8 = SparseVectorDemo(nums8)
    
    result4 = vec7.dotProduct(vec8)
    
    print(f"\n🎯 Final Result: {result4}")
    print(f"   (One vector is all zeros, so result is 0)")
    
    # Example 5: Large sparse vectors
    print("\n" + "█" * 60)
    print("█ EXAMPLE 5: Large sparse vectors")
    print("█" * 60)
    nums9 = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0]
    nums10 = [0, 1, 0, 0, 2, 0, 0, 3, 0, 0]
    
    vec9 = SparseVectorDemo(nums9)
    vec10 = SparseVectorDemo(nums10)
    
    result5 = vec9.dotProduct(vec10)
    
    print(f"\n🎯 Final Result: {result5}")
    print(f"   (No matching indices: vec1 has indices [2,5,8], vec2 has indices [1,4,7])")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY OF ALL RESULTS")
    print("=" * 60)
    print(f"Example 1: [1,0,0,2,3] · [0,3,0,4,0] = {result} ✓")
    print(f"Example 2: [1,0,0,0,0] · [0,0,0,0,5] = {result2} ✓")
    print(f"Example 3: [1,0,3,0,5] · [2,0,4,0,6] = {result3} ✓")
    print(f"Example 4: [1,2,3] · [0,0,0] = {result4} ✓")
    print(f"Example 5: Large sparse vectors = {result5} ✓")


if __name__ == "__main__":
    main()
