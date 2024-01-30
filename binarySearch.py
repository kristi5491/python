def bianry_search(lists, item):
    low = 0
    high = len(lists) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lists[mid]
        if guess == item:
            return mid + 1
        if guess >item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,2,3,5,8,0,9]

print(bianry_search(my_list, 3))