def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target) # recursive call
            else:
                return recursive_binary_search(list[:midpoint], target) # recursive call

def verify(result):
    print("Target found: ", result)
