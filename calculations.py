import os
import time

GB = 1024 * 1024 * 1024
DAYS = 24 * 60 * 60

# Function to get the age of a file or folder in days
def get_age_in_days(file_or_folder_path):
  # Get the modification time of the file or folder in seconds
  mod_time = os.path.getmtime(file_or_folder_path)
  # Calculate the age in days by dividing the modification time by the number of seconds in a day
  age_in_days = (time.time() - mod_time) / DAYS
  return age_in_days

# Function to get the size of a file or folder in gigabytes
def get_size_in_gigabytes(file_or_folder_path):
  # Get the size of the file or folder in bytes
  size_in_bytes = os.path.getsize(file_or_folder_path)
  size_in_gigabytes = size_in_bytes / GB

  return size_in_gigabytes