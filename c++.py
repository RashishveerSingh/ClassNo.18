list1 = [1,2,4,5,6,7,8,9]
print(list1)

list2 = [1,2,4,5,6,7,8,9]
count = 0
for i in list2:
    count += i
print(count)

avg = count / len(list2)
print(avg)

list2.sort()
print(list2)