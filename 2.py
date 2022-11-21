def returnCount(str1,str2):
    targetletter=str2[-1]
    count=0
    for i in str1:
        if targetletter==i:
            count=count+1
    return count


str1='going to go to goa'

str2='go'


print(returnCount(str1,str2))