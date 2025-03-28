from car import Car

def main():
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"{my_car.name} has {my_car.fuel} fuel remaining.")

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"{limo.name} has {limo.fuel} fuel after refueling.")
    distance_driven = limo.drive(115)
    print(f"{limo.name} drove {distance_driven} km and has {limo.fuel} fuel remaining.")

if __name__ == "__main__":
    main()
