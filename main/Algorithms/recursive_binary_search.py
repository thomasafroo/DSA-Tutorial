def recursive_binary_search(list, target):
    if len(list) == 0: # base case
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target: # base case
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target) # recursive call w/ slice operation
            else:
                return recursive_binary_search(list[:midpoint], target) # recursive call

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
