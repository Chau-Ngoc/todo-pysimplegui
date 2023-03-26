from utils import read_file, write_file

if __name__ == "__main__":
    while True:
        user_action = input("Add, show, edit, complete or exit? ")
        user_action = user_action.lower().strip()

        if user_action.startswith("add"):
            todo = user_action[4:].capitalize()

            with open("todo.txt", "a") as file:
                file.write(todo + "\n")

        elif user_action.startswith("show"):
            print("----- SHOWING ALL TODOS -----")

            todos = read_file()

            for index, todo in enumerate(map(str.strip, todos)):
                print(f"{index + 1}. {todo}")

        elif user_action.startswith("edit"):
            todos = read_file()

            try:
                todo_index = int(user_action[5:])
            except ValueError:
                print("You have to enter the index number of the todo items")
                continue

            try:
                existing_todo = todos[todo_index - 1]
                print(f"This is the selected todo: {existing_todo}")
            except IndexError:
                print("The number you enter is not a valid index")

            todo = input("Enter new todo: ")
            todos[todo_index - 1] = f"{todo.capitalize()}\n"

            write_file(todos)

        elif user_action.startswith("complete"):
            todo_index = int(user_action[9:])

            todos = read_file()

            try:
                completed_todo = todos.pop(todo_index - 1).strip()
                print(f"'{completed_todo}' is fulfilled and therefore deleted")
            except IndexError:
                print("The number you enter is not a valid index")

            write_file(todos)

        elif user_action.startswith("exit"):
            break

        else:
            print("That is not a valid command!")

    print("Bye")
