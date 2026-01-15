def write_numbers_into_file(filename):
    try:
        with open(filename, 'w') as f:
            for i in range(1, 101):
                f.write(f"{i}\n")
            print("Write successful")
    except PermissionError:
        print(f"Permission denite to write into the {filename}")
    except FileNotFoundError:
        print(f"Couldn't find the directory of {filename}")
    except Exception as e:
        print(f"an unknown error occured, {e}")
        