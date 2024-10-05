# Employee Management Project
class Employee:  
    def __init__(self, emp_id, name, position):  
        self.emp_id = emp_id  
        self.name = name  
        self.position = position  

    def __str__(self):  
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}"  

class EmployeeManagementSystem:  
    def __init__(self):  
        self.employees = {}  

    def add_employee(self, emp_id, name, position):  
        if emp_id in self.employees:  
            print(f"Employee ID {emp_id} already exists.")  
        else:  
            employee = Employee(emp_id, name, position)  
            self.employees[emp_id] = employee  
            print(f"Employee {name} added successfully.")  

    def display_employees(self):  
        if not self.employees:  
            print("No employees in the system.")  
            return  
        for emp in self.employees.values():  
            print(emp)  

    def update_employee(self, emp_id, name=None, position=None):  
        if emp_id in self.employees:  
            if name:  
                self.employees[emp_id].name = name  
            if position:  
                self.employees[emp_id].position = position  
            print(f"Employee ID {emp_id} updated successfully.")  
        else:  
            print(f"Employee ID {emp_id} not found.")  

    def remove_employee(self, emp_id):  
        if emp_id in self.employees:  
            del self.employees[emp_id]  
            print(f"Employee ID {emp_id} removed successfully.")  
        else:  
            print(f"Employee ID {emp_id} not found.")  

    def search_employee(self, emp_id):  
        if emp_id in self.employees:  
            print(self.employees[emp_id])  
        else:  
            print(f"Employee ID {emp_id} not found.")  

def main():  
    ems = EmployeeManagementSystem()  
    
    while True:  
        print("\nEmployee Management System")  
        print("1. Add Employee")  
        print("2. Display Employees")  
        print("3. Update Employee")  
        print("4. Remove Employee")  
        print("5. Search Employee")  
        print("6. Exit")  

        choice = input("Choose an option: ")  
        
        if choice == '1':  
            emp_id = input("Enter Employee ID: ")  
            name = input("Enter Employee Name: ")  
            position = input("Enter Employee Position: ")  
            ems.add_employee(emp_id, name, position)  
        
        elif choice == '2':  
            ems.display_employees()  
        
        elif choice == '3':  
            emp_id = input("Enter Employee ID to update: ")  
            name = input("Enter new name (leave blank to keep current): ")  
            position = input("Enter new position (leave blank to keep current): ")  
            ems.update_employee(emp_id, name if name else None, position if position else None)  
        
        elif choice == '4':  
            emp_id = input("Enter Employee ID to remove: ")  
            ems.remove_employee(emp_id)  
        
        elif choice == '5':  
            emp_id = input("Enter Employee ID to search: ")  
            ems.search_employee(emp_id)  
        
        elif choice == '6':  
            print("Exiting Employee Management System.")  
            break  
        
        else:  
            print("Invalid choice, please try again.")  

if __name__ == "__main__":  
    main()
