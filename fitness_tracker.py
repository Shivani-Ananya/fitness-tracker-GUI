import json
import os

if not os.path.exists("fitness_logs.json") or os.stat("fitness_logs.json").st_size == 0:
    with open("fitness_logs.json", "w") as file:
        json.dump([], file)

while True:
    print("\n==== Options =====")
    print("1. Add new fitness log")
    print("2. View all logs")
    print("3. Search log by date")
    print("4. Update a log")
    print("5. Delete a log")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        user_date = input("Enter date (YYYY-MM-DD): ").strip()
        user_steps = input("Enter your steps: ").strip()
        user_workout = input("Enter your workout: ").strip()
        user_calories = input("Enter your calories: ").strip()
        user_sleep = input("Enter your sleep: ").strip()
        user_notes = input("Enter your notes: ").strip()

        new_log = {
            "date": user_date,
            "steps": int(user_steps),
            "workout": user_workout,
            "calories": int(user_calories),
            "sleep": user_sleep,
            "notes": user_notes
        }

        with open("fitness_logs.json", "r") as file:
            logs = json.load(file)

        logs.append(new_log)

        with open("fitness_logs.json", "w") as file:
            json.dump(logs, file, indent=2)

        print("Log added successfully!")

    elif choice == "2":
        with open("fitness_logs.json", "r") as file:
            logs = json.load(file)

        if not logs:
            print("No logs found!")
        else:
            for log in logs:
                print("\n--- Log ---")
                print(f"Date      : {log['date']}")
                print(f"Steps     : {log['steps']}")
                print(f"Workout   : {log['workout']}")
                print(f"Calories  : {log['calories']}")
                print(f"Sleep     : {log['sleep']}")
                print(f"Notes     : {log['notes']}")

    elif choice == "3":
        search_date = input("Enter date to search (YYYY-MM-DD): ").strip()
        with open("fitness_logs.json", "r") as file:
            logs = json.load(file)

        found = False
        for log in logs:
            if log['date'] == search_date:
                print("\n--- Log ---")
                print(f"Date      : {log['date']}")
                print(f"Steps     : {log['steps']}")
                print(f"Workout   : {log['workout']}")
                print(f"Calories  : {log['calories']}")
                print(f"Sleep     : {log['sleep']}")
                print(f"Notes     : {log['notes']}")
                found = True

        if not found:
            print("No logs found on that date!")

    elif choice == "4":
        update_date = input("Enter date to search (YYYY-MM-DD): ").strip()
        with open("fitness_logs.json", "r") as file:
            logs = json.load(file)

        found = False

        for log in logs:
            if log['date'] == update_date:
                print("\n--- Current Log Details ---")
                print(f"Date      : {log['date']}")
                print(f"Steps     : {log['steps']}")
                print(f"Workout   : {log['workout']}")
                print(f"Calories  : {log['calories']}")
                print(f"Sleep     : {log['sleep']}")
                print(f"Notes     : {log['notes']}")

                new_steps = input("New Steps (press Enter to skip): ").strip()
                new_workout = input("New Workout (press Enter to skip): ").strip()
                new_calories = input("New Calories (press Enter to skip): ").strip()
                new_sleep = input("New Sleep (press Enter to skip): ").strip()
                new_notes = input("New Notes (press Enter to skip): ").strip()

                if new_steps.isdigit():
                    log["steps"] = int(new_steps)
                if new_workout:
                    log["workout"] = new_workout
                if new_calories.isdigit():
                    log["calories"] = int(new_calories)
                if new_sleep:
                    log["sleep"] = new_sleep
                if new_notes:
                    log["notes"] = new_notes

                found = True
                break

        if found:
            with open("fitness_logs.json", "w") as file:
                json.dump(logs, file, indent=2)
            print("Log updated successfully!")
        else:
            print("No log found for that date.")

    elif choice == "5":
        delete_date = input("Enter date to delete (YYYY-MM-DD): ").strip()

        try:
            with open("fitness_logs.json", "r") as file:
                logs = json.load(file)
        except FileNotFoundError:
            print("No logs file found.")
            logs = []

        found = False
        for i, log in enumerate(logs):
            if log['date'] == delete_date:
                print("\n--- Current Log Details ---")
                print(f"Date      : {log['date']}")
                print(f"Steps     : {log['steps']}")
                print(f"Workout   : {log['workout']}")
                print(f"Calories  : {log['calories']}")
                print(f"Sleep     : {log['sleep']}")
                print(f"Notes     : {log['notes']}")

                confirm = input("Are you sure you want to delete this log? (y/n): ").strip().lower()
                if confirm == 'y':
                    logs.pop(i)
                    with open("fitness_logs.json", "w") as file:
                        json.dump(logs, file, indent=2)
                    print("Your log has been deleted successfully!")
                else:
                    print("Deletion cancelled.")
                found = True
                break

        if not found:
            print("No log found on that day!")

    elif choice == "6":
        print("Thank you for using Fitness Tracker! See you next time!")
        break

    else:
        print("Invalid choice. Please try again.")
