# my_list = [2,3,4,'hello',3.14, ['a','b']]

# # print(my_list[0])

# for x in my_list:
#     print(x)

# x = 'hello'
# list2 = list(x)
# print(list2)

# list1 = [1,2,3,4,5]

# list2 = [x**2 for x in list1]
# print(list2)

# my_list = [2,3,4,'hello',3.14, ['a','b']]
# my_list[0] = 200
# print(my_list)

# l = [1,2,3,4,5,6]
# print(min(l))

# if 4>2:
#     print('bu togri')
# else:
#     print('bu notogri')

# sample_list = ['abc', 'xyz', 'aba', '1221']

# cnt = 0
# for char in sample_list:
#     if char[0]==char[-1]:
#         cnt = cnt + 1


# print(cnt)

# sample_list = ['abc', 'xyz', 'aba', '1221']

# cnt = 0
# for char in sample_list:
#     if char[0]==char[-1]:
#         cnt = cnt + 1
# print(cnt)

# list = [x for x in range(10,1000,10)]
# print(list)

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190,
#          200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 350, 360,
#            370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530,
#              540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700,
#                710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870,
#                  880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]

# cnt = 0
# for x in list:
#    if x % 10 !=0:
#         cnt = cnt + 1
# print(cnt)

# for i in range(0,len(list)):
#     if list[i-1] + 10 != list[i] and i>0:
#         print(list[i], list[i-1])


# for x in 'hello':
#     print(x)

# numbers = [1,2,3,4,5]
# sq_numbers = []
# for numbers in numbers:
#     sq_numbers.append(numbers**2)
# print(sq_numbers)

# for numbers in numbers:
#     print(numbers)
#     if numbers==4:
#         print('4 soni topildi')
#         break

# for numbers in numbers:
#     # print(numbers)
#     if numbers==4:
#         print('4 soni topildi')
#         continue
#     print(numbers)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# for numbers in numbers:
#     print(f'numbers = {numbers}')
#     if numbers%2!=0:
#         continue
#     print(f'{numbers} is even')

# list1 = ['Hello','Python','Dev']
# list2 = []

# for x in list1:
#     for y in x:
#         list2.append(y)
# print(list2)

# for i in range(5):
#     print(i)

# numbers=[1,2,2,2,2,2,2,3,4,4,5]
# print(set (numbers))

# set1={1,'hi',3.14}
# print(set1)

# x='temurbek'
# print(set (x))

# set1={x**2 for x in  range(10)}
# print(set1)

# set1={1,2,3,4,5}
# set2={3,4,5,6,7}

# # print(set1.union(set2))
# # print(set1 | set2)

# # print(set1.intersection(set2))
# # print(set1 & set2)

# print(set1.difference(set2))
# print(set1-set2)
# print(set1.symmetric_difference(set2))
set1={"nok", "banan", "olma", "nok"}
set2={"uzum", "olma", "tarvuz", "nok"}
# print(set(mevalar))

# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
print(set1 - set2)
# bun narsa & listlarning bir birida yo'q narsalarini chiqaradi

a='mening'
b='ismim'
c='temur'
print(a, b, c)


