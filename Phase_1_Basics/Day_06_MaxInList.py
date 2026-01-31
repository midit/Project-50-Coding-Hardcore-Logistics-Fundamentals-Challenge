def max_in_list(arr):

    if len(arr) == 0:
        return 0
    
    current_max = arr[0]

    for val in arr[1:]:
        if val > current_max:
            current_max = val
    
    return current_max
            

if __name__ == "__main__":
    print(max_in_list([3, 7, 2, 9, 5]))
    print(max_in_list([-1, -5, -2]))
    print(max_in_list([10]))
    print(max_in_list([]))