# recursion
def recursive(n):
    if n<2 and n>=0:
        return 1
    else:
        b=recursive(n-1)+recursive(n-2)
        return b

# 1 1 2 3 5 8 13 
print(recursive(6))
