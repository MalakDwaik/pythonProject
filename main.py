vegetables = ["Cucumber", "Tomato", "Carrot", "pepper"]
fruits = ["apple", "grape", "Figs", "Peache"]

banner = """ 
** Welcome To Amo Emad's shop ****

** Welcome to customer service ***
"""
print(banner)

services = """
[1] View products
[2] Add product 
[3] Delete product
[4] Edit the product
[5] Exit
"""
print(services)

x = (input("Enter the desired service number: "))
ser = int(x)

if (ser == 1):
    print("[?!] View products")
    print("The vegetables present are: ", vegetables)
    print("The fruits present are: ", fruits)
elif (ser == 2):
    print("\n [?!] Add product")

    add = input("""\n Enter the type you want to add to it (vegetables / fruits) ...
                    If vegetables, enter a letter (v) ...
                    If fruits, enter a letter (f) ... \n 
                    """)
    if (add == 'v'):
        g = input("\n Enter what you want to add to the list of vegetables: ")
        vegetables.append(g)

        print("\n ** Added successfully ***")

        print("\n The list of vegetables is as follows: ", vegetables)

    elif (add == 'f'):
        d = input("\n Enter what you want to add to the list of fruits: ")
        fruits.append(d)

        print("\n ** Added successfully ***")

        print("\n The list of fruits is as follows: ", fruits)

    else:
        print("Wrong Entry")



elif (ser == 3):
    print("[?!] Delete products")

    delete = input("\n Enter the name of the product to be deleted: ")
    res = input("\n Enter the type of product you want to delete (Vegetables(v)/ Fruits(f)): ")

    if (res == 'v'):
        vegetables.remove(delete)

        print("\n ** Deleted Successfully ***")
        print("\n Vegetables list has become: ", vegetables)

    elif (res == 'f'):
        fruits.remove(delete)

        print("\n ** Deleted Successfully ***")
        print("\n Fruits list has become: ", fruits)

    else:
        print("Wrong Entry")

elif (ser == 4):
    print("[?!] Edit the product")
    edit = input("\n Enter the name of the product to be edit: ")
    ed = input("\n Enter the type of product you want to edit (Vegetables(v)/ Fruits(f)): ")
    t = input(f"\n Enter the product to be added instead of {edit}: ")

    if (ed == 'v'):
        vegetables.insert(edit, t)

        print("\n ** Edit Successfully ***")
        print("\n Vegetables list has become: ", vegetables)

    elif (ed == 'f'):
        fruits.insert(edit, t)

        print("\n ** Edit Successfully ***")
        print("\n Fruits list has become: ", fruits)

    else:
        print("Wrong Entry")

elif (ser == 5):
    print("The program has been exited ,,, ")

else:
    print("Wrong Entry")
