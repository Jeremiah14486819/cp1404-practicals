# Constant dictionary of color names and their hex codes
COLOR_CODES = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BISQUE": "#ffe4c4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#ffebcd",
    "BLUE": "#0000ff",
    "BLUEVIOLET": "#8a2be2"
}

# Print instructions to the user
print("Enter a color name to get its hexadecimal code (enter a blank line to exit):")

# Loop to prompt the user for color names until a blank input is given
color_name = input("Enter color name: ").strip().upper()  # Convert input to uppercase for case insensitivity

while color_name != "":
    # Check if the color name exists in the dictionary
    if color_name in COLOR_CODES:
        print(f"The hex code for {color_name} is {COLOR_CODES[color_name]}")
    else:
        print(f"Sorry, {color_name} is not a valid color name.")

    # Ask for the next color name
    color_name = input("Enter color name: ").strip().upper()  # Convert input to uppercase for case insensitivity
