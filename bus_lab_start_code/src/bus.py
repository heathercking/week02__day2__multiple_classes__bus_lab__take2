from src.bus_stop import BusStop
# from src.person import Person

class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self,passenger):
        self.passengers.append(passenger)

    def drop_off(self,passenger):
        self.passengers.remove(passenger)

    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self,bus_stop_1):
        for passenger in bus_stop_1.queue:
            if self.route_number in passenger.valid_buses:
                self.passengers.append(passenger)
        bus_stop_1.clear()

    def drop_off_passenger_at_stop(self, bus_stop_drop_off):
        for passenger in self.passengers:
            if passenger.destination == bus_stop_drop_off:
                self.passengers.remove(passenger)
