# Colors used to inform users if the operation was successful or there was an error.
DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

# Dictionaries and variable's inicialization:
name = ""
price = ""
quantity = ""
inventory = {
    "manzana": {
      "price" : 3000,
      "quantity" : 32  
    },
    "piña": {
      "price" : 5500,
      "quantity" : 20  
    },
    "leche de almendras": {
      "price" : 8000,
      "quantity" : 20  
    },
    "gomitas": {
      "price" : 2000,
      "quantity" : 20  
    },
    "avena": {
      "price" : 1500,
      "quantity" : 60  
    }    
}

# Function's definition:
# Function validate str: verifies if the value is different than void and if it's alphanumeric
def validate_str(value):
  return value.strip() != "" and value.isalpha()

# Function validate num: verifies if the value is numeric and if it's greater than 0
def validate_num(value):
  return value.isnumeric() and int(value) > 0

# Function add product: adds a new product to the inventory, validating the values entered by the user
def add_product(name, price, quantity):
  flag = "s"
  while flag != "n":
    name = input("Ingresa el nombre del producto ").lower()
    if not validate_str(name):
        print(DANGER + "Error. Ingresa un valor válido." + RESET)
    if name in inventory:
      print(WARNING + "Este artículo ya se encuentra en el inventario, si deseas puedes actualizarlo." + RESET)
      return
    price = input("Ingresa el precio del producto ")
    quantity = input("Ingresa la cantidad del producto ")
    if not validate_num(price) and not validate_num(quantity):
      print(DANGER + "Error. Ingresa un valor válido." + RESET)
      continue
    inventory[name] = {"price": price, "quantity": quantity}
    print(SUCCESS + f"El producto {name} fue añadido exitosamente" + RESET)
    # User should press "n" to exit the function
    choice = input("¿deseas ingresar otro producto? [s/n] ").lower()
    match choice:
      case "n":
        break

# Function get product: verifies if the product name exists in the inventory, if it doesn't notifies the user and sugests them to create the new product. 
# Returns price and quantity.
def get_product():
    name = input("Ingresa el nombre del producto ").lower()
    if not validate_str(name):
      print(DANGER + "Error. Ingresa un valor válido." + RESET)
      return
    if name in inventory:
      price = inventory[name]['quantity']
      quantity = inventory[name]['price']
      print("Nombre: ", name)
      print("Cantidad: ", price)
      print("Precio: ", quantity)
      return price, quantity
    else:
        print(WARNING + "El producto no existe en el inventario. Si desea crearlo ingrese a agregar producto." + RESET)

# Function update product: validate if the product exists in the inventory and changes the old price to the new price and the dictionary
# Uses the function validate num to validate if the price is greater than 0 and a valid digit
def update_product():
  name = input("Ingresa el nombre del producto ").lower()
  if name in inventory:
    while True:
      update_product = input("Ingresa un nuevo precio: ")
      if not validate_num(update_product):
        print(DANGER + "Error. Ingresa un valor válido." + RESET)
        continue
      inventory[name]['Precio'] = int(update_product)
      print(SUCCESS + f"Su producto: {name} fue actualizado con éxito. Su nuevo precio es: {update_product}." + RESET)
      break
  else:
      print(WARNING + "Producto no existente en el inventario." + RESET)


# Function delete product: verifies if the product exists in the inventory, prints the quantity and deletes the product from the dictionary with .pop() method
def delete_product():
  name = input("Ingresa el nombre del producto ").lower()
  if name in inventory:
    print(f"El producto si se encuentra en el inventario, con {inventory[name]['quantity']} existencias.")
    # Asks the user if they are sure of deleting the product and can press "s" to continue or "n" to exit
    choice = input("¿estás seguro que deseas eliminarlo? [s/n] ").lower()
    match choice:
        case "s": 
            inventory.pop(name)
            print(SUCCESS + "Producto eliminado exitosamente" + RESET)
        case "n":
            print(DANGER + "Operación detenida. Ingresa una nueva opción." + RESET)
            return
  else:
      print(WARNING + "Producto no encontrado en el inventario." + RESET)
      
      
# Function calculate inventory: multiplies price with quantity of each product in the inventory and shows the total value of every product
def calculate_inventory():
  total = 0
  for name in inventory:
    multiplication = int(inventory[name]['price']) * int(inventory[name]['quantity'])
    total = total + multiplication
  print(f"El total del inventario actual es: {total:.2f}")

  
# Function menu: defines every option the user has to choose and returns option which is the value of each option
def menu():
  option = input("""
  Bienvenido a tu inventario. Ingresa la opción que deseas realizar
  \n[1] Agregar producto al inventario
  \n[2] Consultar producto del inventario
  \n[3] Actualizar precio del inventario
  \n[4] Eliminar producto del inventario
  \n[5] Calcular el valor total del inventario
  \n[6] Salir del sistema de inventarios

  """)
  return option

flag = True
while flag != 6:
  match menu():
    case "1": add_product(name, price, quantity)
    case "2": get_product()
    case "3": update_product()
    case "4": delete_product()
    case "5": calculate_inventory()
    case "6":
      break
    # if the user enters an unvalid option
    case _:
        print(WARNING + "Opción no válida." + RESET)







