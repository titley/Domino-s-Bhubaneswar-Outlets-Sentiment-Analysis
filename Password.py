master_pwd= input ("what is the master password")

def view():
    with open ('passwords.txt', 'r') as f:
        for line in f.readlines():
            print (line.rstrip()) 


 
def add():
    name= input("account name: ")
    pwd = input ("Password : ")
    with open ('passwords.txt', 'a') as f:
        f.write(name+"| "+pwd+ "\n")

while True:
    mode= ("would you like to add new password or view existing one (add or view)?, press q to quit").lower
    if mode == 'q':
    break
    if mode=='view':
        view()
    elif mode =='add':
        add()
    else:
        print ("invalid mode")
        continue