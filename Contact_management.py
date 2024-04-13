import re

def add_new_contact(file):
  contact_name = input("Enter the Name of the Employee: ").title()
  for id, values in file.items():
    if contact_name in values["Employee Name"]:
      print("Employee is already in This Department")
      break
  else:
    e_id = input("Enter Employee ID Number: ")
    phone = input("Enter Employee Phone Number [1-999-999-999]: ")
    email = input("Enter Employee email: ")
    address = input("Enter in Employee Address: ").title()
    note = input("Enter notes: ").capitalize()
    validation = validating_contact(contact_name,e_id,phone,email)
    if validation:
      file[e_id]= {"Employee Name":contact_name,"Phone Number":phone,"Email":email,"Address":address,"Notes":note}
      print("New contact was created")
    
def validating_contact(*contact): 
  name_match = re.match(r"\w{2,20}\s\w{2,20}",contact[0])
  if name_match:
    id_match =re.match(r"(\w{4})",contact[1])
    if id_match:
      phone_match = re.match(r"(\w{1}-\w{3}-\w{3}-\w{4})",contact[2])
      if phone_match:
        email_match = re.match(r"([-Za-z0-9._%-]+\@{1}\w+\.{1}\w{2,3})",contact[3])
        if email_match:
          return True
  else:
    print("Contact couldn't be validated")
    return False

def edit_contact(file):
  e_id = input("Enter Employee ID: ")
  if e_id not in file:
    print("Employee isn't in This Department")
  else:
    contact_name = input("Enter the Name of the Employee: ").title()
    phone = input("Enter new Employee Phone Number [1-999-999-999]: ")
    email = input("Enter new Employee email: ")
    address = input("Enter new in Employee Address: ").title()
    note = input("Enter In new note: ")
    validation = validating_contact(contact_name,e_id,phone,email)
    if validation:
      file[e_id]= {"Employee Name":contact_name,"Phone Number":phone,"Email":email,"Address":address,"Notes":note}
      print(f"{contact_name}'s contact was updated")

def delete_contact(file,all):
  contact = input("Enter Employee Number: ").title()
  if contact in file:
      file.pop(contact)
      print("Contact Deleted")
  else:
    print("Employee isn't Found In this Department")    

def search_contact():
  file = all_files_content()
  contact_id = input("Enter Employee ID Number: ")
  for directory in file.items():
    for department, group in directory[1].items():
      for people in group:
        if contact_id in people:
          print(f"\n{department}:\nEmployee Number: {contact_id}")
          for type_info, info in group[contact_id].items():
            print(f"{type_info}: {info}")
        
def display_contacts(file,all):
  while True:
    print("\nView Menu:\n1. View by Selected Department\n2. View Company\n3. Quit\n")
    user_input = input("Choose Menu Option: ")
    if user_input == "1":
      file = picking_file()
      looping_contacts(file[0])
    elif user_input == "2":
      looping_all_contacts(all)
    elif user_input == "3":
      print("Returning to Main Menu")
      break
    else:
      print("Invalid Input")

def export_contacts(file_name,changes):
  with open(file_name, "w" ) as file:
    for person, info in changes.items():
      file.writelines(f"{person}/{info['Employee Name']}/{info['Phone Number']}/{info['Email']}/{info['Address']}/{info['Notes']}")
    file.write(f"")
    print("\nFile has been updated")
       
def import_contacts(file_info):
  try:
    with open(f"Contact_management_system\\{file_info}","r") as file:
      extraction = file.readlines()
      contents = {}
      print(extraction)
      for line in extraction:
        getting_info = line.strip("''[]").split('/')
        contents[getting_info[0]] = {"Employee Name":getting_info[1],"Phone Number":getting_info[2],"Email":getting_info[3],"Address":getting_info[4],"Notes":getting_info[5]}
      return contents
  except FileNotFoundError:
        print(f"We do not have records for that Department")

def all_files_content():
  try:
    with open(f"Contact_management_system\\Accounting.txt","r") as file1, open(f"Contact_management_system\\Finance.txt","r") as file2, open(f"Contact_management_system\\Management.txt","r") as file3:
      extraction1 = file1.readlines()
      extraction2 = file2.readlines()
      extraction3 = file3.readlines()
      contents1 = {}
      contents2 = {}
      contents3 = {}
      all_content = {}
      for line1 in extraction1:
        getting_info1 = line1.split('/')
        contents1[getting_info1[0]] = {"Employee Name":getting_info1[1],"Phone Number":getting_info1[2],"Email":getting_info1[3],"Address":getting_info1[4],"Notes":getting_info1[5]}
      
      for line2 in extraction2:
        getting_info2 = line2.split('/')
        contents2[getting_info2[0]] = {"Employee Name":getting_info2[1],"Phone Number":getting_info2[2],"Email":getting_info2[3],"Address":getting_info2[4],"Notes":getting_info2[5]}
      
      for line3 in extraction3:
        getting_info3 = line3.split('/')
        contents3[getting_info3[0]] = {"Employee Name":getting_info3[1],"Phone Number":getting_info3[2],"Email":getting_info3[3],"Address":getting_info3[4],"Notes":getting_info3[5]}
      
      all_content["Company Directory"] = {"Accounting":contents1, "Finance":contents2, "Management":contents3} 
      return all_content
  except FileNotFoundError:
    print(f"We do not have records for that Department")

def picking_file():
  print("Departments:\n1. Accounting\n2. Finance\n3. Management\n4. New Hire")
  path = input("Enter the department: ")
  if path == "1":
    contacts = import_contacts("Accounting.txt")
    file = "Accounting.txt"
  elif path == "2":
    contacts = import_contacts("Finance.txt")
    file = "Finance.txt"
  elif path =="3":
    contacts = import_contacts("Management.txt")
    file = "Management.txt"
  elif path == "4":
    contacts = import_contacts("New_hires.txt")
    file = "New_hires.txt"
  return contacts, file

def looping_contacts(file_info):
  for employee in file_info.items():
    print(f"\nEmployee Number: {employee[0]}")
    for key, info in employee[1].items():
      print(f"{key}: {info}")
      
def looping_all_contacts(file_info):
  for company, department in file_info.items():
        print(f"\n{company}:")
        for grouping,people in department.items():
          print(f"\n{grouping}:")
          looping_contacts(people)
     
def main_menu():
  try:
     print("Welcome to the Contact Management System")
     file = picking_file()
     while True:
      print("Main Menu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit")
      main_menu_choice = input("Select one of out menu options: ")
      if main_menu_choice == "1":
        add_new_contact(file[0])
      elif main_menu_choice == "2":
        edit_contact(file[0])
      elif main_menu_choice == "3":
        delete_contact(file[0],all_files_content())
      elif main_menu_choice == "4":
        search_contact()
      elif main_menu_choice == "5":
        display_contacts(file[0],all_files_content())
      elif main_menu_choice == "6":
        export_contacts(f"Contact_management_system\\{file[1]}",file[0])
      elif main_menu_choice == "7":
        file = picking_file()
      elif main_menu_choice == "8":
        print("Thank you for using our Contact Management System")
        break
      else:
        print("Invalid choice")
  except IndexError as e:
    print(f"Error Main Menu: {e}")
    
main_menu()
