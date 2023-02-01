from car import Car
from account import Account
from UberX import UberX
from user import User


if __name__ == "__main__":
    print("### Initializing ###")
    print("### Car: ###")
    car = Car("AMS234", Account("Andrés Herrera",
                                "ANDA876",
                                "andres@platzi.com",
                                "234567"))
    print(vars(car))
    print(vars(car.driver))

    print("### UberX: ###")
    uberX = UberX("UBS234", Account("Marcos Botero",
                                    "MAR876",
                                    "marcbot@platzi.com",
                                    "678901"), "Ford", "2018")
    print(vars(uberX))
    print(vars(uberX.driver))

    print("### User: ###")
    user = User("Mariana Valle", "SDFG123G",
                "marianavalle@platzi.com", "12345")
    print(vars(user))
