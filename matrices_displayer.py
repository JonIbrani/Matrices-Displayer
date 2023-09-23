print('This program creates two matrices A and B')

rows_A = int(input('Enter the number of rows you want for matrix A:\n'))
columns_A = int(input('Enter the number of columns you want for matrix A:\n'))

main_list_A = []

for i in range(rows_A):
    row_A = []
    for j in range(columns_A):
        user_input = int(input(f'Enter element at position ({i+1},{j+1}) for matrix A: '))
        row_A.append(user_input)
    main_list_A.append(row_A)

rows_B = int(input('Enter the number of rows you want for matrix B:\n'))
columns_B = int(input('Enter the number of columns you want for matrix B:\n'))

main_list_B = []

for i in range(rows_B):
    row_B = []
    for j in range(columns_B):
        user_input = int(input(f'Enter element at position ({i+1},{j+1}) for matrix B: '))
        row_B.append(user_input)
    main_list_B.append(row_B)

print('Matrix A:')
for row in main_list_A:
    print(row)

print('Matrix B:')
for row in main_list_B:
    print(row)






