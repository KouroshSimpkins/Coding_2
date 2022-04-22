"""find the closest value in binary to an integer"""


import sys
 
def highestPowerof2( n):
 
    # Invalid input
    if (n < 1):
        return 0
  
    res = 1
  
    #Try all powers starting from 2^1
    for i in range(8*sys.getsizeof(n)):
     
        curr = 1 << i
  
        # If current power is more than n, break
        if (curr > n):
             break
  
        res = curr
  
    return res
  
# Driver code
if __name__ == "__main__":
 
    n = 10
    print(highestPowerof2(n))


def testFunction(denary):
    """find the closest single binary value to the denary input"""
    denary = int(denary)