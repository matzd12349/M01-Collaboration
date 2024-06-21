
class vehicle:
    #A dictionary of variable types
    category: dict[str,int] = {
        0:"null",
        1:"car",
        2:"truck",
        3:"plane",
        4:"boat",
        5:"broomstick"
    }
    type: str = category[0]
    
    #initialize
    def __init__(self, t: int =0) -> None:
        self.type = self.category[t]

    #get list of types
    def display_types(self) -> dict:
        print("List of vehicle types")
        for key, value in self.category.items():
            print(f"{key}: {value}")

    #Get;Set functions
    def get_vehicle_type(self) -> str:
        return type
    def set_vehicle_type(self, t) -> None:
        self.type = self.category[t]

    