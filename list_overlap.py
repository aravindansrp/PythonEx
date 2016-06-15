list1 = [3,4,9,8,10,3]
list2 = [3,10,9,4,12,15,16]
overlap_list = [] #result list

#finding smallest list length
len1=len(list1)
len2=len(list2)

if(len1<len2):
    ref_list=list1
    compare_list=list2
else:
    ref_list=list2
    compare_list=list1

for element in ref_list:
    if(element in compare_list):
        overlap_list.append(element)

print(overlap_list)

        
    


