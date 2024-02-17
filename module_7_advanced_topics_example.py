
# Binary Search Algorithm Example
def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

# Example usage of binary search
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(items, 4))  # Output: True
print(binary_search(items, -1))  # Output: False
