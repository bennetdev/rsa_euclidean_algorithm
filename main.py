from prettytable import PrettyTable


# recursive function for euclidean algorithm
def get_next_numbers(e, m, lst):
    if e % m == 0:
        return lst + [[e, m, e // m, e % m]]
    else:
        return lst + get_next_numbers(m, e % m, [[e, m, e // m, e % m]])


# define rsa variables
p = int(input("p: "))
q = int(input("q: "))
n = p * q
e = int(input("e: "))
m = (p - 1) * (q - 1)

mod = e % m
# copy input variables to modify them
m_lst = m
e_lst = e
# get result of recursiv euclidean algorithm
lst = get_next_numbers(e_lst, m_lst, [])
# initialize with 0 and 1
numbers = [[0, 1]]
# reverse lst
lst = lst[::-1]
# calculate d
for i in range(1, len(lst)):
    # append numbers folowing the calculation
    nums = [numbers[i - 1][1], numbers[i - 1][0] - (lst[i][2] * numbers[i - 1][1])]
    numbers.append(nums)
# if d is incorrect (smaller than or equal to zero)
if numbers[-1][0] <= 0:
    d = numbers[-1][0] + ((p - 1) * (q - 1))
else:
    d = numbers[-1][0]
# convert numbers and steps to table
table = PrettyTable(["e", "m", "e//m", "e%m", "a", "b"])
lst = lst[::-1]
numbers = numbers[::-1]
for index, i in enumerate(lst):
    table.add_row([i[0], i[1], i[2], i[3], numbers[index][0], numbers[index][1]])
# print values and table
print(table)
print("Private: ", d)
print("Public: e:", e, ", n:", n)
