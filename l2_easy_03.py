new_list = [1,2,3,4]
result = []


for x in range (len(new_list)):
    if new_list[x] % 2 == 0:
        result.append(new_list[x] / 4)
    else:
        result.append(new_list[x] * 2)


print(result)