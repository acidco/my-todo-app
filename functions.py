FILEPATH = "act.txt"


def get_act(file_path=FILEPATH):
    """Read a text file and return the list of
    to-do items"""
    with open(file_path, "r") as file_local:
        actions_local = file_local.readlines()
    return actions_local


def write_act(actions_arg, file_path=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(file_path, "w") as file_local:
        file_local.writelines(actions_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_act())
