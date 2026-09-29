a = list(map(int, input("Enter numbers: 1,2,3,4").split()))

n = len(a)

for i in range(n):
    for j in range(0, n - i - 1):

        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted array:", a)
