from cli import read_file, write_file


def test_read_file(resources_path):
    file_path = resources_path / "todo.txt"
    todos = read_file(file_path)

    assert len(todos) == 3
    assert todos == ["Test read file\n", "Test write file\n", "End"]


def test_write_file(resources_path):
    file_path = resources_path / "empty-todo.txt"

    content = ["Go to work\n", "Go to school"]
    write_file(content, file_path)

    with open(file_path, "r") as file:
        content = file.readlines()

    assert len(content) == 2
    assert content[0] == "Go to work\n"
    assert content[1] == "Go to school"
