import os

paths = []

for root, _, file_names in os.walk(os.path.dirname(os.path.realpath(__file__))):
    for file_name in file_names:
        _, extension = os.path.splitext(file_name)

        if extension in (".tex", ".sty"):
            paths.append(os.path.join(root, file_name))

for path in paths:
    with open(path) as file:
        lines = file.readlines()

    with open(path, "w") as file:
        for line in lines:
            file.write(line.rstrip() + "\n")
