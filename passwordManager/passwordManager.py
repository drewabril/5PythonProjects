from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file: #wb represents 'write binary'
        key_file.write(key)

write_key()'''

def load_key():
    file = open('key.key', 'rb') #rb represents read binary, encryption works in a biary mode
    key = file.read()
    file.close()
    return key

#master_pwd = input("What is your password? ")
key = load_key()# + master_pwd.encode() # encode means we are working in binary again
fer = Fernet(key)


def view():
    with open ('pywords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #this strips off the \n carriage return from our add function
            user, passw = data.split("|") #sets deliniator for key value pairs. same as user, passw = [drew, password]
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    #use keyword 'with' to manipulate the file, open/close keywords are available but not as clean.
    with open('pywords.txt', 'a') as f:
# modes in with include Write, Read, Append (we picked a for append)
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("would you like to add, or view a password? (View/Add) press q to quit ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        quit()
    else:
        print("Not a valid mode")
        continue