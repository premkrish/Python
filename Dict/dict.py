""" This script contains lessons for dictionary """

#Create a dict
dictMsg = {"user_id": 137, "user_name":"premkrish", "created_date":'123120170301TZ'}
print(dictMsg)

#Add elements to dict
dict1 = dict(user_id=137, user_name="premkrish")
print(dict1)

dict1["email_id"] = "pk@mailinator.com"
print(dict1)

#print all element in dict
for key in dictMsg.keys():
    val = dictMsg[key]  
    print(f"{key} = {val}")

for key,val in dict1.items():
    print(key + " = " + str(val))

# Get values from dictionary
print(dict1.get("email_id"))

#clear all elements of dictionary
dict1.clear()
print(dict1)