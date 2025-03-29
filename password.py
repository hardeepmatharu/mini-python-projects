from cryptography.fernet import Fernet

#write key into a key file
'''def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)'''


#load key to decrypt
def load_key():
    f = open('key.key', 'rb')
    key = f.read()
    f.close()
    return key

key = load_key()
fer = Fernet(key)

#function to add password
def add_pwd():
    name = input('Enter the account name: ')
    pwd = input('Enter the password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')


#function to view password
def view_pwd():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split('|')
            print('User:', user, '| Passowrd:',fer.decrypt(passw.encode()).decode())



while True:
    mode = input('Would you like to create a new password or view the existing one? (view/add) or press q to quit. ')
    
    if mode == 'q':
        break

    if mode == 'view':
        view_pwd()
    elif mode == 'add':
        add_pwd()
    else:
        print('Invalid mode')