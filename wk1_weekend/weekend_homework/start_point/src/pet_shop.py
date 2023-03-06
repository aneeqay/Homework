# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    updated_amount = (pet_shop["admin"]["total_cash"]) + amount
    pet_shop["admin"]["total_cash"] = updated_amount
#   or pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, no):
    updated_no = (pet_shop["admin"]["pets_sold"]) + no
    pet_shop["admin"]["pets_sold"] = updated_no
    # or pet_shop["admin"]["pets_sold"] += no

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_name):
    list_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            list_by_breed.append(pet)
    
    return list_by_breed

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
          if pet["name"] == pet_name:
            return pet

# def remove_pet_by_name(pet_shop, pet_name):
#     pets = pet_shop["pets"]
#     for pet in pets:
#         if pet_name == pet["name"]:
#             del pets[pet]

def remove_pet_by_name(pet_shop, pet_name):
    pets = pet_shop["pets"]
    for i in range(len(pets) - 1):
        if pet_name == pets[i]["name"]:
            del pets[i]
    # or pet_to_delete = find_pet_by_name(pet_shop, pet_name)
    # pet_shop["pets"].remove(pet_to_delete)

def add_pet_to_stock(pet_shop, pet_to_add):
    pet_shop["pets"].append(pet_to_add)
    
def get_customer_cash(customer_list):
    return customer_list["cash"]

def remove_customer_cash(customer_list, amount):
    updated_amount = (customer_list["cash"]) - amount
    customer_list["cash"] = updated_amount
    # or customer_list["cash"] -= amount

def get_customer_pet_count(customer_list):
    return len(customer_list["pets"])

def add_pet_to_customer(customer_list, new_pet):
    pet_details = []
    pet_details.append(new_pet)
    customer_list["pets"] = pet_details
    #  or customer_list["pets"].append(new_pet)



def customer_can_afford_pet(customer_list, new_pet):
    if customer_list["cash"] >= new_pet["price"]:
        return True
    else:
        return False
    # or return customer_list["cash"] >= new_pet["price"]



def sell_pet_to_customer(pet_shop, pet_name, customer_list):
    if pet_name != None and customer_can_afford_pet(customer_list, pet_name):
        remove_pet_by_name(pet_shop, pet_name["name"])
        add_pet_to_customer(customer_list, pet_name)
        remove_customer_cash(customer_list, pet_name["price"])
        add_or_remove_cash(pet_shop, pet_name["price"])
        increase_pets_sold(pet_shop, 1)

