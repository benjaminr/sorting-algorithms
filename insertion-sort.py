def insertionSort(u):
    for i in range(len(u) - 1):
        j = i
        while j > 0 and u[j-1] > u[j]:
            u[j], u[j-1] = u[j-1], u[j]
            j -= 1
    return u
