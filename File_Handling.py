import os

def list_directory_contents(path):
    """
    List and print all files and subdirectories in the given path.

    Args:path (str): The directory path to inspect.

    Returns:
    None
    """
    try:
        # Check if the path exists and is a directory
        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist.")
            return
        if not os.path.isdir(path):
            print(f"Error: The path '{path}' is not a directory.")
            return

        # List and print all files and subdirectories
        print(f"Contents of the directory '{path}':")
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"DIR : {item}")
            else:
                print(f"FILE: {item}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    # Prompt the user for the directory path
    directory_path = input("Enter the directory path to inspect: ").strip()
    list_directory_contents(directory_path)