# for i in range(10):
#     print("The value of i is currently", i)
#
# for i in range(2, 8):
#     print("The value of i is currently", i)
#
# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2
#


# n = range(4)
#
# for num in n:
#     print(num - 1)
# else:
#     print(num)

#
# for i in range(0, 6, 3):
#     print(i)
#
# t = [[3 - i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)
#
# val = [1, 2, 3]
# num = val[-1:-2]
# print(val)
# print(num)
i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
        break
    print("*")

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e)

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

x = 1
x = x == x
print(x)

my_list = [i for i in range(-1, 2)]
print(my_list)

for i in range(-1, 1):
    print("#")


my_list = [3, 1, -1]
my_list[-1] = my_list[-2]
print(my_list)

#
# vals = [0, 1, 2]
# vals[0], vals[1] = vals[1], vals[2]
# print(vals)

nums = []
vals = nums
vals.append(1)
print(vals)
print(nums)

# my_list = [0 for i in range(1, 3)]
# print(my_list)

# my_list = [0, 1, 2, 3]
# x = 1
# for elem in my_list:
#     x *= elem
# print(x)
#
#
# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)


# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)

nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(vals)
print(nums)

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])


my_list = [1, 2, 3, 4]
print(my_list[-3:-2])


vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(vals)

i = 0
while i <= 3 :
    i += 2
    print("*")


# var = 1
# while var < 10:
#     print("#")
#     var = var << 1


for i in range(1):
    print("#")
else:
    print("#")
