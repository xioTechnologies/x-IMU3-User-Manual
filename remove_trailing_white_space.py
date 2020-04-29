import os

for root, _, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
    for source_file in files:
        _, file_extension = os.path.splitext(source_file)

        if file_extension != ".tex" and file_extension != ".sty":
            continue

        file_path = os.path.join(root, source_file)

        with open(file_path) as source_file:
            lines = source_file.readlines()

        with open(file_path, "w") as source_file:
            for line in lines:
                source_file.write(line.rstrip() + "\n")
