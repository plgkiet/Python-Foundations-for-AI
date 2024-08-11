class ItemValue:
    """Item Value DataClass"""
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val / wt  # Cost per weight unit

    def __lt__(self, other):
        return self.cost > other.cost  # For descending sort

class FractionalKnapSack:
    """Greedy Approach with Time Complexity O(n log n)"""
    @staticmethod
    def getMaxValue(wt, val, capacity):
        """Function to get maximum value in the knapsack"""
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))
        
        # Sort items by value-to-weight ratio in descending order
        iVal.sort(reverse=True)
        
        totalValue = 0
        for i in iVal:
            curWt = i.wt
            curVal = i.val
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
            else:
                fraction = capacity / curWt
                totalValue += curVal * fraction
                break
        
        return totalValue

# Driver Code
if __name__ == "__main__":
    wt = [10, 40, 20, 30]  # Weights
    val = [60, 40, 100, 120]  # Values
    capacity = 50  # Knapsack Capacity
    
    # Function call
    maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)
