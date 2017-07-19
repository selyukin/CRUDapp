#For now this is using a hardcoded dictionary of products
#Not checking for validity of input, will have to add check for product in csv



# Need to modify existing code so products = read_from_csv instead of dictionary
# Use code from shopping_cart, but instead of a new list of IDs, check in csv

import csv

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


# Reading CSV
csv_path = "data/products.csv"

'''with open(csv_path, "r") as inventory:
	inventory = csv.DictReader(inventory)
	for row in inventory:
		#print (row) #this prints lists of entire contents with headers
		#if row['id']=='3': #change number to user input product number to select specific product
		print (row["id"], row["name"], row["aisle"], row["department"], row["price"])
'''		

#with open(csv_path, "w") as inventory:
#	inventory =csv.DictWriter(inventory, fieldnames=["id", "name", "aisle", "department", "row"])
#	writer.writerow


#THE CRUD APP

print ("----------------")
print ("Products Application")
print ("----------------")
print ("Welcome selyukin:")
print ("There are %i products in the database. Please select an operation:"
	%((len(open(csv_path).readlines()))-1)) #https://stackoverflow.com/questions/16108526/count-how-many-lines-are-in-a-csv-python
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
	#for product in products:
	#	print ("+  ID:" + str(product["id"]), "Name: " + product["name"])
	with open(csv_path, "r") as inventory:
		inventory = csv.DictReader(inventory)
		for row in inventory:
			print ("+  ID :" + row["id"] + " Name: " + row["name"])

#Will need to add count of products?
#Need to check is product ID is in the CSV, handle invalid identifiers
def ShowOp():
	item = input("Please specify a product id:")
	if int(item) > 0 and int(item) < 21:
	#	print ("Name:", products[(int(item)-1)]["name"], "\n"
	#		"Department:", products[(int(item)-1)]["department"], "\n"
	#		"Aisle:", products[(int(item)-1)]["aisle"], "\n"
	#		"Price: ${0:.2f}".format(products[(int(item)-1)]["price"]))
		with open(csv_path, "r") as inventory:
			inventory = csv.DictReader(inventory)
			for row in inventory:
				if row['id']==item:
					print ("Name:", row["name"], "\n",
						"Department:", row["department"], "\n",
						"Aisle:", row["aisle"], "\n",
						"Price: $" + row["price"])


#Will need to append to csv
def CreateOp():
	print ("Please specify new product information:")
	newName = input("Name:")
	newDept = input("Department")
	newAisle = input("Aisle:")
	newPrice = float(input("Price:"))
	print ("Creating a new product:")
	products.append({'id':int(len(products)+1), 'name':newName,
		'department':newDept, 'aisle':newAisle, 'price':newPrice})
	#print (len(products))
	print (products[(len(products))-1])
 
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