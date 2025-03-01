# Program to read Wimbledon champions data and display their information
# Time estimate: 45 minutes
# Actual time: 50 minutes

def read_wimbledon_data(filename):
    """
    Reads the Wimbledon champions data from a CSV file.
    Each line contains the champion's name and country.
    """
    champions = []

    # Read the file with UTF-8 encoding and BOM handling
    with open(filename, "r", encoding="utf-8-sig") as file:
        # Skip the header line
        next(file)

        # Process each line in the CSV file
        for line in file:
            parts = line.strip().split(",")  # Split each line by comma
            name = parts[0].strip()
            country = parts[1].strip()
            champions.append((name, country))

    return champions


def count_champions(champions):
    """
    Counts how many times each champion has won Wimbledon.
    Returns a dictionary where keys are champion names and values are their win count.
    """
    win_count = {}

    for name, _ in champions:
        if name in win_count:
            win_count[name] += 1
        else:
            win_count[name] = 1

    return win_count


def get_unique_countries(champions):
    """
    Extracts the unique countries from the champions' data and returns them in alphabetical order.
    """
    countries = set()

    for _, country in champions:
        countries.add(country)

    # Return countries sorted in alphabetical order
    return sorted(countries)


def display_results(win_count, countries):
    """
    Displays the champions and their win counts, as well as the list of countries.
    """
    print("Wimbledon Champions:")
    for name, count in win_count.items():
        print(f"{name} {count}")

    print("\nThese countries have won Wimbledon:")
    print(", ".join(countries))


def main():
    # Read and process the data
    filename = "wimbledon.csv"  # Assume the file is in the same directory
    champions = read_wimbledon_data(filename)

    # Count the number of wins for each champion
    win_count = count_champions(champions)

    # Get the unique countries in alphabetical order
    countries = get_unique_countries(champions)

    # Display the results
    display_results(win_count, countries)


if __name__ == "__main__":
    main()
