def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
        return

    modified_content = content.upper()

    new_filename = "modified_" + filename

    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified file has been successfully written to '{new_filename}'.")
    except IOError as e:
        print(f"Error: Unable to write to file '{new_filename}'. {e}")

if __name__ == "__main__":
    main()