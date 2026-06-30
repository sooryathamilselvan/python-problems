def reverse_array(arr, start, end):
    """Reverse arr in place using recursion."""
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start + 1, end - 1)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("Original:", data)
    reverse_array(data, 0, len(data) - 1)
    print("Reversed:", data)
