'''
Langham Hotel Management System
File name: assignment 2.py
Author: Nguyen Do Hoang Duong

Description: The program that creates a console-based Hotel Management Application System,
allowing users to add room, delete room, control room status, allocate room to customer, bill them,
and handle room file operations such as saving, showing, and backing up allocations.

Date: December 4, 2024
'''
# Import necessary modules
try:
    from datetime import datetime #managing date and time
    import os #Interacting with the operating system
except ImportError as e: #if there is ImportError, inform
    print(f"ImportError occurred: {e}")

# Global variables to store room list and allocations
room_list = {} # Dictionary to store available rooms with room details
allocations = {} # Dictionary to store allocated rooms and their customer details

# Define file names for the original and backup files
ori_file = "LHMS_800002966.txt" # Original file to store room allocations
# Backup file with timestamp
backup_file = "LHMS_800002966_backup_{}.txt".format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
      
# Add new room to the list
def add_room(room_list):
    """
    This function adds a new room to the room list after entering room details.
    """
    while True: #Use loop to ensure correct input for room number
        try:
            room_number = int(input("Enter room number: ")) # Get room number
            break  # If input is valid, break out of the loop
        except ValueError as e:  # If there's a ValueError, print an error message and prompt again
            print(f"ValueError occured: {e}")
        except TypeError as e: #If there is a TypeError, inform 
            print(f"TypeError occured: {e}")
        except NameError as e: #If there is a NameError, inform 
            print(f"NameError occured: {e}")
        except SyntaxError as e:#If there is a SyntaxError, inform
            print(f"SyntaxError occured: {e}")
        except Exception as e:  # Catch any other unexpected errors
            print(f"Unexpected error: {e}. Please re-enter.")

    try:
        room_type = input("Enter room type (Single/Couple/Family): ")
        # If room type is not in the valid options, prompt the user to re-enter
        while room_type not in ("Single", "Couple", "Family"):
            print("Incorrect form. Please re-enter.")
            room_type = input("Enter room type (Single/Couple/Family): ")
    except Exception as e:  # Catch any other unexpected errors
        print(f"Unexpected error: {e}. Please re-enter.")

    while True:  #Use loop to ensure correct input for room price
        try:
            room_price = float(input("Enter room price: ")) # Get room price
            break  # If input is valid, break out of the loop
        except ValueError as e:  # If there's a ValueError, print an error message and prompt again
            print(f"ValueError occured: {e}")
        except TypeError as e: #If there is a TypeError, inform 
            print(f"TypeError occured: {e}")
        except NameError as e: #If there is a NameError, inform 
            print(f"NameError occured: {e}")
        except SyntaxError as e:#If there is a SyntaxError, inform
            print(f"SyntaxError occured: {e}")
        except Exception as e:  # Catch any other unexpected errors
            print(f"Unexpected error: {e}. Please re-enter.")
            
     # Add the room to the list
    room_list[room_number] = {"type": room_type, "price": room_price}
    print(f"Room {room_number} is added to the list successfully.")

# Delete room from the list
def delete_room(room_list, allocations):
    """
    This function deletes a room from the room list if it is not allocated to a customer.
    If the room is allocated, it cannot be deleted.
    """
    while True: # Use loop to ensure correct input for room number
        try:
            room_number = int(input("Enter room number: ")) # Get room number
            break # If input is valid, break out of the loop
        except ValueError as e:  # If there's a ValueError, print an error message and prompt again
            print(f"ValueError occured: {e}")
        except TypeError as e: #If there is a TypeError, inform 
            print(f"TypeError occured: {e}")
        except NameError as e: #If there is a NameError, inform 
            print(f"NameError occured: {e}")
        except SyntaxError as e:#If there is a SyntaxError, inform
            print(f"SyntaxError occured: {e}")
        except Exception as e:  # Catch any other unexpected errors
            print(f"Unexpected error: {e}. Please re-enter.")

    # Check room status
    try:
        if room_number in room_list: #For room in room list
            del room_list[room_number]   # Delete the room from list
            print(f"Room {room_number} is deleted from the list successfully.")
        elif room_number in allocations: #For room have customer
            print(f"Room {room_number} is not available")
        else:
            print("Room not found") # Room doesn't exist
    except KeyError as e: #If there is KeyError, inform
        print(f"KeyError occurred: {e}")
    except IndexError as e: # If there is IndexError, inform 
        print(f"IndexError occurred: {e}")
    except Exception as e: #Catch any other unexpected errors
        print(f"Unexpected error: {e}")
        
