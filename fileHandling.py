def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        raise  # Reraise the exception after notifying the user.
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
        raise  # Reraise the exception after notifying the user.
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        raise  # Reraise the exception for any other unexpected issues.

def modify_content(content):
    return content.upper()

def write_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
            print(f"Successfully wrote modified content to '{filename}'.")
    except IOError as e:
        print(f"Error: Unable to write to '{filename}'. Details: {e}")
        raise  # Reraise the exception after notifying the user.

def main():
    # Ask the user for the input filename with error handling.
    input_filename = input("Enter the filename to read: ")

    # Read the file; catch any errors while reading.
    try:
        original_content = read_file(input_filename)
    except Exception:
        # Exit the program if the file could not be read.
        return

    # Modify the file's contents.
    modified_content = modify_content(original_content)

    # Ask the user for the output filename.
    output_filename = input("Enter the filename to write the modified content: ")

    # Write the modified content to the new file.
    try:
        write_file(output_filename, modified_content)
    except Exception:
        # If writing fails, exit the program.
        return

if __name__ == "__main__":
    main()
