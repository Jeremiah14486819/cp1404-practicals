import csv
from programming_language import ProgrammingLanguage

def read_languages(filename):
    """Read programming languages from a CSV file and return a list of ProgrammingLanguage objects."""
    language_list = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            name, typing, reflection, year = row
            language_list.append(ProgrammingLanguage(name, typing, reflection == "Yes", int(year)))
    return language_list

if __name__ == "__main__":
    programming_languages = read_languages("languages.csv")
    for language in programming_languages:
        print(language)
