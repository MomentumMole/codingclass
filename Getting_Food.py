def main():

# Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
# Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
# Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
# The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
    
    Vegie = input("is anyone in your party vegetarian? ")
    Vegan = input("is anyone in your party vegan? ")
    Glute = input("is anyone in your party gluten-free? ")
    print()

    if Vegie == "no":
        if Vegan == "no":
            if Glute == "no":
                print("here are you resturant choices:")
                print()
                print("Joe's Gourmet Burgers")
                print("Main Street Pizza")
                print("Courner Café")
                print("Mama's Fine Italian")
                print("The Chef's Kitchen")

main()    