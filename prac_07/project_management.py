from project import Project
import pickle

def add_project(projects, name, priority, completion_percentage):
    project = Project(name, priority, completion_percentage)
    projects.append(project)

def save_projects_to_file(projects, filename):
    with open(filename, 'wb') as file:
        pickle.dump(projects, file)

def load_projects_from_file(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def display_projects(projects):
    for project in projects:
        print(project)

if __name__ == "__main__":
    projects = load_projects_from_file("projects.dat")

    while True:
        print("\nProject Management System")
        print("1. Add project")
        print("2. Display projects")
        print("3. Save and Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter project name: ")
            priority = int(input("Enter project priority (1-5): "))
            completion_percentage = int(input("Enter completion percentage: "))
            add_project(projects, name, priority, completion_percentage)
        elif choice == "2":
            display_projects(projects)
        elif choice == "3":
            save_projects_to_file(projects, "projects.dat")
            print("Projects saved.")
            break
        else:
            print("Invalid choice, try again.")
