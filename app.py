import json



emp_data = [{"first_name": input("enter your first name : "),
             "last_name": input("enter your last name : "),
             "employe_id": "A2022" ,
             "city": input("enter the city : "),
             "experience": int(input("enter the experience : ")),
             "ctc": int(input("enter your ctc : ")),
             "age": int(input("enter the age : ")),
             "contact_no": int(input("enter the contact number : "))
         }]
#
# def write_json(emp_data,filename="detail.json"):
#
#     with open(filename, "w") as f:
#             json.dump(emp_data, f)
#
# write_json(emp_data)




filename = "detail.json"

# read
with open(filename, "r") as file:
    data = json.load(file)

# update
data.append(emp_data)

# write
with open(filename, "w") as file:
    json.dump(data, file)
