import json

# Load data from file
try:
    with open("study.json", "r") as file:
        data = json.load(file)
except:
    data = {}

while True:
    print("\n--- Study Tracker ---")
    print("1. Add Study Hours")
    print("2. View Data")
    print("3. Reset Data")
    print("4. Exit")

    choice = input("Choose option: ")

    # ADD
    if choice == "1":
        subject = input("Subject: ")
        hours = int(input("Hours: "))

        if subject in data:
            data[subject] += hours
        else:
            data[subject] = hours

        with open("study.json", "w") as file:
            json.dump(data, file)

        print("Updated!")

    # VIEW
    elif choice == "2":
        print("\n--- Your Data ---")

        if not data:
            print("No data yet.")
        else:
            for subject, hours in data.items():
                print(f"{subject}: {hours}")

    # RESET
    elif choice == "3":
        data = {}

        with open("study.json", "w") as file:
            json.dump(data, file)

        print("Data reset!")

    # EXIT
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")