from vehicle import vehicle

class automobile(vehicle):
    
    year: int = 0
    make: str = ""
    model: str = ""
    doors: int = 4
    roof: str = ''

    #intializing the variable
    def __init__(self,t: int,y: int,ma: str,mo: str,d: int,r: str) -> None:
        super().__init__(t) #initialize type from parent class
        self.year = y
        self.make = ma
        self.model = mo
        self.doors = d
        self.roof = r

    #get/set for each variable
    #Year
    def get_year(self) -> int:
        return self.year
    def set_year(self, y: int) -> None:
        self.year = y
    #Make
    def get_make(self) -> str:
        return self.make
    def set_make(self, ma: str) -> None:
        self.make = ma
    #Model
    def get_model(self) -> str:
        return self.model
    def set_model(self, mo: str) -> None:
        self.model = mo
    #Doors
    def get_doors(self) -> int:
        return self.doors
    def set_doors(self, d: int) -> None:
        self.doors = d
    #Roof
    def get_roof(self) -> str:
        return self.roof
    def set_roof(self, r: str) -> None:
        self.roof = r

    #return all user info
    def return_auto(self) -> None:
        auto: dict = {
            "Type ":self.type,
            "Year ":self.year,
            "Make ":self.make,
            "Model":self.model,
            "Doors":self.doors,
            "Roof ":self.roof
        }
        print("==============================")
        print("User Automobile Information")
        print(" = = = = = = = = = = = = = = =")
        for key,value in auto.items():
            print(f"{key}:{value}")

