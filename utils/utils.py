def read_file(filename="todo.txt"):
    with open(filename, "r") as file:
        todos = file.readlines()

    return todos


def write_file(content, filename="todo.txt"):
    with open(filename, "w") as file:
        file.writelines(content)
