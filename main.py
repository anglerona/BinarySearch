# Binary Search using recursion by Angelina Wu

import matplotlib.pyplot as plt
import math
import random

def bin(arr,target,left,right,count):
  if left > right:
    return -1 # not found
  mid = (right + left) // 2
  if target == arr[mid]:
    count += 1 # keeps track of steps
    return count
  elif target < arr[mid]:
    # Restrict to the left side of current index
    count += 1
    return bin(arr,target,left,mid-1,count)
  else: 
    count += 1
    return bin(arr,target,mid+1,right,count)
   
x_vals = [] # list size
y_vals = [] # steps
N = 10000

for n in range(1,N):
  arr = list(range(1,n+1))
  # Generate random number
  tar = random.randint(1,n+1)
  x_vals.append(n)
  y_vals.append(bin(arr,tar,0,n-1,0))

x_linear = [i for i in range(1,N)]
y_linear = [x for x in x_linear] # linear time
y_log = [math.log10(x) for x in x_linear] # log(n) time


fig = plt.figure()

# Comparing data to linear time
fig.add_subplot(2,1,1)
plt.xlabel('List Size')
plt.ylabel('Steps')
plt.title("Plot searches vs O(n)")
plt.plot(x_vals,y_vals,'*',color='orange',label="Plot Searches")
plt.plot(x_linear,y_linear,'ch',label="O(n)")
plt.legend()

fig.tight_layout(pad=3.0)

# Comparing data to log(n) time
fig.add_subplot(2,1,2)
plt.xlabel('List Size')
plt.ylabel('Steps')
plt.title("Plot Searches vs O(Log(n))")
plt.plot(x_vals,y_vals,'*',color='orange',label="Plot Searches")
plt.plot(x_linear,y_log,'mh',label="O(Log(n))")
plt.legend()

fig.savefig('plot.png')