#BAYAN
# n = int(input("Input N(1<=N<=1000): "))
# brands = []
#
# for _ in range(n):
#     brands.append(input("Input brands(length 1 to 30): "))
#
# # bayan_count = len(brands)-len(set(brands))
# # print(bayan_count)
#
#Ice Cream Parlor
# t = int(input("Input trips: "))
#
# money1 = int(input("Input money for first trip: "))
# size1 = int(input("Input first trip's cost length: "))
# cost1 = []
#
# for i in range(size1):
#     cost1.append(int(input("Input first trip's costs: ")))
#
# money2 = int(input("Input money for second trip: "))
# size2 = int(input("Input second trip's cost length: "))
# cost2 = []
#
# for i in range(size2):
#     cost2.append(int(input("Input second trip's costs: ")))
#
# for i in range(len(cost1) - 1):
#     for j in range(i+1, len(cost1)):
#         if cost1[i] + cost1[j] == money1:
#             print(i + 1, j + 1)
#
# for i in range(len(cost2) - 1):
#     for j in range(i+1, len(cost2)):
#         if cost2[i] + cost2[j] == money2:
#             print(i + 1, j + 1)


#String power

# string_1 = input("Input the string: ")
# k = int(input("Input K: "))
#
# if k >= 0:
#     print(string_1 * k)
# else:
#     if string_1.count(string_1[0]) < -k:
#         print("Undefined")
#     else:
#         num = int(len(string_1) / -k)
#         print(string_1[0:num])

#Two strings
#sxal lucum
# tests = int(input("Input number of tests: "))
# str1 = input("Input first string: ")
# str2 = input("Input second string: ")
# str3 = input("Input third string: ")
# str4 = input("Input fourth string: ")
# for i in str1:
#     if i in str2:
#         print("YES")
#     else:
#         print("NO")
#
# for i in str3:
#     if i in str4:
#         print("YES")
#     else:
#         print("NO")

#Jewels and Stones

# jewels = input("Input jewels, 1<= jewels.length, stones.length <= 50: ")
# stones = input("Input stones, 1<= jewels.length, stones.length <= 50: ")
#
# result = 0
#
# for i in stones:
#     result += jewels.count(i)
#
# print(result)