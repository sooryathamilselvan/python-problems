def greet():
    count=0
    if count == 4:
        return
    print("Soorya")
    count+=1
    greet()
if __name__ == "__main__":
    greet()