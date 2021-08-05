from cryptography.fernet import Fernet



'''
def write_key():
	key = Fernet.generate_key()
	with open("key.key","wb") as key_file:
		key_file.write(key)

'''



def load_key():
	file = open('key.key','rb')
	key = file.read()
	file.close()
	return key

pwd = input("Choose a master password: ")
key = load_key() + pwd.encode()
fer = Fernet(key)

def view():
	with open('passwords.txt','r') as f:
		for line in f.readlines():
			data = line.rstrip()
			username,pwd = data.split('|')
			print(f'User: {username}, Password: {fer.decrypt(pwd.encode().decode())} ')


def add():
	name = input("Account Name: ")
	password = input("Password: ")
	with open('passwords.txt', 'a') as f:
		f.write(f"{name}|{fer.encrypt(password.encode()).decode()} \n")


while True:
	user = input("Would you like to add a new password (A), or view existing ones (V)?  Press q to quit").upper()
	if user == "Q":
		break
	if user == "V":
		view()
	elif user == "A":
		add()
	else:
		print("Invalid mode.")
		continue

