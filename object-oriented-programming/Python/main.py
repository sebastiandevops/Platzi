from car import Car

if __name__ == "__main__":
    print("Hola, Mundo")
    car = Car()
    car.license = "AMS234"
    car.drive = "Andrés Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "QWE567"
    car2.driver = "Manuel Herrera"
    print(vars(car2))
