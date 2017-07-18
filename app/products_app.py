print ("----------------")
print ("Products Application")
print ("----------------")
print ("Welcome selyukin:")
print ("There are _ products in the database. Please select an operation:")
print ("\n",
	"   Operation | Description \n"
	"   --------- | ----------- \n"
	"   List      | Display a list of product identifiers and names. \n"
	"   Show      | Show information about a product. \n"
	"   Create    | Add a new product. \n"
	"   Update    | Edit an existing product. \n"
	"   Destroy   | Delete an existing product.")

task = input()

def CRUD(task):
	if task == "List":
		print ("Display")
	elif task == "Show":
		print ("Show")
	elif task == "Create":
		print ("Add")
	elif task == "Show":
		print ("Edit")
	elif task == "Destroy":
		print ("Delete")
	else: print ("Wrong input")

CRUD(task)

