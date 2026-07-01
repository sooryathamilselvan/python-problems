def main(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return main(s, left + 1, right - 1)

text = input("Enter a string: ")
result = main(text, 0, len(text) - 1)
print("Palindrome" if result else "Not a palindrome")