# https://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations/

class Station:
    def __init__(self, petrol, distanceToNextStation):
        self.petrol = petrol
        self.distanceToNextStation = distanceToNextStation

def findTour(stations):
    start = -1
    numStations = len(stations)
    for i in range(numStations):
        if stations[i].petrol >= stations[i].distanceToNextStation:
            start = i
            break
    if start == -1:
        return -1
    end = (start + 1) % numStations
    petrolLeft = stations[start].petrol - stations[start].distanceToNextStation
    while start != end:
        petrol = petrolLeft + stations[end].petrol
        if petrol >= stations[end].distanceToNextStation:
            petrolLeft = petrol - stations[end].distanceToNextStation
        else:
            if (end + 1) % numStations <= start:
                return -1
            start = end + 1
            petrolLeft = stations[start].petrol - stations[start].distanceToNextStation
        end = (end + 1) % numStations
    return end

stations = [Station(4, 6), Station(6, 5)]
print(findTour(stations))
    


