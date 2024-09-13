"""This is a program to plan a tea party based on a set number of guests"""

__author__: str = "730476269"


def main_planner(guests: int) -> None:
    """This is the entrypoint of the program to allow calculations"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    """This line prints an intro for the tea party"""
    print("Tea Bags: " + str(tea_bags(people=guests)))
    """This prints the number of tea bags needed based off the number of guests"""
    print("Treats: " + str(treats(people=guests)))
    """This prints the number of treats needed based on the number of guests"""
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    """This prints the cost of teabags and treats based on the number of guests"""


def tea_bags(people: int) -> int:
    """This will calculate how many tea bags are needed based on the number of guests"""
    return people * 2


"""The number of people is multiplied by 2 assuming every guest drinks 2 cups of tea"""


def treats(people: int) -> int:
    """This will calculate treats needed for the tea party."""
    return int(tea_bags(people=people) * 1.5)


"""The teabags are multiplied assuming everyone gets 1.5 treats per tea bag"""
"""The integer of this value is used to round up"""
"""No one is buying half of a treat, so we need to round up"""


def cost(tea_count: int, treat_count: int) -> float:
    "This will calculate the cost of treats and tea based on the number of guests"
    return tea_count * 0.50 + treat_count * 0.75


"""Note that tea costs $0.50 per tea bag and treats are $0.75 per treat"""
"""This is the total cost based on guests and previously defined functions """


if __name__ == "__main__":
    """This will run the main function and calculate the tea party plan"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    """This prompts the number of guests attending for the remaining functions"""
