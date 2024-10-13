class Students:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter for house
    @property
    def house(self):
        return self._house
    
    # Setter for house
    @house.setter
    def house(self, house):
        if not house:
            raise ValueError("Missing house")
        self._house = house

    # Getter for patronus
    @property
    def patronus(self):
        return self._patronus
    
    # Setter for patronus
    @patronus.setter
    def patronus(self, patronus):
        if not patronus:
            raise ValueError("Missing patronus")
        self._patronus = patronus

    def charm(self):
        match self.patronus:
            case "abracadabra":
                return "🐴"  # Corrected spelling from "abracadbra" to "abracadabra"
            case _:
                return "No patronus found."  # Default case

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")

    try:
        student = Students(name, house, patronus)  # Create the instance here
        return student
    except ValueError as e:
        print(e)  # Print the error message if raised
        return None  # Return None if there was an error

def main():
    student = get_student()
    
    if student:  # Check if student was created successfully
        print("Expecto Patronum!")
        print(student)  # Using the __str__ method
        print(student.charm())  # Call the charm method on the instance
    else:
        print("Failed to create student due to missing information.")

if __name__ == "__main__":
    main()
