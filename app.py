import json

def Choices():

    print("manage employee system")
    print("add - add the new employee detail")
    print("update - update the employee detail")
    print("delete - delete the employee detail")
    print("exit  - exit from the process")

filename = "detail.json"


while True:

    Choices()
    Choice = input("\nSelect a option: ")
    if Choice == "add":

        emp_data = {"first_name": input("enter your first name : "),
                     "last_name": input("enter your last name : "),
                     "employe_id": int(input("enter the employee id : ")),
                     "city": input("enter the city : "),
                     "experience": int(input("enter the experience : ")),
                     "ctc": int(input("enter your ctc : ")),
                     "age": int(input("enter the age : ")),
                     "contact_no": int(input("enter the contact number : "))
                     }

        with open(filename, "r") as file:
            data = json.load(file)

        data.append(emp_data)

        with open(filename, "w") as file:
            json.dump(data, file,indent=4)

        print("new employee details added")

    elif Choice == "update":

        with open(filename, "r+") as file:
            data = json.load(file)
            print(data)

            Enter_emp_id = int(input("Enter the employee id to update: "))

            for index, emp in enumerate(data):

                if Enter_emp_id == emp['employe_id']:
                    data[index]["first_name"] = input("enter your first name : ")
                    data[index]["last_name"] = input("enter ypur last name : ")
                    data[index]["city"] = input("Enter city : ")
                    data[index]["experience"] = int(input("Enter experience :"))
                    data[index]["ctc"] = int(input("Enter CTC : "))
                    data[index]["age"] = int(input("Enter age : "))
                    data[index]["contact_no"] = int(input("Enter contact : "))

                    with open(filename, 'w') as data_file:
                        data = json.dump(data, data_file,indent=4)
                        print("employee detail updated")
                    break

            else:
                print("entered invalid employee id")


    elif Choice == "delete":

        with open(filename, "r+") as file:
            data = json.load(file)
            print(data)

        Enter_emp_id = int(input("Enter employee_id you want to delete: "))

        for index, emp in enumerate(data):

            if Enter_emp_id == emp["employe_id"]:
                asking = input("press yes to delete")

                if asking == "yes":
                    del data[index]

                    with open(filename, 'w') as data_file:
                        data = json.dump(data, data_file,indent=4)
                    break
        else:
            print("emp_id is not found.")

    elif Choice == "exit":
        print("invalid input")
        break


# emp_data = [{"first_name": input("enter your first name : "),
#              "last_name": input("enter your last name : "),
#              "employe_id": int(input("enter the employee id : ")),
#              "city": input("enter the city : "),
#              "experience": int(input("enter the experience : ")),
#              "ctc": int(input("enter your ctc : ")),
#              "age": int(input("enter the age : ")),
#              "contact_no": int(input("enter the contact number : "))
#              }]
#
# def write_json(emp_data,filename="detail.json"):
#
#     with open(filename, "w") as f:
#             json.dump(emp_data, f,indent=4)
#
# write_json(emp_data)