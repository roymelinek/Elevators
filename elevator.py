import time


class Elevator:
    def __init__(self):
        self.name = ""
        self.max_number_of_people = 0
        self.max_cargo_weight = 0
        self.operation_time_per_floor_in_secs = 0
        self.min_work_floor = 0
        self.max_work_floor = 0
        self.current_floor = 0
        self.in_use = False

    def calculate_operation_time(self, customer_current_floor, customer_requested_floor) -> int:
        """
        Calculate operation time - waiting time (for elevator) + serving time (in the elevator)
         :param customer_current_floor: current floor of the tenant
         :param customer_requested_floor: requested floor of the tenant
         :return: operation time
         """
        waiting_time = abs(self.current_floor - customer_current_floor) * self.operation_time_per_floor_in_secs
        serving_time = abs(customer_current_floor - customer_requested_floor) * self.operation_time_per_floor_in_secs
        operation_time = waiting_time + serving_time
        return operation_time

    def reserve(self, customer_current_floor, customer_requested_floor):
        """
        Pause the elevator according to the operation time (waiting time + serving time)
        :param customer_current_floor: current floor of the tenant
        :param customer_requested_floor: requested floor of the tenant
         """
        self.in_use = True
        operation_time = self.calculate_operation_time(customer_current_floor, customer_requested_floor)
        time.sleep(operation_time)
        self.current_floor = customer_requested_floor
        self.in_use = False

    def is_supported(self, current_floor, requested_floor, cargo_weight, num_of_people) -> bool:
        """
        Checks if there is an elevator that is supported by the restrictions the user has given
        :param current_floor: current floor of the tenant
        :param requested_floor: requested floor of the tenant
        :param cargo_weight: cargo weight in the elevator
        :param num_of_people: number of people in te elevator
        :return: True - if there is elevator that can fit those restrictions, else False
         """
        if current_floor >= self.min_work_floor and\
                requested_floor <= self.max_work_floor and \
                cargo_weight <= self.max_cargo_weight and \
                num_of_people <= self.max_number_of_people:
            return True
        return False


class FastElevator(Elevator):
    def __init__(self):
        super().__init__()
        self.name = "Fast elevator"
        self.max_number_of_people = 5
        self.max_cargo_weight = 0
        self.operation_time_per_floor_in_secs = 1
        self.min_work_floor = 10
        self.max_work_floor = 100


class StandardElevator(Elevator):
    def __init__(self):
        super().__init__()
        self.name = "Standard elevator"
        self.max_number_of_people = 10
        self.max_cargo_weight = 50
        self.operation_time_per_floor_in_secs = 3
        self.max_work_floor = 100


class CargoElevator(Elevator):
    def __init__(self):
        super().__init__()
        self.name = "Cargo elevator",
        self.max_number_of_people = 2
        self.max_cargo_weight = 750
        self.operation_time_per_floor_in_secs = 5
        self.max_work_floor = 5
