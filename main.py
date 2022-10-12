matrix = eval(input("Enter your matrix numbers: "))
result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(result)