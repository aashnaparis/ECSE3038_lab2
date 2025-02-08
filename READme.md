# LAB 2
The essential functions in this codes is the post request and get request. Essentially, using classes that deifne the paremeters of a entry to the api as well as define the fields necessary for a success reponse were created as an architypes for this API.

## GET Request
Thus function is used to parse through each dictionary that we know will be in the list 
```Python data = []```  which is then added in a new list ```Python person_x=[] ``` where it displays all the dictionary in posted to the list.
```Python
...
person_x = []
for element in data:
    persons = element
    person_x.append(persons)
return {"Database" : person_x}
```

### POST Request
This function takes an object arguement with variable type "Person", which is the class created earlier. Thus the arguement has fields consistent with the Person class. Within the function a if loop is present to strip and check if the name, occupation and address has been posted correctly.
```Python
...
if (person_request.name.strip() == "" 
        or person_request.occupation.strip() == ""
        or person_request.address.strip() == ""):
            return {"success" : False, 
                   "result" : {"error_message" : "invalid request"}}
...
return {"success" : True,
            "result" : data_json}

```

The exercise was done under lab/assignment for ECSE3038

However, my favorite pokeman in Tsareena is my favorite pokeman cause she unapologetically kick @ss.

