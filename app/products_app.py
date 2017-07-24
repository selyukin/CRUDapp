#Some functions use a hardcoded dictionary of products, some read a csv
#Not checking for validity of input, will have to add check for product in csv


import csv

# Reading CSV
csv_path = "data/products.csv"

'''updated with Prof's code for cleaner script, 
appends rows read from CSV to dictionary
rather than rereading CSV multiple times'''
inventory = []

with open(csv_path, "r") as file:
		reader = csv.DictReader(file)
		for row in reader:
			inventory.append(row)

#THE CRUD APP

print ("----------------")
print ("Products Application")
print ("----------------")
print ("Welcome selyukin:")
print ("There are %i products in the database. Please select an operation:"
	%((len(inventory)))) 
print ("\n",
	"   Operation | Description \n"
	"   --------- | ----------- \n"
	"   List      | Display a list of product identifiers and names. \n"
	"   Show      | Show information about a product. \n"
	"   Create    | Add a new product. \n"
	"   Update    | Edit an existing product. \n"
	"   Destroy   | Delete an existing product.")

task = input()

def ListOp():
	'''This function reads the dictionary created
	from reading the CSV and prints out
	the ID and name of each product'''
	for i in range(0, len(inventory)):
		print ("+  ID:" + inventory[i]["id"] + 
			", Name: " + inventory[i]["name"])

#Still need to add count of products
def ShowOp():
	'''This function requests a user input for a product 
	identifier, then reads the dictionary and prints the
	product info for the product matching the ID. If the
	product ID is not in the inventory the app states so 
	and prompts the user for a new ID.'''
	item = input("Please specify a product id:")
	ids = []
	for i in range(0, len(inventory)):
		ids.append(inventory[i]["id"])
	if item in ids:
		item = int(item) - 1
		print ("Name:", inventory[int(item)]["name"], "\n",
				"Department:", inventory[int(item)]["department"], "\n",
				"Aisle:", inventory[int(item)]["aisle"], "\n",
				"Price: $" + inventory[int(item)]["price"])
	else:
		print ("Sorry, this item is not in the inventory.")
		ShowOp()


'''
#The below functions still utilize the dictionary rather than the CSV
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]
'''
#Will need to append to csv
def CreateOp():
	print ("Please specify new product information:")
	newName = input("Name:")
	newDept = input("Department:")
	newAisle = input("Aisle:")
	newPrice = float(input("Price:"))
	print ("Creating a new product:")
	inventory.append({'id':int(len(inventory)+1), 'name':newName,
		'department':newDept, 'aisle':newAisle, 'price':newPrice})
	with open(csv_path, "w") as file:
		writer = csv.DictWriter(file, 
			fieldnames=["id","name","aisle","department","price"])
		writer.writeheader()
		for product in inventory:
			writer.writerow(product)
	print ("There are now %i products in the inventory." %(len(inventory)))
	
 
#will need to add overwrite of information to csv
def UpdateOp():
	item = input("Please specify a product id:")
	print ("Please specify new product information:")
	newName = input("Change name to:")
	newDept = input("Change department to:")
	newAisle = input("Change aisle to:")
	newPrice = float(input("Change price to:"))
	print ("Updating product information. \n New product details:")
	products[int(item)-1]["name"] = newName
	products[int(item)-1]["department"] = newDept
	products[int(item)-1]["aisle"] = newAisle
	products[int(item)-1]["price"] = newPrice
	print (products[int(item)-1])

#Will need to delete from csv
def DestroyOp():
	item = input("Please specify a product to remove:")
	products.remove(products[(int(item)-1)])
	print ("Product deleted.")
			# below two steps are just a check
	#print (len(products))
	#ListOp()

def CRUD(task):
	if task == "List":
		ListOp()
	elif task == "Show":
		ShowOp()
	elif task == "Create":
		CreateOp()
	elif task == "Update":
		UpdateOp()
	elif task == "Destroy":
		DestroyOp()
	else:
		print ("Sorry, please specify a valid operation")
		task = input()
		CRUD(task)


#Run application
CRUD(task)