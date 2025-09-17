# Calculate the subset by backtracking

def Calcsubset(A, res, subset, index):
    res.append(subset[:])

    for i in range(index, len(A)):
        subset.append(A[i])

        Calcsubset(A , res, subset, i + 1)

        subset.pop()

def subset(A):
    subset = []
    res = []
    index = 0
    
    Calcsubset(A, res, subset, index)
    return res

if __name__ == "__main__":
    arr = [1, 7, 9]
    res = subset(arr)
    print("Total Subset: ",len(res))
    print("Subset of the given array is:",res)

    for s in res:
        print(*s)
