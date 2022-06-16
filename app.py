# import json
import json
import simplejson

# creating a json file
while True:
    try:
        emp_data = [{"first_name": input("enter your first name : "),
                     "last_name": input("enter your last name : "),
                     "employe_id": "A2022:001",
                     "city": input("enter the city : "),
                     "experience": int(input("enter the experience : ")),
                     "ctc": int(input("enter your ctc : ")),
                     "age": int(input("enter the age : ")),
                     "contact_no": int(input("enter the contact number : "))
                     }]

        def write_json(emp_data,filename="detail.json"):

            with open(filename, "w") as f:
                    json.dump(emp_data, f,indent=4)

        write_json(emp_data)
        break

    except:
            print("check the input detail datatype and enter the correct datatype data")


# Choices function for user to select add,update,delete
def Choices():

    print("manage employee system")
    print("add - add the new employee detail")
    print("update - update the employee detail")
    print("delete - delete the employee detail")
    print("exit  - exit from the process")

# filename
filename = "detail.json"

while True:

    # open the json file and store the datas in data variable
    with open(filename, "r") as file:
        data = json.load(file)

    # to get the last employee id in a list
    listemp = [int(data[-1]['employe_id'][6:])]

    Choices()
    # user need to select the option
    Choice = input("\nSelect a option: ")
    # add a new data to json file
    if Choice == "add":

        # to create a new employee id for new user
        emp_id = listemp[-1] + 1
        listemp.append("A2022" + ":" +str(emp_id))
        try:
            # getting all the input data from the user for new employee to add in json file
            emp_data = {"first_name": input("enter your first name : "),
                         "last_name": input("enter your last name : "),
                         "employe_id": listemp[-1],
                         "city": input("enter the city : "),
                         "experience": int(input("enter the experience : ")),
                         "ctc": int(input("enter your ctc : ")),
                         "age": int(input("enter the age : ")),
                         "contact_no": int(input("enter the contact number : "))
                         }

            # open the file and read the data and store in data variable
            with open(filename, "r") as file:
                data = json.load(file)

            # append the new employee data to data variable
            data.append(emp_data)

            # data variable had some datas , write the data to json file
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

            print("new employee details added")

        except :
            print("check the input detail datatype and enter the correct datatype data")



    # update the data on existing employee
    elif Choice == "update":

        # open the file and read the data and store it in data variable
        with open(filename, "r+") as file:
            data = json.load(file)
            print(simplejson.dumps(data, indent=2))


            #  asking the user which employee id that user must update
            Enter_emp_id = input("Enter the employee id to update: ")

            # getting the data from file separately using index
            for index, emp in enumerate(data):

                # checking user given employee id is in the dataset already
                if Enter_emp_id == emp['employe_id']:

                    update = input("Enter what you want to update : ")

                    if update == "first_name":
                        data[index]["first_name"] = input("enter your first name : ")
                    elif update == "last_name":
                        data[index]["last_name"] = input("enter ypur last name : ")
                    elif update == "city":
                        data[index]["city"] = input("Enter city : ")
                    elif update == "experience":
                        data[index]["experience"] = int(input("Enter experience :"))
                    elif update == "ctc":
                        data[index]["ctc"] = int(input("Enter CTC : "))
                    elif update == "age":
                        data[index]["age"] = int(input("Enter age : "))
                    elif update == "contact_no":
                        data[index]["contact_no"] = int(input("Enter contact : "))

                    # open the file and write the updated data to file
                    with open(filename, 'w') as data_file:
                        data = json.dump(data, data_file,indent=4)
                        print("employee detail updated")
                    break

            # if the user gives not matching employee id
            else:
                print("entered invalid employee id")


    # delete the employee data in json file
    elif Choice == "delete":

        # open the file and read the data and store it in data variable
        with open(filename, "r+") as file:
            data = json.load(file)
            print(simplejson.dumps(data, indent=2))

        # asking the employee id which user need to delete
        Enter_emp_id = input("Enter employee_id you want to delete: ")

        # getting the data from file separately using index
        for index, emp in enumerate(data):

            # checking emp id is in the dataset
            if Enter_emp_id == emp["employe_id"]:
                asking = input("press yes to delete : ")

                if asking == "yes":
                    del data[index]

                    # open the file and write the data to json file
                    with open(filename, 'w') as data_file:
                        data = json.dump(data, data_file,indent=4)
                    break
        else:
            print("emp_id is not found.")

    elif Choice == "exit":
        break