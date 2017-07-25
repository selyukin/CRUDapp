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
		for ordered_dict in reader:
			inventory.append(dict(ordered_dict))

ids = []
for i in range(0, len(inventory)):
	ids.append(inventory[i]["id"])

# Created a function for writing the dictionary back to CSV
def WriteCSV():
	with open(csv_path, "w") as file:
		writer = csv.DictWriter(file, 
			fieldnames=["id","name","aisle","department","price"])
		writer.writeheader()
		for product in inventory:
			writer.writerow(product)

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
	"   Destroy   | Delete an existing product. \n"
	"   Exit      | Exit the application.")

task = input()

def ListOp():
	'''This function reads the dictionary created
	from reading the CSV and prints out
	the ID and name of each product'''
	for i in range(0, len(inventory)):
		print ("+  ID:" + inventory[i]["id"] + 
			", Name: " + inventory[i]["name"])

def ShowOp():
	'''This function requests a user input for a product 
	identifier, then reads the dictionary and prints the
	product info for the product matching the ID. If the
	product ID is not in the inventory the app states so 
	and prompts the user for a new ID.'''
	item = input("Please specify a product id:")
	if item in ids:
		item = int(item) - 1
		print ("Name:", inventory[int(item)]["name"], "\n",
				"Department:", inventory[int(item)]["department"], "\n",
				"Aisle:", inventory[int(item)]["aisle"], "\n",
				"Price: $" + inventory[int(item)]["price"])
	else:
		print ("Sorry, this item is not in the inventory.")
		ShowOp()

def CreateOp():
	'''This functions prompts the user to enter information
	for a new product. It then appends this information to
	the dictionary and writes everything out to the CSV,
	overwriting the original.'''
	print ("Please specify new product information:")
	newName = input("Name:")
	newDept = input("Department:")
	newAisle = input("Aisle:")
	newPrice = float(input("Price:"))
	print ("Creating a new product.")
	#can modify below to autoincrement the product IDs, should re-index
	inventory.append({'id':int(len(inventory)+1), 'name':newName,
		'department':newDept, 'aisle':newAisle, 'price':newPrice})
	WriteCSV()
	print ("There are now %i products in the inventory." %(len(inventory)))
	
def UpdateOp():
	'''This function prompts the user for the ID of
	a product to update. The user is then prompted
	to enter all the new information for this product.
	The dictionary is then updated with this new product
	information and then written out to the CSV,
	overwriting the original.
	'''
	item = input("Please specify a product id:")
	print ("Please specify new product information:")
	newName = input("Change name to:")
	newDept = input("Change department to:")
	newAisle = input("Change aisle to:")
	newPrice = float(input("Change price to:"))
	print ("Updating product information. \n New product details:")
	item = int(item) - 1
	inventory[int(item)]["name"] = newName
	inventory[int(item)]["department"] = newDept
	inventory[int(item)]["aisle"] = newAisle
	inventory[int(item)]["price"] = newPrice
	WriteCSV()
	print ("Name:", inventory[int(item)]["name"], "\n",
			"Department:", inventory[int(item)]["department"], "\n",
			"Aisle:", inventory[int(item)]["aisle"], "\n",
			"Price: $" + str(inventory[int(item)]["price"]))

def DestroyOp():
	'''This function prompts the user for a
	product ID and then deletes that product
	information from the dictionary. The CSV
	is then overwritten with the updated 
	dictionary.
	'''
	item = input("Please specify a product to remove:")
	item = int(item) - 1
	inventory.remove(inventory[item])
	#should reindex products
	print ("Product deleted. There are now {0} products in the inventory"
		.format(len(inventory)))
	WriteCSV()

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
	elif task == "Exit":
		print ("Goodbye!")
	else:
		print ("Sorry, please specify a valid operation")
		task = input()
		CRUD(task)


#Run application
CRUD(task)