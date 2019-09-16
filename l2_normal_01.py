first_list = [4,3,5,-7,3,-2,9,15,25,250,10,100]
result = []

for x in range(len(first_list)):
    if first_list[x] > 0 and ((first_list[x] ** 0.5) - int(first_list[x] ** 0.5 )) == 0:
        result.append(int(first_list[x]) ** 0.5)

print(result)