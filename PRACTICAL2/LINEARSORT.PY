 alist(map(int, input("Enter numbers: ").split()))
tar = int(input("Enter target number: "))

for i in range(len(a)):
    if a[i] == tar:
        print("Found at index:", i)
        break
else:
    print("Target not found")