# Display room features before booking it for a customer
def display_room(room_list):
    """
    This function displays the details of all rooms in room_list
    If no room, output is "No rooms now"
    """
    try:
        if len(room_list) == 0:  # If there are no rooms
            print("No rooms now")
            return
        else:
            for room_num, details in room_list.items(): # Loop through all rooms
                print(f"Room {room_num}: Type - {details['type']}, Price - {details['price']}")
    except TypeError as e: #If there is a Type Error, inform
        print(f"TypeError occurred: {e}")
    except KeyError as e: #If there is a KeyError, inform
        print(f"KeyError occurred: {e}")
    except IndexError as e: # If there is IndexError, inform 
        print(f"IndexError occurred: {e}")
    except Exception as e: # Catch any other unexpected errors
        print(f"Unexpected error: {e}. Please re-enter.")

# Book the room for the customer
def allocation_room(allocations, room_list):
    """
    This function allocates a room to a customer,
    with the customer name and real check-in time.
    """
    while True: # Use loop to ensure correct input for room number
        try:
            room_number = int(input("Enter room number: ")) # Get room number
            break  # If input is valid, break out of the loop
        except ValueError as e:  # If there's a ValueError, print an error message and prompt again
            print(f"ValueError occured: {e}")
        except TypeError as e: #If there is a TypeError, inform 
            print(f"TypeError occured: {e}")
        except NameError as e: #If there is a NameError, inform 
            print(f"NameError occured: {e}")
        except SyntaxError as e:#If there is a SyntaxError, inform
            print(f"SyntaxError occured: {e}")
        except Exception as e:  # Catch any other unexpected errors
            print(f"Unexpected error: {e}. Please re-enter.")
        
    # Check if room is available
    try:
        if room_number in room_list and room_number not in allocations:
            name = input("Enter customer's name: ") # Enter customer's name
            time_check_in = datetime.now() # Get the current time as check-in time
            print ("Start from " + time_check_in.strftime("%y-%m-%d %H:%M:%S"))
            allocations[room_number] = {"name": name, "time in": time_check_in} # Add to allocations
        else:
            print ("Room is not available")  # If room is already allocated or invalid, show error
    except TypeError as e: #If there is TypeError, inform
        print(f"TypeError occurred: {e}")
    except OverflowError as e: #If there is OverflowError, inform
        print(f"OverflowError occurred: {e}")
    except Exception as e: #Catch any other unexpected errors
        print(f"Unexpected error: {e}")

# Display Room Allocation status
def display_allocation(allocations):
    """
    This function displays the details of all allocated rooms 
    If no allocated rooms, output is "No rooms is allocated"
    """
    try:
        if len(allocations) == 0: # If no rooms are allocated
            print("No rooms is allocated")
        else:
            for room_num, details in allocations.items(): # Loop through allocated rooms
                time_check_in = details["time in"].strftime("%y-%m-%d %H:%M:%S")
                print(f"Room {room_num} is allocated to {details['name']} from {time_check_in}")
    except TypeError as e: #If there is a Type Error, inform
        print(f"TypeError occurred: {e}")
    except KeyError as e: #If there is a KeyError, inform
        print(f"KeyError occurred: {e}")
    except Exception as e: # Catch any other unexpected errors
        print(f"Unexpected error: {e}. Please re-enter.")
    except SyntaxError as e:#If there is a SyntaxError, inform
        print("SyntaxError occurred: {e}")
    except IndexError as e: # If there is IndexError, inform 
        print(f"IndexError occurred: {e}")
        
