#produce a partition function, and then apply the logic to make up all possibilities to get to £2.00 using pound sterling coins

goal = 7

x = 1
array = []
counter = 0
while sum(array) < goal:
    array.append(1)




a = -2
big_array = []
array2 = []
big_array2 = []
count2 = 0
while True:
    count2 += 1






    #print(array[a:])
   # print(array)
    var1 = sum(array[a:])
    var2 = (array[0:a])
    var2.append(var1)
  #  print(array)
   # print(var2)





    var3 = var2[::-1]
    var4 = var2



    if (len(str(var4)) == 1) and (len(str(big_array[-1][-1]))) == 1:
        break

    big_array.append(var2[::-1])
    print(big_array)
    print(var2[::-1])
    print(big_array[-1])

    print(str(var4[0]), 'var4')
    print(str(big_array[-1][-1]), 'big array')

    



    if big_array[-1][-1] < sum(array):



        a -= 1
    else:
        array = big_array[counter]
        counter += 1
       # print(big_array[0])
        a = -2





print(big_array)

#array2 = big_array[0]

# a = -2
# while True:
#     print(array2)
#
#     var3 = sum(array2[a:])
#     var4 = array2[0:a]
#     print(var3)
#     print(var4)
#     var4.append(var3)
#     print(var4)
#     big_array.append(var4)
#     print(big_array)

#     if big_array[-1][-1] < sum(array):
#
#         a -= 1
#     else:
#         # print(big_array[0])
#         break
#
#
#
# print(big_array)
# print(big_array[-1])
#
# big_array.pop(-1)
#
# print(big_array)



print(len(big_array))







#start with 1+1+1 until you reach your number
#break this down until it's n-1 + 1
#then, use factors to build up to the number