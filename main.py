from prettytable import PrettyTable
p = int(input("p: "))
q = int(input("q: "))
n = p*q
e = int(input("e: "))
m = (p-1) * (q-1)

lst = []
mod = e % m
m_lst = m
e_lst = e
while mod != 0:
    mod = e_lst % m_lst
    lst.append([e_lst, m_lst, e_lst//m_lst, e_lst % m_lst])
    e_lst = m_lst
    m_lst = mod
numbers = []
lst = lst[::-1]
for i in range(0,len(lst)):
    if i == 0:
        nums = [0, 1]
    else:
        nums = [numbers[i-1][1], numbers[i-1][0] - (lst[i][2] * numbers[i-1][1])]
    numbers.append(nums)
if numbers[-1][0] <=0:
    d = numbers[-1][0] + ((p-1) * (q-1))
else:
    d = numbers[-1][0]

table = PrettyTable(["e","m","e//m","e%m","a","b"])
lst = lst[::-1]
numbers = numbers[::-1]
for index,i in enumerate(lst):
    table.add_row([i[0], i[1], i[2], i[3], numbers[index][0], numbers[index][1]])
print(table)
print("Private: ", d)
print("Public: ", e, ",", n)