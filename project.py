import re
import pickle
class User:
    users=[]
    filename = "users.pkl"
    
    
    
    def __init__(self,first_name,last_name,email,password, phone):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.phone=phone

    @staticmethod
    def validate_phone(phone):
           phone = phone.strip()  
           return re.match(r'^01[0125]{1}[0-9]{8}$', phone) is not None

    @classmethod
    def register(cls):
        first_name =input("Enter First Name: ")
        last_name =input("Enter Last Name: ")
        email =input("Enter Email: ")
        password =input("Enter Password: ")
        confirm_password = input("Confirm Password: ")
        phone = input("Enter Mobile Number: ")



        if password != confirm_password:
            print("Passwords do not match!")
            return None

        if not cls.validate_phone(phone):
            print("Invalid Egyptian phone number!")
            return None
 
   
        new_user = cls(first_name, last_name, email, password, phone)
        cls.users.append(new_user)
        cls.save()
        print("Registration successful!")
        return new_user
  
   
    @classmethod
    def view_all_users(cls):
     print("Users list:", cls.users) 
     for user in cls.users:
      print(f"Name: {user.first_name} {user.last_name}, Email: {user.email}, Phone: {user.phone}")


    @classmethod
    def save(cls):
        with open(cls.filename, 'wb') as f:
            pickle.dump(cls.users, f)
            print("data saved")

    @classmethod
    def load(cls):
        try:
            with open(cls.filename, 'rb') as f:
                cls.users = pickle.load(f)
                print("user saved")
                return cls.users
        except FileNotFoundError:
            cls.users = []
            print("no file exists")


    @classmethod
    def login(cls):
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        for user in cls.users:
            if user.email == email and user.password == password:
                print("Login successful!")
                return user

        print("Invalid email or password!")
        return None


 
from datetime import datetime
class Project:
    projects=[]
    pfilename ="project.pkl"

    def __init__(self,owner, title, details, target, start_date, end_date):
        self.owner = owner
        self.title = title
        self.details = details
        self.target = target
        self.start_date = start_date
        self.end_date = end_date
    
    @staticmethod
    def validate_date(date_text):
        try:
            return datetime.strptime(date_text, "%Y-%m-%d")
        except ValueError:
            return None

    @classmethod
    def create_project(cls,user):
        title=input("enter project title :") 
        details=input("enter project details :") 
        target=input("enter project target :") 
        start_date= input("enter project start_date :") 
        end_date=input("enter project end_date :") 

        start_date1 = cls.validate_date(start_date)
        end_date1 = cls.validate_date(end_date) 

        if not start_date1 or not end_date1:
            print("Invalid date format!")
            return None
        if start_date1 >= end_date1:
            print("Start date must be before end date!")
            return None




        new_project = cls(user, title, details, target, start_date, end_date)
        cls.projects.append(new_project)
        cls.save()
        print("Project created successfully!")
        return new_project
 
    @classmethod
    def view_projects(cls):
        if not cls.projects:
            print("No projects available.")
            return

        print(" All Projects:")
        for project in cls.projects:
            print(f"Title: {project.title},Target: {project.target}, Duration: {project.start_date} - {project.end_date}")


    @classmethod
    def save(cls):
        with open(cls.pfilename, 'wb') as f:
            pickle.dump(cls.projects, f)
            print("Projects saved successfully!")

    @classmethod
    def load(cls):
        try:
            with open(cls.pfilename, 'rb') as f:
                cls.projects = pickle.load(f)
                print("Projects loaded successfully!")
        except FileNotFoundError:
            cls.projects = []
            print("No projects file found.")

       

    @classmethod
    def delete_project(cls):
        if not cls.projects:
            print("no projects available.")
            return
        cls.view_projects()

        try:
            project_index = int(input("enter the project number to delete:")) - 1
        except ValueError:
            print("Invalid input!")
            return

        if 0 <= project_index < len(cls.projects):
            del cls.projects[project_index]
            cls.save()  
            print("Project deleted successfully!")
        else:
            print("Invalid input!")




class System:
 @staticmethod
 def run():
        print("start")
        User.load()
        Project.load()
        while True:
            print("\n1. Register\n2. Login\n3. Exit")
            choose = input("Choose an option: ")

            if choose == "1":
                user = User.register()
            elif choose == "2":
                user = User.login()
            elif choose == "3":
                print("Exit")
                break
            else:
                print("Invalid choice")
            
            while user:
                print("\n1. Create Project\n2. View Projects\n3. Delete Project\n4. Logout")
                choice = input("Choose an option: ")

                if choice == "1":
                    Project.create_project(user)
                elif choice == "2":
                    Project.view_projects()
                elif choice == "3":
                    Project.delete_project()
                elif choice == "4":
                    print("Logout")
                    user = None
                else:
                    print("Invalid choice")

        
def main():
  System.run()
if __name__ == "__main__":
    main()

