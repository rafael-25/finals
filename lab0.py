from math import pi

def calculate_pizzas(guests):
    """
    Calculate the number of large, medium, and small pizzas needed.

    :param guests (int): The number of guests to be served.

    :returns tuple: A tuple containing the number of large,
                    medium, and small pizzas (in that order).
    """
    slices_per_guest = 3
    total_slices = guests * slices_per_guest

    slices_large = 10
    slices_medium = 8
    slices_small = 6

    large = total_slices // slices_large
    remaining_slices = total_slices % slices_large

    medium = remaining_slices // slices_medium
    remaining_slices %= slices_medium

    small = -(-remaining_slices // slices_small)  # Round up

    return large, medium, small

def serving_size(large, medium, small):
    """
    Compute the total area of pizzas ordered.

    :param large (int): Number of large pizzas.
    :param medium (int): Number of medium pizzas.
    :param small (int): Number of small pizzas.

    :returns float: Total area of the pizzas in square inches.
    """
    radius_large = 14 / 2
    radius_medium = 12 / 2
    radius_small = 10 / 2

    area_large = pi * (radius_large ** 2)
    area_medium = pi * (radius_medium ** 2)
    area_small = pi * (radius_small ** 2)

    total_area = (large * area_large) + (medium * area_medium) + (small * area_small)

    return total_area

def calculate_cost(large, medium, small, tip_percentage):
    """
    Compute the total cost of the pizzas, including tip.

    :param large (int): Number of large pizzas.
    :param medium (int): Number of medium pizzas.
    :param small (int): Number of small pizzas.
    :param tip_percentage (float): The percentage tip to add to the cost.

    :returns float: Total cost of the pizzas, including the tip, in dollars.
    """
    cost_large = 14.99
    cost_medium = 12.99
    cost_small = 9.99

    subtotal = (large * cost_large) + (medium * cost_medium) + (small * cost_small)
    tip = subtotal * (tip_percentage / 100)

    return subtotal + tip

def main():
    """
    The main function should:
    - Call the functions `calculate_pizzas`, `calculate_area`, and `calculate_cost` appropriately.
    - Prompt the user for input where needed.
    - Display the output in the format shown in the sample outputs.
    - Ensure all values are formatted correctly (e.g., using :.2f for numeric precision).
    """
    # Input: Number of guests
    guests = int(input("Please enter how many guests to order for: "))

    # Calculate number of pizzas
    large, medium, small = calculate_pizzas(guests)
    print(f"\n{large} large pizzas, {medium} medium pizzas, and {small} small pizzas will be needed.")

    # Calculate total pizza area
    total_area = serving_size(large, medium, small)
    area_per_guest = total_area / guests
    print(f"\nA total of {total_area:.2f} square inches of pizza will be ordered ({area_per_guest:.2f} per guest).")

    # Input: Tip percentage
    tip_percentage = float(input("\nPlease enter the tip as a percentage (i.e. 10 means 10%): "))

    # Calculate total cost
    total_cost = calculate_cost(large, medium, small, tip_percentage)
    print(f"\nThe total cost of the event will be: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
