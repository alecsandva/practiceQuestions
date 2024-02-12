
# x = 1
# print(x,"yo1")
# #
# # x = 2
# print(x,"yo2")
# x += 2
# print(x,"yo3")
# x = 1
# while True:
# #     x += 1 and x < 10
# #     print(x,"yo5")
# #
# #     if x == 10:
# #         break
# #
# #
# # #
# # while x < 10:
# #     print(x)
# #     x+=1
# #
# #

x = 0

array = []

total_sum = 0

while True:
    x += 1
    if (x%3== 0) or (x%5 ==0):
        total_sum += x
  #      print(x)
  #      print(total_sum)

    if x >= 999:
         break


print("the total sum of numbers divisible by 3 or 5 under 1000 is " ,total_sum)