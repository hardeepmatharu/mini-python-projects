master_pwd = input('What is the master password? ')

#function to add password
def add_pwd():
    name = input('Enter the account name: ')
    pwd = input('Enter the password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n')
#function to view password
def view_pwd():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())

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