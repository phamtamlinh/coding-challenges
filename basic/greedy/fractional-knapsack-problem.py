# Same as 0-1 Knapsack problem but now it's allowed to break the item

class Item:
  def __init__(self, wt, val):
    self.wt = wt
    self.val = val
    self.cost = val // wt
  def __lt__(self, other):
    return self.cost < other.cost

def fractionalKnapsack(valList, W):
  valList.sort(reverse=True)

  totalValue = 0

  for val in valList:
    curWt = int(val.wt)
    curVal = int(val.val)
    if W - curWt >= 0:
      W -= curWt
      totalValue += curVal
    else:
      fraction = W / curWt
      totalValue += curVal * fraction
      W = int(W - (curWt * fraction))
      break
  
  return totalValue

wtStr = "10 40 20 30"
valStr = "60 40 100 120"

wt = list(map(int, wtStr.split()))
val = list(map(int, valStr.split()))
W = 50

valList = []
for i in range(len(val)):
  valList.append(Item(wt[i], val[i]))

maxVal = fractionalKnapsack(valList, W)
print(maxVal)