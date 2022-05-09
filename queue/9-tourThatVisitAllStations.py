# https://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations/
class Station:
    def __init__(self, petrol, next):
        self.petrol = petrol
        self.next = next

def tour(stations):
    start = -1
    n = len(stations)
    for i in range(n):
        if stations[i].petrol > stations[i].next:
            start = i
            break
    if start == -1:
        return "Not Possible"
    end = (start + 1) % n
    petrol = stations[start].petrol - stations[start].next
    while start != end:
        petrol += stations[end].petrol
        if petrol >= stations[end].next:
            petrol -= stations[end].next
            end = (end + 1) % n
        else:
            start = -1
            while True:
                i = end + 1
                if i >= n:
                    return "Not Possible"
                if stations[i].petrol > stations[i].next:
                    start = i
                    break
                end = (start + 1) % n
    return start

stations = [Station(6, 4), Station(3, 6), Station(7, 3)]
print(tour(stations))
    


