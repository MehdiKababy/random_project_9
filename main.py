import time
import random


class Car:
    def __init__(self, input_name, input_color, input_min_speed, input_max_speed):
        while True:
            if input_color in (
                "black",
                "white",
                "gray",
                "silver",
                "blue",
                "red",
                "green",
                "brown",
                "beige",
                "yellow",
            ):
                if input_name.title() in (
                    "Peugeot 206",
                    "Peugeot 405",
                    "Peugeot Pars",
                    "Samand",
                    "Dena",
                    "Rana",
                    "Tiba",
                    "Saina",
                    "Kia Cerato",
                    "Chery Tiggo 5",
                    "Brilliance H220",
                    "Jack S5",
                    "Peugeot 207",
                    "Mitsubishi ASX",
                    "Saipa 141",
                    "Pride",
                    "Khodro K1",
                    "Zamyad Z24",
                    "Iran Khodro Runna",
                    "Saba",
                    "Kia Rondo",
                    "Changan CS35",
                    "Peykan",
                    "Peugeot 504",
                    "Mazda 323",
                    "Datsun 120Y",
                    "Simorgh",
                    "Khodro 110",
                ):
                    break
                else:
                    print("This car name is not correct")
                    input_name = input("name : ")
            else:
                print("Color is not correct")
                input_color = input("color : ")
        self.name = input_name
        self.color = input_color
        while True:
            if 0 < input_min_speed <= 100:
                if 0 < input_max_speed <= 300:
                    if input_min_speed < input_max_speed:
                        break
                    else:
                        print("Max must be greater than min")
                        input_min_speed = int(input("min : "))
                        input_max_speed = int(input("max : "))
                else:
                    print("Range of max speed should 0 between 300")
                    input_max_speed = int(input("max : "))
            else:
                print("Range of min speed should 0 between 100")
                input_min_speed = int(input("min : "))
        self.min_speed = input_min_speed
        self.max_speed = input_max_speed
        self.car_is_runing = False

    def stop_car(self):
        print("Car stoped")
        print("You turned off the car")

    def start_move(self):
        print("How far will the car travel ? ")
        run_all = int(input("Enter number : "))
        print("Car started to move")
        while run_all > 0:
            delay = (random.randrange(self.min_speed, self.max_speed)) / 5000
            Run = 1
            while Run <= 10:
                print("-" * Run)
                Run += 1
                time.sleep(delay)
            Run = 10
            while Run > 1:
                print("-" * Run)
                Run -= 1
                time.sleep(delay)
            run_all -= 1

    def car_runing(self):
        starting = random.randrange(1, 5)
        while starting > 0:
            print("You start the car")
            start_delay = random.randrange(1, 3)
            time.sleep(start_delay)
            print("The car did not start")
            try_again = input("Try again ? ")
            if try_again.title() == "Yes":
                starting -= 1
            elif try_again.title() == "No":
                break
            else:
                print("Enter yes or no")
        print("car started")
        self.car_is_runing = True
        if starting == 0:
            self.start_move()


def run_car(input_obj):
    while True:
        run = input("Do you want to get in this car ? ")
        if run.title() in ("True", "Yes"):
            print(f"You got into a {input_obj.name} {input_obj.color}")
            input_obj.car_runing()
            if input_obj.car_is_runing:
                while True:
                    continue_to_move = input(
                        "Do you want to keep moving or trun off car or change car speed ? "
                    )
                    if continue_to_move.title() in ("Move", "Run", "Start"):
                        input_obj.start_move()
                    elif continue_to_move.title() in (
                        "Stop",
                        "Stop Car",
                        "Exit",
                        "Leave",
                    ):
                        input_obj.stop_car()
                        print("You got out of the car\n")
                        break
                    elif continue_to_move.title() in (
                        "Change",
                        "Change Speed",
                        "Speed",
                    ):
                        input_obj.min_speed = int(input("Enter new min speed : "))
                        input_obj.max_speed = int(input("Enter new max speed : "))
                        while True:
                            if 0 < input_obj.min_speed <= 100:
                                if 0 < input_obj.max_speed <= 300:
                                    if input_obj.min_speed < input_obj.max_speed:
                                        break
                                    else:
                                        print("Max must be greater than min")
                                        input_obj.min_speed = int(input("min : "))
                                        input_obj.max_speed = int(input("max : "))
                                else:
                                    print("Range of max speed should 0 between 300")
                                    input_obj.max_speed = int(input("max : "))
                            else:
                                print("Range of min speed should 0 between 100")
                                input_obj.min_speed = int(input("min : "))
                        input_obj.start_move()
                    else:
                        print("Enter yes or on")
        elif run.title() == "No":
            print("you are out of car")
            break
        else:
            print("Enter yes or no")


