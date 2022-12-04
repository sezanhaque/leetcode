class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big:
            self.big -= 1
            return True
        elif carType == 2 and self.medium:
            self.medium -= 1
            return True
        elif carType == 3 and self.small:
            self.small -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1), obj.addCar(2), obj.addCar(3))
