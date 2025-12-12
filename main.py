import os 

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename} created successfully.")

    except FileExistsError:
        print(f"File Name {filename} already exists.")

    except Exception as e:
        print("An error occurred: ")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found in the current directory.")

        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File Name{filename} deleted successfully.")

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print("An error occurred: ")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"The content of the file {filename} is :\n {content}")

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print("An error occurred: ")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            new_content = input("Enter data to add")
            f.write(new_content + "\n")
            print(f"Content added to {filename} successfully")

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print("An error occurred: ")

def main():
    while True:
        print("File Management System")
        print('1. Create File')
        print('2. View All Files')
        print('3. Delete File')
        print('4. Read File')
        print('5. Edit File')
        print('6. Exit')

        choice = input("Enter Your Choice (1 - 6):  ")

        if choice == '1':
            filename = input("Enter the file name to create:")
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input("Enter the file name you want to delete: ")
            delete_file(filename)

        elif choice == '4':
            filename = input("Enter File name you want to read:")
            read_file(filename)

        elif choice == '5':
            filename = input("Enter the file name you want to edit: ")
            edit_file(filename)

        elif choice == '6':
            print("closing the app ....")
            break
        else:
            print("In-valid syntax")

if __name__ == "__main__":
    main()
