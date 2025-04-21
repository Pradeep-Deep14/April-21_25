fruits = ['apple','banana','apple','cherry']


#count number of times string has appeared


def count_of_fruits(lst):
    dict={}
    for i in fruits:
        if i in dict:
           dict[i]+=1
        else:
            dict[i]=1
    return dict

print(count_of_fruits(fruits))


#count number of times string has appeared using set
def count_of_fruits(lst):
    dict={}
    for i in set(fruits):
        dict[i]=fruits.count(i)
    return dict 