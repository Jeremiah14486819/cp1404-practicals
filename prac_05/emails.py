# Program to store users' emails and names in a dictionary
# Time estimate: 25 minutes
# Actual time: 30 minutes

def extract_name_from_email(email):
    """
    Extracts a name from the email by splitting the email address at '@'
    and capitalizing the part before the '@'.
    """
    name_part = email.split('@')[0]  # Get the part before '@'
    name = name_part.replace('.', ' ').title()  # Replace dots with spaces and capitalize
    return name

def main():
    # Dictionary to store email as the key and name as the value
    email_to_name = {}

    while True:
        # Ask for the email
        email = input("Email: ").strip()

        # Break the loop if the email is blank
        if email == "":
            break

        # Extract the default name from the email
        name = extract_name_from_email(email)

        # Ask if the extracted name is correct
        is_name_correct = input(f"Is your name {name}? (Y/n): ").strip().lower()

        # If the name is incorrect, ask for the correct name
        if is_name_correct not in ["y", ""]:
            name = input("Name: ").strip()

        # Store the email and name in the dictionary
        email_to_name[email] = name

    # Print all stored emails and names
    print("\nStored emails and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
