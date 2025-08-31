import json
import os

DATA_FILE = "employees.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_employee():
    employees = load_data()
    emp_id = input("Enter Employee ID: ")

    if any(emp["id"] == emp_id for emp in employees):
        print("Employee ID already exists")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employees.append({
        "id": emp_id,
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    })

    save_data(employees)
    print("Employee added successfully")

def display_employees():
    employees = load_data()
    if not employees:
        print("No employee records found!")
        return

    print("\n--- Employee Records ---")
    for emp in employees:
        print(f"ID: {emp['id']} | Name: {emp['name']} | Age: {emp['age']} | Dept: {emp['department']} | Salary: {emp['salary']}")

def search_employee():
    employees = load_data()
    emp_id = input("Enter Employee ID to search: ")

    for emp in employees:
        if emp["id"] == emp_id:
            print(f" Found Employee: {emp}")
            return

    print("Employee not found!")

def update_employee():
    employees = load_data()
    emp_id = input("Enter Employee ID to update: ")

    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = input(f"Enter new Name ({emp['name']}): ") or emp["name"]
            emp["age"] = input(f"Enter new Age ({emp['age']}): ") or emp["age"]
            emp["department"] = input(f"Enter new Department ({emp['department']}): ") or emp["department"]
            emp["salary"] = input(f"Enter new Salary ({emp['salary']}): ") or emp["salary"]

            save_data(employees)
            print("Employee updated successfully!")
            return

    print("Employee not found!")

def delete_employee():
    employees = load_data()
    emp_id = input("Enter Employee ID to delete: ")

    new_employees = [emp for emp in employees if emp["id"] != emp_id]

    if len(new_employees) == len(employees):
        print("Employee not found!")
    else:
        save_data(new_employees)
        print("Employee deleted successfully!")

def average_salary():
    employees = load_data()
    if not employees:
        print("No employee records found!")
        return

    total_salary = sum(float(emp["salary"]) for emp in employees)
    avg_salary = total_salary / len(employees)
    print(f"Average Salary: {avg_salary}")

def median_salary():
    employees = load_data()
    if not employees:
        print("No employee records found!")
        return

    salaries = sorted(float(emp["salary"]) for emp in employees)
    mid = len(salaries) // 2
    med_salary = (salaries[mid] + salaries[mid - 1]) / 2 if len(salaries) % 2 == 0 else salaries[mid]
    print(f"Median Salary: {med_salary}")

def menu():
    while True:
        print("\n====== Employee Management System ======")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Calculate Average Salary")
        print("7. Calculate Median Salary")
        print("8. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            average_salary()
        elif choice == "7":
            median_salary()
        elif choice == "8":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    menu()
