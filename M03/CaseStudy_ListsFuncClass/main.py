import automobile

#funciton to get user input
def get_user_input(prompt:str,type,valid: list) -> type:
    while True:
        try:
            user_input = type(input(prompt))
            if valid is not None:
                if user_input not in valid:
                    raise ValueError(f"Input must be: {valid}")
                else:
                    return user_input
            else:
                return user_input
        except ValueError as e:
            print(f"Invalid input: {e}. Please Try Again with ", type)

def main() -> None:
    #car variable
    user_car: automobile = automobile.automobile(0,0,'','',4,'')

    user_car.return_auto()

    print("Enter the details of your car.")
    print("==============================")
    user_car.display_types()
    print("==============================")
    user_car.set_vehicle_type(get_user_input("Please enter the number that corresponds to your vehicle type: ",int,[0,1,2,3,4,5]))
    user_car.set_year(get_user_input("Please enter your vehicle year: ",int,None))
    user_car.set_make(get_user_input("Please enter your vehicle make: ",str,None))
    user_car.set_model(get_user_input("Please enter your vehicle model: ",str,None))
    user_car.set_doors(get_user_input("Does it have two or four doors: ",int,[2,4]))
    user_car.set_roof(get_user_input("Is the roof 'solid' or 'sun roof'",str,['solid','sun roof']))
    print("==============================")

    user_car.return_auto()


main()

    
    