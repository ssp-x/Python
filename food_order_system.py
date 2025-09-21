italian_food = [
    "Pasta Bolognese",
    "Pepperoni pizza",
    "Margherita pizza",
    "Lasagna"
]

indian_food = [
    "Curry",
    "Chutney",
    "Samosa",
    "Naan"
]

def find_meal(name, menu):
    name_l = name.strip().lower()
    for item in menu:
        if item.lower() == name_l:
            return item
    return None

def select_meal(name, food_type):
    if food_type.lower() == "italian":
        return find_meal(name, italian_food)
    elif food_type.lower() == "indian":
        return find_meal(name, indian_food)
    else:
        return None

def display_available_meals(food_type):
    if food_type.lower() == "italian":
        print("\nAvailable Italian Meals:\n")
        for meal in italian_food:
            print(meal)
    elif food_type.lower() == "indian":
        print("\nAvailable Indian Meals:\n")
        for meal in indian_food:
            print(meal)
    else:
        print("\nInvalid food type")

def create_summary(name, amount, food_type):
    order = select_meal(name, food_type)
    if order:
        return f"\nYou ordered {amount} {order}"
    else:
        return "\nMeal not found"

def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        if not value.isdigit():
            print("\nEnter a valid quantity.")
            continue
        amount = int(value)
        if amount > 0:
            return amount
        print("\nEnter a valid quantity.")

def get_valid_meal(food_type):
    while True:
        name_input = input("\nEnter the name of the meal you want to order: ").strip()
        if select_meal(name_input, food_type):
            return find_meal(name_input, italian_food if food_type.lower() == "italian" else indian_food)
        print("\nMeal not found. Please choose a meal from the menu. Try again.")

def main():
    print("Welcome to the Food Order System!")
    while True:
        while True:
            food_type = input("\nEnter the type of food you want to order (Italian/Indian): ").strip()
            if food_type.lower() in {"italian", "indian"}:
                break
            print("\nPlease enter 'Italian' or 'Indian'.")
        display_available_meals(food_type)
        chosen_meal = get_valid_meal(food_type)

        amount_input = get_positive_int("\nEnter the quantity you want to order: ")

        result = create_summary(chosen_meal, amount_input, food_type)
        print(result)

        again = input("\nWould you like to place another order? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for visiting. Goodbye!")
            break

if __name__ == "__main__":
    main()
