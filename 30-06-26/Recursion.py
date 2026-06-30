def greet(count=0):
    if count == 4:
        return
    print("Soorya")
    greet(count + 1)
if __name__ == "__main__":
    greet()