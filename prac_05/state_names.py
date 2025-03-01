"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# DONE: Reformated this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Print all states with string formatting
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

print()  # For separation between the list and user input prompt

# Take input and handle both lowercase and uppercase input
state_code = input("Enter short state: ").strip().upper()

while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").strip().upper()