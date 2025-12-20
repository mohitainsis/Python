#---couting which number comes how many times nd putting it in dict

n = [1,2,1,3,3,1,1,2,2]
dict = {}
for i in n:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
print(dict)


num = [1,1,2,2,3,3,3]
count = {}
for i in num:
    if i in count:#if i means the number in variable num is in count nd i is key here automatically
        count[i]=count[i]+1#count[i]---means key in count 1 or 2 ....if this key i or num i already in count then add 1 in the value 
    else:
        count[i]=1
print(count)
#-----------in dictionaries i automatically looks for keys and not
#for values its a set rule in python nd also cuz dictionaries are
#made to fast lookup using keys