# Bill the customer and release the room for the next booking
def billing_and_deallocation(room_list, allocations):
    """
    This function calculates and displays the bill for a customer
    based on their allocated room stay duration

    Also resets all room allocations, removing all customer data
    """
    while True: # Use loop to ensure correct input for room number
        try:
            room_number = int(input("Enter room number: "))  # Get room number
            break  # If input is valid, break out of the loop
        except ValueError as e:  # If there's a ValueError, print an error message and prompt again
            print(f"ValueError occured: {e}")
        except TypeError as e: #If there is a TypeError, inform 
            print(f"TypeError occured: {e}")
        except NameError as e: #If there is a NameError, inform 
            print(f"NameError occured: {e}")
        except SyntaxError as e:#If there is a SyntaxError, inform
            print(f"SyntaxError occured: {e}")
        except Exception as e:  # Catch any other unexpected errors
            print(f"Unexpected error: {e}. Please re-enter.")

    try:        
        if room_number in allocations:  # Check if the room is allocated
            room_price = room_list[room_number]["price"] # Get the price of the room
            name = allocations[room_number]["name"] # Get the information of room number
            time_check_in = allocations[room_number]["time in"]
            time_check_out = datetime.now()  # Get the current time as check-out time

            # Calculate the duration of stay in minutes, hours, and days
            time = time_check_out - time_check_in
            duration_min = time.total_seconds()/60
            duration_hours = time.total_seconds()/3600
            duration_days = duration_hours /24
            hourly_price = room_price / 24 # Hourly rate based on room price per day
            
            if duration_min <= 0:  # Invalid duration
                print("Invalid stay duration")
                return
            elif duration_hours <1:  # Short stay, charge hourly
                total_price = 100 # 100$ for the first hour
            elif duration_hours <= 24:  # Less than a day stay
                total_price = 100 + (duration_hours - 1) * hourly_price #Add more price based on hour
            else:  # Stay longer than a day
                total_price = duration_days * room_price #Price based on day
                
            # Print the billing details
            print(f"Billing for customer {name} - room {room_number} from {time_check_in.strftime('%Y-%m-%d %H:%M:%S')} to {time_check_out.strftime('%Y-%m-%d %H:%M:%S')}.")
            print(f"Total price: {total_price}$")

            del allocations[room_number] # De-allocate the room
            print(f"{room_number} is now de-allocated")
        
        else: # If room is not allocated
            print("Room is not allocated")

    except ZeroDivisionError as e: #If there is ZeroDivisionError, inform
        print(f"ZeroDivisionError occurred: {e}")
    except TypeError as e: #If there is a TypeError, inform
        print(f"TypeError occurred: {e}")
    except OverflowError as e: #If there is OverflowError, inform
        print(f"OverflowError occurred: {e}")
    except SyntaxError as e:#If there is a SyntaxError, inform
        print("SyntaxError occurred: {e}")
    except IndexError as e: # If there is IndexError, inform 
        print(f"IndexError occurred: {e}")
    except Exception as e:  # Catch any other unexpected errors
        print(f"Unexpected error: {e}. Please re-enter.")

# Save Room Allocation to a file
def save_allocation_to_file():
    """
    This function saves room allocation details into a file (LHMS_800002966.txt).
    If no rooms are allocated, it writes 'No rooms allocated.' to the file.
    """
    try:
        # Open the original file in write mode ('w') to save room allocation details
        with open("LHMS_800002966.txt", 'w') as file:
            # Check if there are any room allocations
            if not allocations: 
                file.write("No rooms allocated.\n") # If no allocations, write a message
            else:
                # Iterate through all room allocations
                for room_number, details in allocations.items():
                    name = details["name"] # Get the name of the person allocated to the room
                    # Format the time of allocation
                    time_in = details["time in"].strftime("%Y-%m-%d %H:%M:%S")  # Time format
                    # Write the room allocation details to the file
                    file.write(f"Room {room_number}: {name} allocated from {time_in}\n")
        # Confirmation message after saving
        print("Room allocation saved to LHMS_800002966.txt.") 
    except IOError as e: #If there is a IOError, inform
        print(f"IOError occurred: {e}")

# Show Room Allocation from the file
def show_allocation_from_file():
    """
    This function reads and displays the room allocation details from the file (LHMS_800002966.txt).
    """
    try:
        # Check if the original file exists
        if os.path.exists(ori_file):  # Verify if the file exists
            with open(ori_file, 'r') as file: # Open the original file in read mode ('r')
                content = file.read()   # Read all the content from the file
                if content: # If there is content, print it
                    print(content)  # Display the content of the file
                else:
                    print("No data in file")  # If the file is empty, inform 
        else:
            print(f"{ori_file} does not exist.")  # If the file does not exist, inform
    except IOError as e: #If there is a IOError, inform
        print(f"IOError occurred: {e}")
    except FileNotFoundError: #If there is Fle Not Found Error, inform
        print(f"File {ori_file} not found.")
    except EOFError as e: #If there is EOF Error, inform 
        print(f"EOFError occurred: {e}")
    except Exception as e: #Catch any other unexpected errors
        print(f"Unexpected error: {e}")

