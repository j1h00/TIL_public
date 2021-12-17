def selection_sort(numbers, s):
    n = len(numbers)

    if s == n-1:
        return 

    minimum = s
    
    for i in range(s, n):
        if numbers[minimum] > numbers[i]:
            minimum = i

    numbers[s], numbers[minimum] = numbers[minimum], numbers[s]
    selection_sort(numbers, s+1)


A = [2, 4, 6, 1, 9, 8, 7, 0]
selection_sort(A, 0)

print(A)
