from pathlib import Path


BASE = Path(__file__).parent.parent.parent
STATE_FILE = BASE / "data" / "current_mail.txt"

def set_current_email():
    # Ask for user input
    number = input("Enter the email to be analyzed (from 0 - 180):")
    if not number.isdigit():
        print("Please enter a number.")
        exit()
    if int(number) < 0 or int(number) > 180:
        print("Please enter a number between 0 and 180.")
        exit()
    
    # ensure the folder exists
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)

    try: 
        with open(STATE_FILE, "w") as f:
            f.write(number)
            print(f"Chosen email: {number}")
    except:
        print("Error writing to file.")



def load_email():
    with open(STATE_FILE, "r") as f:
        number = f.read()
    # Load email
    email_path = BASE / "data" / "golden_dataset" / f"{number}.txt"
    email_text = email_path.read_text(encoding="utf-8")
    return email_text