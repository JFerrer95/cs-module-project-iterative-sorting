# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j 
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0,len(arr) - 1): 
        for j in range(0, len(arr) - 1 - i): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr

    if maximum == -1:
        maximum = max(arr)           
    
    buckets = [0 for _ in range(maximum + 1)]
    for x in arr:
        if x < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[x] +=1        
    j = 0
    for i in range(len(buckets)):            
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1
    return arr

