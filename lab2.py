def count_infected(city):
    """
    Count the number of infected people in the city.

    :param city (list): List of strings representing the city's state.

    :returns int: The number of infected people.
    """
    num_inf = 0
    for person in city:
        if person[0] == 'I':
            num_inf = num_inf + 1
    return num_inf

def has_infected_neighbor(city, position):
    """
    Check if a susceptible person at the given position has an infected neighbor.

    :param city (list): List of strings representing the city's state.
    :param position (int): Position of the person in the city.
    :returns bool: True if the person has an infected neighbor, False otherwise.
    """ 
    if len(city) <= 1:
        return False


    elif position == 0:
        right_neighbor = city[position + 1]
        return right_neighbor[0] == 'I'
    elif len(city) == position + 1:
        left_neighbor = city[position - 1]
        return left_neighbor[0] == 'I'
    else:
        left_neighbor, right_neighbor = city[position - 1], city[position + 1]
        return left_neighbor[0]  == 'I' or right_neighbor == 'I'

def advance_person(city, position, days_contagious):
    """
    Advance the state of a person in the city.

    :param city (list): List of strings representing the city's state.
    :param position (int): Position of the person in the city.
    :param days_contagious (int): Number of days a person remains contagious.
    :returns str: The new state of the person.
    """
    person = city[position]
    state = person[0]

    if state == 'R':
        return 'R'
    elif state == 'S':
        if has_infected_neighbor(city, position):
            return 'I0'
        else:
            return 'S'

    elif state == 'I':
        days_inf = int(person[1])
        if days_inf + 1 < days_contagious:
            return f"I{days_inf + 1}"
        else:
            return 'R'


def simulate_one_day(city, days_contagious):
    """
    Simulate the spread of the disease for one day.

    :param city (list): List of strings representing the city's state.
    :param days_contagious (int): Number of days a person remains contagious.
    :returns list: Updated city state after one day.
    """
    for pos in range(len(city)):

        city[pos] = advance_person(city, pos, days_contagious)

    return city


def run_simulation(city, days_contagious):
    """
    Run the simulation until there are no infected people.

    :param city (list): Initial state of the city.
    :param days_contagious (int): Number of days a person remains contagious.
    :returns tuple: Final state of the city and number of days simulated.
    """
    days = 0

    while count_infected(city) > 0:

      city = simulate_one_day(city, days_contagious)

      days += 1

    return city, days


if __name__ == "__main__":
    # Example: Simulate a city with 3 people contagious for 2 days
    city = ["S", "I0", "S"]
    days_contagious = 2
    final_state, days = run_simulation(city, days_contagious)
    print(f"Final state: {final_state}")
    print(f"Days simulated: {days}")
