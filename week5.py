# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("My name is Stacy\n")
        file.write("37255867\n")
        file.write("i am 25 years old\n")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")
finally:
    print("File creation completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("Contents of my_file.txt:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read the file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("My name is Stacy\n")
        file.write("37255867\n")
        file.write("i am 25 years old\n")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
finally:
    print("File appending completed.")
