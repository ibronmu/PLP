def main():
    print("Simple File Editor")
    print("==================")
    
    # Get input filename
    input_file = input("Enter the name of the file to read: ")
    
    try:
        # Try to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
        
        print(f"Successfully read '{input_file}'")
        
        # Simple modification: convert to uppercase
        modified_content = content.upper()
        
        # Create output filename
        output_file = input("Enter the name for the new file: ")
        
        # Write modified content
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Successfully created '{output_file}'")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()