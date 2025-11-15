# Vehicle Service Booking System

# Available service slots
available_slots = ["10:00 AM", "11:00 AM", "01:00 PM", "03:00 PM"]

# Function to display services
def show_services():
    print("\nAvailable Service Types:")
    print("1. Basic Service")
    print("2. Full Service")
    print("3. Engine Repair")
    print("4. Oil Change")
    
    choice = int(input("Choose service (1-4): "))
    
    services = {
        1: "Basic Service",
        2: "Full Service",
        3: "Engine Repair",
        4: "Oil Change"
    }
    
    return services.get(choice, "Basic Service")


# Function to select slot
def select_slot():
    print("\nAvailable Slots:")
    for i, slot in enumerate(available_slots):
        print(f"{i+1}. {slot}")
    
    choice = int(input("Choose a slot: "))
    
    if 1 <= choice <= len(available_slots):
        return available_slots[choice - 1]
    else:
        print("Invalid choice!")
        return select_slot()


# Main Program
print("=== VEHICLE SERVICE BOOKING SYSTEM ===")

# User registration/login (simple)
name = input("Enter your name: ")
mobile = input("Enter mobile number: ")

vehicle_number = input("Enter Vehicle Number: ")
vehicle_model = input("Enter Vehicle Model: ")

service_type = show_services()
slot = select_slot()

print("\nBooking Confirmed!")
print("------------------------------")
print(f"Name           : {name}")
print(f"Mobile         : {mobile}")
print(f"Vehicle Number : {vehicle_number}")
print(f"Model          : {vehicle_model}")
print(f"Service Type   : {service_type}")
print(f"Time Slot      : {slot}")
print("------------------------------")
print("Thank you! You will receive a confirmation message soon.")
