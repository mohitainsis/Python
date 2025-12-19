# freq = [1,2,3,2,1,5,5,6,6,7]
# freq_dict = {}
# for i in freq:
#     if i in freq_dict:
#         freq_dict[i] = freq_dict[i] + 1
#     else:
#         freq_dict[i] = 1
# for i in freq:
#     if freq_dict[i] == 1:
#         print("first unique number is : ",i)
#         break

#Question 2----------------------

lis = [1,1,2,2,2,3,3,3,3,5,5,5,5,5,7,8]
count = {}
for i in lis:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
for i in lis:
    if count[i] == 1:
        print(i)
print(count)
