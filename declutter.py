import os
import shutil
from time import sleep
from calculations import get_age_in_days, get_size_in_gigabytes


def search_files_and_folders(min_size_gb, age_days, root_directory):


    #Raises an error if specified directory doesnt exist
    if not os.path.exists(root_directory):
        print("Invalid root directory")
        sleep(2)
        return

    
    print(f"\nSearching all files and folders in {root_directory}\n-------------------------------------")
    sleep(2)

    items_found = []

    # Iterate over all files and folders in the root directory
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
       
            try:
    
                file_age_days = get_age_in_days(file_path)
                file_size_gb = get_size_in_gigabytes(file_path)


                # Check if the file meets the size and age criteria
                if file_size_gb >= min_size_gb and file_age_days >= age_days:
                    # Display the file path, age, and size
                    print(f'\nFound file: {file_path} (age: {file_age_days} days, size: {file_size_gb} GB)')
                    items_found.append((file_path))
                    # [*items_found, (file_path)]

            except Exception as e:
                # Display a message if the file a file meets the age and size criteria and cannot be found or accessed
                if file_size_gb >= min_size_gb and file_age_days >= age_days:
                    print(f'\nFile {file_path} cannot be displayed for this reason: {e}')

        for dir in dirs:

            dir_path = os.path.join(root, dir)
            # print(file_path)

            try:
                # Get the directory size and age
                dir_size_bytes = 0
                for dirpath, dirnames, filenames in os.walk(dir_path):
                    for f in dirnames:
                        fp = os.path.join(dirpath, f)
                        dir_size_bytes += os.path.getsize(fp)

                
                # Convert the directory size and age criteria to gigabytes
                dir_age_days = get_age_in_days(dir_path)
                dir_size_gb = get_size_in_gigabytes(dir_path)
                

                # Check if the directory meets the size and age criteria
                if dir_size_gb >= min_size_gb and dir_age_days >= age_days:

                    # Display the directory path, age, and size
                    print(f'\nFound directory: {dir_path} (age: {dir_age_days} days, size: {dir_size_gb} GB)')
                    items_found.append((dir_path))

            except Exception as e:
                # Display a message if the directory cannot be found or accessed
                print(f'\nDirectory {dir_path} cannot be displayed for this reason: {e}')

    return items_found

def delete_files_and_folders(search_results):
    print(search_results)
    # Prompt the user to confirm the deletion
    if len(search_results) == 0:
        # raise Exception("\nNo directories/files found. Skipping file/folder deletion...")
        print("\nNo directories/files found. Skipping file/folder deletion...")
        sleep(2)
        return


    else:
        response = input("\nDo you want to delete the files and folders being displayed? (yes/no) ")

        if response.lower() == "yes" or response.lower() == "y":

            print(f"Deleting all files and folders...")
            sleep(1)

            # iterate through results and delete each file or folder
            for result in search_results:
                file_path = result
                try:
                    os.remove(file_path)
                    print(f"\n{file_path} has been deleted")
                except OSError:
                    try:
                        shutil.rmtree(file_path)
                        print(f"\n{file_path} has been deleted")
                    except OSError as e: 
                        print(f"{file_path} cannot be deleted because {e}\n")
        elif response.lower() == "no":
            print("Terminating script..")
            sleep(2)
        else:
            print("Invalid input. Terminating script...")
            sleep(2)


def main():

    age_criteria = int(input("Enter the minimum age requirement of the files/folders to be searched for in days (e.g. 30, 540):"))
    size_criteria = float(input("Enter the minimum size requirement of the files/folders to be searched for in GB (e.g. 3, 0.0001):"))
    directory_criteria = input("Enter the directory to be searched (e.g. '/', '/Documents'):")

    
    search_results = search_files_and_folders(size_criteria, age_criteria, directory_criteria)
    delete_files_and_folders(search_results)

    print("\nCompleted Actions.")


main()