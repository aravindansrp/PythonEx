
src_list = [1, 1, 2, 3, 5, 8, 13, 12, 34, 55, 89]
result = []

ref_num = int(input("enter the ref num to find lesser no of it"))
for element in src_list:
    if element < ref_num:
        result.append(element)

print(result)

    
    
    
