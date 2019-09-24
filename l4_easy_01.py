result = []
generated_list = [i for i in range(0, 10)]

for i in range(len(generated_list)):
    result.append(generated_list[i] * i)

print(result)