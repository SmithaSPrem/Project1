
 
def printNos(n):
    if n > 0:
        printNos(n - 1)
        print(n)
 
# Driver code
printNos(100)
