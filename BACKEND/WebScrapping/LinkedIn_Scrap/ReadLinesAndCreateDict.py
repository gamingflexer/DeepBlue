for i in range(12):
    with open(f"blocks/{i + 1}b.txt", "r") as file:
        first_line = file.readline()
        print(first_line)