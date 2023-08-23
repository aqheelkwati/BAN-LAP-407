def binary_search(arr, element):
    """
    Implementation of Binary Search Algorithm.
    Searches for an element in a sorted list and returns a tuple containing the element and its index.
    If the element is not found, returns None.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return (arr[mid], mid)
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14, 16]
element = 10
result = binary_search(arr, element)
if result:
    print(f"Element {result[0]} found at index {result[1]}.")
else:
    print(f"Element {element} not found in the list.")