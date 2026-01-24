class SolutionDemo:
    def mySqrt(self, x: int) -> int:
        print(f"\n{'='*60}")
        print(f"Finding integer square root of {x}")
        print(f"{'='*60}")
        
        # Edge cases
        if x == 0:
            print("Edge case: x == 0, return 0")
            return 0
        
        if x == 1:
            print("Edge case: x == 1, return 1")
            return 1
        
        left = 0
        right = x
        value = -1
        
        print(f"\nInitial: left={left}, right={right}, search space: [0, {x}]")
        print(f"Goal: Find largest integer n such that n² <= {x}")
        print(f"{'─'*60}")
        
        iteration = 0
        
        while left <= right:
            iteration += 1
            mid = (left + right) // 2
            mid_squared = mid * mid
            
            print(f"\n📍 Iteration {iteration}:")
            print(f"   left={left}, right={right}, mid={mid}")
            print(f"   mid² = {mid}² = {mid_squared}")
            print(f"   Compare: {mid_squared} vs {x}")
            
            self.visualize_search_space(left, right, mid, x)
            
            if mid_squared > x:
                print(f"\n   {mid_squared} > {x} → mid is TOO LARGE")
                print(f"   → Store mid={mid} as candidate (value = {mid})")
                print(f"   → Search LEFT: right = mid - 1 = {mid - 1}")
                value = mid
                right = mid - 1
            else:
                print(f"\n   {mid_squared} <= {x} → mid might be answer or too small")
                print(f"   → Search RIGHT: left = mid + 1 = {mid + 1}")
                left = mid + 1
        
        print(f"\n{'─'*60}")
        print(f"Binary search complete!")
        print(f"   Final candidate value = {value}")
        print(f"   Check: {value}² = {value * value}")
        
        if value * value > x:
            result = value - 1
            print(f"   {value}² = {value * value} > {x}")
            print(f"   → Return {value} - 1 = {result}")
            return result
        else:
            print(f"   {value}² = {value * value} <= {x}")
            print(f"   → Return {value}")
            return value
    
    def visualize_search_space(self, left: int, right: int, mid: int, x: int):
        """Visualize the current search space"""
        # Create a simple visualization
        if right - left <= 20:  # Only visualize if range is small enough
            print(f"\n   Search space visualization:")
            print(f"   ", end="")
            for i in range(left, right + 1):
                if i == left and i == mid and i == right:
                    print(f" LMR", end="")
                elif i == left and i == mid:
                    print(f" L,M", end="")
                elif i == mid and i == right:
                    print(f" M,R", end="")
                elif i == left and i == right:
                    print(f" L,R", end="")
                elif i == left:
                    print(f"  L", end="")
                elif i == mid:
                    print(f"  M", end="")
                elif i == right:
                    print(f"  R", end="")
                else:
                    print(f"  .", end="")
            print()
            print(f"   ", end="")
            for i in range(left, right + 1):
                print(f"{i:4}", end="")
            print()
        else:
            print(f"\n   Search space: [{left}, {right}], mid = {mid}")


def main():
    print("╔" + "═" * 58 + "╗")
    print("║" + " INTEGER SQUARE ROOT (BINARY SEARCH) - DEMO ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    
    sol = SolutionDemo()
    
    # Example 1: Perfect square
    print("\n" + "█" * 60)
    print("█ EXAMPLE 1: Perfect square (4)")
    print("█" * 60)
    result1 = sol.mySqrt(4)
    print(f"\n🎯 Final Result: sqrt(4) = {result1}")
    print(f"✅ Verification: {result1}² = {result1 * result1} = 4")
    
    # Example 2: Non-perfect square
    print("\n" + "█" * 60)
    print("█ EXAMPLE 2: Non-perfect square (8)")
    print("█" * 60)
    result2 = sol.mySqrt(8)
    print(f"\n🎯 Final Result: sqrt(8) = {result2}")
    print(f"✅ Verification: {result2}² = {result2 * result2} <= 8 < {(result2 + 1) ** 2}")
    
    # Example 3: Perfect square (16)
    print("\n" + "█" * 60)
    print("█ EXAMPLE 3: Perfect square (16)")
    print("█" * 60)
    result3 = sol.mySqrt(16)
    print(f"\n🎯 Final Result: sqrt(16) = {result3}")
    print(f"✅ Verification: {result3}² = {result3 * result3} = 16")
    
    # Example 4: Edge case - 0
    print("\n" + "█" * 60)
    print("█ EXAMPLE 4: Edge case (0)")
    print("█" * 60)
    result4 = sol.mySqrt(0)
    print(f"\n🎯 Final Result: sqrt(0) = {result4}")
    
    # Example 5: Edge case - 1
    print("\n" + "█" * 60)
    print("█ EXAMPLE 5: Edge case (1)")
    print("█" * 60)
    result5 = sol.mySqrt(1)
    print(f"\n🎯 Final Result: sqrt(1) = {result5}")
    
    # Example 6: Large number
    print("\n" + "█" * 60)
    print("█ EXAMPLE 6: Large number (100)")
    print("█" * 60)
    result6 = sol.mySqrt(100)
    print(f"\n🎯 Final Result: sqrt(100) = {result6}")
    print(f"✅ Verification: {result6}² = {result6 * result6} = 100")
    
    # Example 7: Non-perfect square (15)
    print("\n" + "█" * 60)
    print("█ EXAMPLE 7: Non-perfect square (15)")
    print("█" * 60)
    result7 = sol.mySqrt(15)
    print(f"\n🎯 Final Result: sqrt(15) = {result7}")
    print(f"✅ Verification: {result7}² = {result7 * result7} <= 15 < {(result7 + 1) ** 2}")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY OF ALL RESULTS")
    print("=" * 60)
    print(f"sqrt(0)  = {result4} ✓")
    print(f"sqrt(1)  = {result5} ✓")
    print(f"sqrt(4)  = {result1} ✓ (perfect square)")
    print(f"sqrt(8)  = {result2} ✓ (3²=9 > 8, so return 2)")
    print(f"sqrt(15) = {result7} ✓ (4²=16 > 15, so return 3)")
    print(f"sqrt(16) = {result3} ✓ (perfect square)")
    print(f"sqrt(100) = {result6} ✓ (perfect square)")


if __name__ == "__main__":
    main()
