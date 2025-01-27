def suggest_clothing(temperature):
    clothing_options = [
        ((85, float('inf')), "light clothes like shorts and a t-shirt."),
        ((70, 85), "a light jacket or sweater."),
        ((50, 70), "a jacket or sweater."),
        ((float('-inf'), 50), "a heavy jacket, gloves, and a hat.")
]


    for temp_range, clothing in clothing_options:
        if temperature >= temp_range[0] and temperature < temp_range[1]:
            return f"It's {temp_range} outside. Wear {clothing}"
    
    return "Unable to determine appropriate clothing."

def main():
    temperature = float(input("Enter the temperature in Fahrenheit: "))
    clothing_suggestion = suggest_clothing(temperature)
    print("Weather suggestion:", clothing_suggestion)

if __name__ == "__main__":
    main()
