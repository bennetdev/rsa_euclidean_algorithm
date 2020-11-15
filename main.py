from prettytable import PrettyTable


# recursive function for euclidean algorithm
def get_next_numbers(e, m, lst):
    if e % m == 0:
        return lst + [[e, m, e // m, e % m, 0, 1]]
    else:
        new_lst = get_next_numbers(m, e % m, [[e, m, e // m, e % m]])
        a, b = new_lst[1][-2], new_lst[1][-1]
        e_divided_m = new_lst[0][2]
        new_lst[0].extend([b, a-(e_divided_m * b)])
        return lst + new_lst


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

# reverse lst
lst = lst[::-1]
# initialize with 0 and 1
numbers = [[element[-2], element[-1]] for element in lst]
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
    table.add_row(i)
# print values and table
print(table)
print("Private: ", d)
print("Public: e:", e, ", n:", n)
