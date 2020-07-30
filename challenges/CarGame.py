# Commands:
# help: shows every command that can be executed
# start: starts the car
# stop: stops the car
# quit: exit the game

command = ""

car_is_started = False

while True:
    command = input("> ").lower()
    if command == "help":
        help_msg = '''start: starts the car
stop: stops the car
quit: exit the game'''
        print(help_msg)
    elif command == "quit":
        break
    elif command == "start":
        if car_is_started:
            print("Car already started")
        else:
            car_is_started = True
            print("Car started... Ready to go!")
    elif command == "stop":
            if car_is_started:
                print("Car stopped.")
                car_is_started = False
            else:
                print("Car already stopped")
    else:
        print("I don't understand that")
