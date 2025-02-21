# subject_reader.py

# Function to load the data from the text file
def load_data(filename):
    with open(filename, 'r') as file:
        data = []
        for line in file:
            parts = line.strip().split(',')  # Split each line by commas
            # Convert the number of students to an integer
            parts[2] = int(parts[2])
            data.append(parts)
    return data

# Function to display the subject details in the desired format
def display_subject_details(subjects):
    for subject in subjects:
        subject_code, lecturer, num_students = subject
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students.")

# Main function to run the program
def main():
    filename = 'subject_data.txt'
    subjects = load_data(filename)  # Load data from the file
    display_subject_details(subjects)  # Display the details of each subject

# Call the main function to run the program
if __name__ == "__main__":
    main()