car_created_list = {}


def create_car():
    while True:
        create_car = input("You want to create a car ? ")
        if create_car.title() == "Yes":
            obj = Car(
                input("Enter name : "),
                input("Enter color : "),
                int(input("Enter min speed : ")),
                int(input("Enter max speed : ")),
            )
            run_car(obj)
            car_created_list.update(
                {
                    obj.name: {
                        "name": obj.name,
                        "color": obj.color,
                        "min speed": obj.min_speed,
                        "max speed": obj.max_speed,
                    }
                }
            )
        elif create_car.title() == "No":
            print("Create car task finished")
            break
        else:
            print("Enter yes or no")


def menu():
    while True:
        print("Do you want to crate a car or see list of previous created cars ? ")
        task_request = input("What do you want to do ? ")
        if task_request.title() in ("Create", "Build", "Create Car", "Build Car"):
            create_car()
        elif task_request.title() in (
            "Show",
            "List",
            "Show List",
            "List Car",
            "Show Car",
        ):
            if len(car_created_list) > 0:
                for item, value in car_created_list.items():
                    print(f"{item} : ")
                    for i_item, i_value in value.items():
                        print(f"    {i_item} : {i_value}")
            else:
                print("The number of created car is 0")
        elif task_request.title() in ("Exit", "End Task", "Leave"):
            break
        elif task_request.title() in ("Edit", "Edit Car"):
            while True:
                search_car = input("Enter Car name : ")
                if search_car in car_created_list.keys():
                    print("The car is founded")
                    while True:
                        change_request = input("Enter item for change : ")
                        if change_request.title() == "Name":
                            new_name = input("Enter new name : ")
                            if new_name.title() in (
                                "Peugeot 206",
                                "Peugeot 405",
                                "Peugeot Pars",
                                "Samand",
                                "Dena",
                                "Rana",
                                "Tiba",
                                "Saina",
                                "Kia Cerato",
                                "Chery Tiggo 5",
                                "Brilliance H220",
                                "Jack S5",
                                "Peugeot 207",
                                "Mitsubishi ASX",
                                "Saipa 141",
                                "Pride",
                                "Khodro K1",
                                "Zamyad Z24",
                                "Iran Khodro Runna",
                                "Saba",
                                "Kia Rondo",
                                "Changan CS35",
                                "Peykan",
                                "Peugeot 504",
                                "Mazda 323",
                                "Datsun 120Y",
                                "Simorgh",
                                "Khodro 110",
                            ):
                                car_created_list.update(
                                    {
                                        new_name: {
                                            "name": new_name,
                                            "color": car_created_list[search_car][
                                                "color"
                                            ],
                                            "min speed": car_created_list[search_car][
                                                "min speed"
                                            ],
                                            "max speed": car_created_list[search_car][
                                                "max speed"
                                            ],
                                        }
                                    }
                                )
                                car_created_list.pop(search_car)
                                search_car = new_name
                                print("The car name updated")
                            else:
                                print("This car name is not correct")
                        elif change_request.title() == "Color":
                            new_color = input("Enter new color : ")
                            if new_color.title() in (
                                "black",
                                "white",
                                "gray",
                                "silver",
                                "blue",
                                "red",
                                "green",
                                "brown",
                                "beige",
                                "yellow",
                            ):
                                car_created_list[search_car]["color"] = new_color
                                print("The car color updated")
                        elif change_request.title() in ("Min Speed", "Max Speed"):
                            new_min_speed = int(input("Enter new min speed : "))
                            new_max_speed = int(input("Enter new max speed : "))
                            while True:
                                if 0 < new_min_speed <= 100:
                                    if 0 < new_max_speed <= 300:
                                        if new_min_speed < new_max_speed:
                                            car_created_list[search_car][
                                                "min speed"
                                            ] = new_min_speed
                                            car_created_list[search_car][
                                                "max speed"
                                            ] = new_max_speed
                                            print("The car min and max speed updated")
                                            break
                                        else:
                                            print("Max must be greater than min")
                                    else:
                                        print("Range of max speed should 0 between 300")
                                else:
                                    print("Range of min speed should 0 between 100")
                        elif change_request.title() in ("Exit", "End Task", "Leave"):
                            break
                        else:
                            print("This item not in car properties")
                elif search_car.title() in ("Exit", "End Task", "Leave"):
                    break
                else:
                    print("This car not found")
        else:
            print("This task not supported")
            print("Try again")


menu()
