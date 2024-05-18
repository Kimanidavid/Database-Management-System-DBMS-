import os
import subprocess

# Define the directory path
DIRECTORY_PATH = 'C:\\Users\\ADMIN\\Downloads\\Documents'

# Structure to represent a record in the database
class Record:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

# List to store records
records = []

# Function to add a new record to the database
def add_record(id, name, age, file_path):
    new_record = Record(id, name, age)
    records.append(new_record)
    add_record_to_file(id, name, age, file_path)
    print("Record added successfully.") 

# Function to add a new record to the specified file
def add_record_to_file(id, name, age, file_path):
    with open(file_path, 'a') as file:
        file.write(f'{id} {name} {age}\n')

# Function to display all records in the database
def display_records():
    print("ID\tName\tAge")
    for record in records:
        print(f"{record.id}\t{record.name}\t{record.age}")

# Function to read records from a file
def read_records_from_file(filename):
    records.clear()
    try:
        with open(filename, "r") as file:
            for line in file:
                id, name, age = line.split()
                records.append(Record(int(id), name, int(age)))
        print(f"Records loaded successfully from {filename}.")
    except FileNotFoundError:
        print(f"Error: Unable to open file {filename}.")

# Function to list all available data records in the directory
def list_data_records():
    print("Available data records:")
    files = [f for f in os.listdir(DIRECTORY_PATH) if f.endswith('.txt')]
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")
    return files

# Function to allow the user to continue with a preexisting data record
def continue_with_existing_record():
    files = list_data_records()
    if not files:
        print("No data records found.")
        return None

    choice = input("Enter the number of the data record you want to continue with: ")
    try:
        file_idx = int(choice) - 1
        if 0 <= file_idx < len(files):
            return files[file_idx]
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Invalid input.")
        return None

# Function to open the file directory using PowerShell
def open_file_directory(directory_path):
    subprocess.run(["powershell", "-Command", f"Start-Process '{directory_path}'"])

def main():
    if not os.path.exists(DIRECTORY_PATH):
        os.makedirs(DIRECTORY_PATH)

    print("Select an option:")
    print("1. Create a new data record")
    print("2. Continue with a preexisting data record")
    choice = input("Enter your choice: ")

    if choice == "1":
        filename = input("Enter the name for your new data record (without extension): ") + ".txt"
        file_path = os.path.join(DIRECTORY_PATH, filename)
        if os.path.exists(file_path):
            print("A file with this name already exists. Please choose a different name.")
            return
        print(f"New data record '{filename}' will be created.")
    elif choice == "2":
        filename = continue_with_existing_record()
        if filename:
            file_path = os.path.join(DIRECTORY_PATH, filename)
            read_records_from_file(file_path)
        else:
            return
    else:
        print("Invalid choice.")
        return

    while True:
        print("Select an option:")
        print("1. Enter new data")
        print("2. Edit entered data")
        print("3. Display all records")
        print("4. Open file directory")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            add_record(id, name, age, file_path)
        elif choice == "2":
            print("Opening file directory...")
            open_file_directory(DIRECTORY_PATH)
        elif choice == "3":
            display_records()
        elif choice == "4":
            print("Opening file directory...")
            open_file_directory(DIRECTORY_PATH)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
