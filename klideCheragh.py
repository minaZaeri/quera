n = int(input())
list_number = [0 for i in range(n)]
count = 0
for i in range(n):
    list_number[i] = int(input())

for i in range(1, n):
    if list_number[i-1] == 0 and list_number[i] == 1:
        count += 1
    elif list_number[i-1] == 1 and list_number[i] == 0:
        count += 1

print(count)