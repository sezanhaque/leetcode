class UndergroundSystem:
    def __init__(self):
        # Dictionary to store check-in information with customer_id as key and (start_station, check_in_time) as value
        self.check_ins = {}

        # Dictionary to store total travel time and count for each (start_station, end_station) pair
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_ins.pop(id)
        travel = (start_station, stationName)
        travel_time = t - check_in_time

        if travel in self.travel_times:
            total_time, count = self.travel_times[travel]
            self.travel_times[travel] = (total_time + travel_time, count + 1)
        else:
            self.travel_times[travel] = (travel_time, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation)
        total_time, count = self.travel_times[travel]

        return total_time / count


obj = UndergroundSystem()
obj.checkIn(45, "Leyton", 3)
obj.checkIn(32, "Paradise", 8)
obj.checkIn(27, "Leyton", 10)
obj.checkOut(45, "Waterloo", 15)
obj.checkOut(27, "Waterloo", 20)
obj.checkOut(32, "Cambridge", 22)
print(obj.getAverageTime("Paradise", "Cambridge"))
