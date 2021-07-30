list = []
n = int(input("Enter the list size:"))
for i in range(0, n):
    print("Enter number")
    a = int(input())
    list.append(a)
minimum=min(list)
maximum=max(list)
print("Minimum no. of the list is",minimum)
print("Maximum no. of the list is",maximum)