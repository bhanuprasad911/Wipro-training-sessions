from file_package.file_writer import write_numbers_into_file

def read_file(filename):
    write_numbers_into_file(filename)
    try:
        with open(filename, 'r') as file:
            content = file.readlines()
            clean_content = [line.strip() for line in content]
            print(clean_content)
    except PermissionError:
        print(f"permission denied to read {filename}")
    except FileNotFoundError:
        print(f"could not find {filename} to read")
if __name__ == "__main__":
    read_file("data.txt")