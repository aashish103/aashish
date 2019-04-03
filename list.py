# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:51:56 2019

@author: aashish


"""


#implementing list and its function
list=["apple","microsoft","amazon","hcl"]
list2=["IBM","Twitter","SpaceX"]

if "microsoft" in list:
    print("Microsoft is present in list")
    
   
list.sort()
print(list)

list.append("facebook")
print(list)

list.remove("hcl")
print(list)

list.insert(1,"Intel")
print(list)

list.extend(list2)
print(list)

list.pop(3)
list=list.sort()
print(list)

#
#Microsoft is present in list
#['amazon', 'apple', 'hcl', 'microsoft']
#['amazon', 'apple', 'hcl', 'microsoft', 'facebook']
#['amazon', 'apple', 'microsoft', 'facebook']
#['amazon', 'Intel', 'apple', 'microsoft', 'facebook']
#['amazon', 'Intel', 'apple', 'microsoft', 'facebook', 'IBM', 'Twitter', 'SpaceX']
#['IBM', 'Intel', 'SpaceX', 'Twitter', 'amazon', 'apple', 'facebook']
#







#tuple
list2=("twitter","facebook","instagram","whatapp","facebook","facebook")
print(list2)

print(list2.count("facebook"))

#
#('twitter', 'facebook', 'instagram', 'whatapp', 'facebook', 'facebook')
#3





#set
set={2,4,6,8,10,11,6}
set2={9,11,13,16,89}

set.add(80)     
print(set)

set.remove(4)
print(set)

print(set.intersection(set2))

set.difference_update(set2)
print(set)

#{2, 4, 6, 8, 10, 11, 80}
#{2, 6, 8, 10, 11, 80}
#{11}
#{2, 6, 8, 10, 80}
