def is_palindrome(text):
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True
if __name__ == "__main__":
    name = "mom"
    print(is_palindrome(name))
    