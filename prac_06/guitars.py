from guitar import Guitar

def main():
    """Program to store and display guitars."""
    guitars = []

    print("My guitars!")
    while True:
        name = input("Enter guitar name (or press Enter to finish): ")
        if not name:
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")

if __name__ == "__main__":
    main()
