
import os


class main:
    def __init__(self):
        self.lines = []
        directory = os.getcwd()
        print(f"Current Directory: {directory}")
        choice = input("change the directory? (y/n): ").lower()
        if choice == 'y':
            noedir = input("go to an existing directory or make a new one? (e/n): ").lower()
            if noedir == 'e':
                new_directory = input("Enter the new path: ")
                os.chdir(new_directory)
                pass
            elif noedir == 'n':
                new1_directory = input("Enter the new path to create: ")
                os.mkdir(new1_directory)
                os.chdir(new1_directory)
                pass
        elif choice == 'n' or choice == '':
            pass
        else:
            print("Invaid choice, try again\n")
            main.__init__(self)
    def start(self):
        print("--menu--")
        print("1. Create New File or Open Existing File")
        print("2. Delete File")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            self.new_file()
        elif choice == '2':
            self.delete_file()
        elif choice == '3':
            exit()
        else:
            print("Invaid choice, try again\n")
            main.start(self)
    
    def edit_add_save_exit(self, file_name, file):
        while True:
            command = input("Enter a command(add/edit/save/exit): ").lower().split(maxsplit=1)
            print(command)
            for i, line in enumerate(self.lines, start=1):
                print(f"{i}: {line.strip()}")
            if command[0] == 'add':
                new_line = str(input("add new line: ")) + '\n'
                self.lines.append(new_line)
            elif command[0] == 'edit':
                try:
                    line_num = int(command[1]) - 1
                    if 0 <= line_num < len(self.lines):
                        new_content = str(input(f"Enter new content for line {line_num + 1}: ")) + '\n'
                        self.lines[line_num] = new_content
                    elif line_num < 0 or line_num >= len(self.lines):
                        print("Invalid line number.")
                except (IndexError, ValueError):
                    print("Please provide a valid line number to edit.")
            elif command[0] == 'save':
                with open(file_name, 'w', encoding='utf-8') as save_file:
                    save_file.writelines(self.lines)
                print("File saved successfully.")
            elif command[0] == 'exit':
                print("exiting...")
                break
            else:
                print("Invalid command.")
            print(file.readlines())
    def new_file(self):
        file_name = input("Enter the name of the file you want to create or open: ")
        mode = input("Enter 'x' to make a new file or 'r+' to open an existing file: ")
        try:
            with open(file_name, mode, encoding='utf-8') as file:
                if mode == 'x':
                    main.edit_add_save_exit(self, file_name, file)
                elif mode == 'r+':
                    self.lines = file.readlines()
                    for i, line in enumerate(self.lines, start=1):
                        print(f"{i}: {line.strip()}")
                    main.edit_add_save_exit(self, file_name, file)
        except FileExistsError:
            print("File already exists, try again\n")
            main.start(self)
    def delete_file(self):
        name_of_file = str(input("Enter the name of the file you want to delete: "))
        try:
            os.remove(name_of_file)
            print("File deleted")
        except FileNotFoundError:
            print("File not found, try again\n")
            main.start(self)
if __name__ == "__main__":
    main().__init__()
    main().start()