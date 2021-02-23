# my_dctn = {'id': [12], 'name': ['sana'],'id': [13], 'name': ['fahmida']
# 'id': [14], 'name': ['rose']
# 'id': [15], 'name': ['richu']}
# print(my_dctn)

list_data = [
    {'names': 'sana', 'id': 15},
    {'names': 'sana', 'id': 15}
]
mydict = [{'names': 'sana', 'id': 15}, {'names': 'reen', 'id': 16}, {'names': 'rose', 'id': 17}]
new_data = []
for item in mydict:

    print("item ", item)
    if item["id"]==15:
        mydict.remove(item)
#     else:
#         new_data.append(item)
#
# mydict = new_data
# print(new_data)
print(mydict)


# if mydict["id"]==14:
#     mydict["names"]="yes"
# else:
#     mydict["names"] = "not"
# print(mydict)
#
#print(mydict['names'])
#print(mydict['id'])
print("mydict['names']: ", mydict['names'])