
my_list = [8, 6, 4, 2, 0, 1, 3, 5, 7, 9]
#print(my_list)
n = len(my_list)

print(f"Original list: {my_list}")
print(f"Length of the given list: {n}")

for i in range(n):
    print(f"print value of i: {i}")
    for j in range(0, n-i-1):
        print(f"j limit left: {n-i-1}")
        if my_list[j] > my_list[j + 1]:
            print(f"print value of j: {j}")
            my_list[j], my_list[j+1] =my_list[j+1], my_list[j]
            print(f"iterative sorted list: {my_list}")
            print("="*40)


print(f"Final sorted list: {my_list}")

