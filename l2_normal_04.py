first_list = [1,2,3,4,5,4,3,2,1,11]
second_list = []
print(list(set(first_list)))

for i in first_list:
    if first_list.count(i) == 1:
        second_list.append(i)


print(second_list)