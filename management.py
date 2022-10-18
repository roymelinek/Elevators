from typing import List
import threading
from elevator import FastElevator, StandardElevator, CargoElevator


def call_elevator(elevators: List, current_floor, requested_floor, cargo_weight, num_of_people):
    """
    The function call for an elevator that can perform the mission in the fastest way if there is one available
    :param elevators: list of elevators
    :param current_floor: current floor of the tenant
    :param requested_floor: requested floor of the tenant
    :param cargo_weight: cargo weight in the elevator
    :param num_of_people: number of people in te elevator
    :return: message about the available elevator
     """
    chosen_elevator = None
    chosen_operation_time = None
    for elevator in elevators:
        if elevator.is_supported(
                current_floor=current_floor,
                requested_floor=requested_floor,
                cargo_weight=cargo_weight,
                num_of_people=num_of_people,
        ):

            operation_time = elevator.calculate_operation_time(
                customer_current_floor=current_floor,
                customer_requested_floor=requested_floor,
            )

            if chosen_operation_time is None:
                chosen_operation_time = operation_time
                chosen_elevator = elevator

            is_faster = operation_time < chosen_operation_time
            is_more_available = chosen_elevator.in_use and not elevator.in_use
            is_less_available = not chosen_elevator.in_use and elevator.in_use

            if is_more_available:
                chosen_operation_time = operation_time
                chosen_elevator = elevator

            if is_faster and not is_less_available:
                chosen_operation_time = operation_time
                chosen_elevator = elevator

    if not chosen_elevator:
        print('No supported elevators.')

    elif chosen_elevator.in_use:
        print(f'The {chosen_elevator.name} is ideal for you but it is in use..')
    else:
        print(f'{chosen_elevator.name} reserved, you will reach your destination in {chosen_operation_time} seconds.')
        chosen_elevator.reserve(
            current_floor, requested_floor)


def factory(elevator_type):
    """Factory Method"""
    localizers = {
        "Fast elevator": FastElevator,
        "Standard elevator": StandardElevator,
        "Cargo elevator": CargoElevator,
    }
    return localizers[elevator_type]()


def get_input(floors:int):
    """
    Get tenant's restrictions on elevator and try to reserve him an elevator
    :param floors: number of floors in the building
     """
    reserve_more = 1
    while reserve_more == 1:
        tenant_current_floor = int(input("Input your current floor"))
        if tenant_current_floor < 0 or tenant_current_floor > floors:
            raise Exception("Sorry, current floor is not valid")
        tenant_requested_floor = int(input("Input your requested floor"))
        if tenant_requested_floor > floors or tenant_requested_floor < 0:
            raise Exception("Sorry, requested floor is not valid")
        if tenant_current_floor == tenant_requested_floor:
            raise Exception("Sorry, the current floor must be different from the requested floor")
        tenant_cargo_weight = int(input("Input your cargo weight"))
        if tenant_cargo_weight < 0:
            raise Exception("Sorry, cargo weight is not valid")
        number_of_tenants = int(input("Input number of tenants"))
        if number_of_tenants < 1:
            raise Exception("Sorry, number of persons is not valid")

        threading.Thread(target=call_elevator,
                         args=(elevators, tenant_current_floor,
                               tenant_requested_floor, tenant_cargo_weight,
                               number_of_tenants)).start()

        reserve_more = int(input("Press 1 to reserve another elevator, else 0"))


if __name__ == '__main__':
    floors = int(input("Input number the floors in the building"))
    fast = factory("Fast elevator")
    standard = factory("Standard elevator")
    cargo = factory("Cargo elevator")
    fast.max_work_floor = floors
    standard.max_work_floor = floors
    elevators = [fast, standard, cargo]
    get_input(floors)