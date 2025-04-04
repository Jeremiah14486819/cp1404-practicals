from guitar import Guitar

def read_guitars_from_file(filename):
    guitars = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def sort_guitars_by_year(guitars):
    return sorted(guitars)

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

if __name__ == "__main__":
    guitars = read_guitars_from_file("guitars.csv")
    sorted_guitars = sort_guitars_by_year(guitars)
    display_guitars(sorted_guitars)
