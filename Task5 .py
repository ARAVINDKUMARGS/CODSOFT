contacts = {}

def add_contact():

name = input("Name: ")

phone = input("Phone: ")

email = input("Email: ")

contacts [name] = {'Phone': phone,

'Email': email}

def view_contacts():

for name, info in contacts.items():

print(f"{name}: {info}")

def main():

while True:

print("\n1.Add 2. View 3.Exit")

choice = input("Choose: ")

if choice == '1':

add_contact()

elif choice == '2':

view_contacts()

elif choice == '3':

break

main()
