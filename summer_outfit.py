degrees = int(input())
date_night = input()
outfit = ""
shoes = ""


if date_night == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    if 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    if degrees >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif date_night == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    if 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    if degrees >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"

elif date_night == "Evening":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    if 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    if degrees >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
