data_list = [{'id': 1, 'name': 'sana'}, {'id': 2, 'name': 'reen'}, {'id': 3 ,'name': 'rose'}]
print(data_list)
subtitle = []

# add elements to a list from dictionary by name
for value in data_list:
    subtitle.append(value['name'])
print(subtitle)

#addedd elements are deleted from the list for value in datalist
for value in data_list:
    subtitle.remove(value['name'])
print(subtitle)

#deletion from particular id
for value in data_list:
    print("value :",value)
    if value["id"] == 3:
        data_list.remove(value)
print(data_list)

#updation by particular id
for value in data_list:
    if value["id"] == 2:
        value["name"] = "sanu"
print(data_list)