# Backup and delete the file
def backup_and_clear_file():
    """
    This function backs up the room allocation file to a new file and clears the original file.
    The backup file is named with the current date and time. (LHMS_800002966_Backup_Date_Time.txt)
    """
    try:
        # Check if the original file exists
        if os.path.exists(ori_file):   # Verify if the original file exists
            with open(ori_file,'r') as original_file: # Open the original file in read mode ('r') file in read mode
                content = original_file.read() # Read the content of the original file

                # Create a backup file
                with open(backup_file, 'w') as backup:# Open the backup file in write mode
                    backup.write(content)  # Write the content of the original file to the backup file

                # Clear the content in the original file after creating the backup
                with open(ori_file, 'w') as file: # Open the original file in write mode ('w')
                    file.truncate(0)# This removes all the content from the file
                    
                # Confirmation message after backup and clearing
                print(f"Backup created as {backup_file} and the orginal file {ori_file} have been cleared.")
        else: 
            print(f"{roomfile} doesn't exist !!!")# If the original file doesn't exist, print an error message
    except IOError as e: #If there is a IOError, inform
        print(f"IOError occurred: {e}")
    except OverflowError as e: #If there is OverflowError, ìnorm
        print(f"OverflowError occurred: {e}")
    except Exception as e: #Catch any other unexpected errors
        print(f"Unexpected error: {e}")
        
#Show
def main():
    """
    This function runs the main menu of the hotel management system with options
    """
    while True: # Use loop to ensure correct input for choice
        print("*"*70)
        print(" "*15 + "Langham Hotel Management System")
        print(" "*30 + "Menu")
        print("*"*70)
        print("1. Add Room")
        print("2. Delete room")
        print("3. Display Rooms Details")
        print("4. Allocate Rooms")
        print("5. Display Rooms Allocation Details")
        print("6. Billing & De-Allocation")
        print("7. Save Room Allocation to File")
        print("8. Show Room Allocation from File")
        print("9. Backup and Clear Room Allocation File")
        print("0. Exit Application")
        print("*"*70)
        
        choice = input("Enter Your Choice Number Here: ") # Get choice number

        try:
            if choice == "1": # Add a new room
                add_room(room_list)
            elif choice == "2":  # Delete a room
                delete_room(room_list)
            elif choice == "3":  # Show room details
                display_room(room_list)
            elif choice == "4": # Allocate a room to a customer
                allocation_room(allocations, room_list)
            elif choice == "5": # Show room allocation details
                display_allocation(allocations)
            elif choice == "6":  # Bill and deallocate a room
                billing_and_deallocation(room_list, allocations)
            elif choice == "7":  # Save allocation to a file
                save_allocation_to_file()
            elif choice == "8":  # Display allocation from a file
                show_allocation_from_file()
            elif choice == "9":  # Backup and clear allocation file
                backup_and_clear_file()
            elif choice == "0":   # Exit the application
                print ("Exiting the application")
                break # If input is valid, break out of the loop
            else:
                print ("Invalid choice. Please try again") # Handle invalid menu choices
                
        except SyntaxError as e:#If there is a SyntaxError, inform
            print(f"SyntaxError occurred: {e}")
        except ValueError as e:  # If there's a ValueError, inform
            print(f"ValueError occurred: {e}")
        except ZeroDivisionError as e: #If there is ZeroDivisionError, inform
            print(f"ZeroDivisionError occurred: {e}")
        except IndexError as e: #If there is a IndexError, inform
            print(f"IndexError ooccurred: {e}")
        except NameError as e: #If there i a NameError, inform
            print(f"NameError occurred: {e}")
        except TypeError as e: #If there is a TypeError, inform
            print(f"TypeError occurred: {e}")
        except OverflowError as e: #If there is OverflowError, inform
            print(f"OverflowError occurred: {e}")
        except IOError as e: # If there is IOError, inform
            print(f"IOError occurred: {e}")
        except ImportError as e: #If there is ImportError, inform
            print(f"ImportError occurred: {e}")
        except EOFError as e: #If there is a EOFError, inform
            print(f"EOFError occurred: {e}")
        except FileNotFoundError as e: #If there is FileNotFoundError, inform
            print(f"FileNotFoundError occurred: {e}")
        except KeyError as e: #If there is a KeyError, inform
             print(f"KeyError occurred: {e}")
        except Exception as e:  # Catch any other unexpected errors
            print(f"Unexpected error: {e}. Please re-enter.")

# Run the main program   
if __name__ == "__main__":
    main()  
    

        
            
