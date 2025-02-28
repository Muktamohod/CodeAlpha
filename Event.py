users=[]

def encrypt(input,shift=4) :
    small_alphabet='abcdefghijklmnopqrstuvwxyz' 
    cap_alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits='0123456789'
    encrypted_input=''


    for char in input :
        small_alphabet_index= small_alphabet.find(char)
        cap_alphabet_index= cap_alphabet.find(char)
        digits_index= digits.find(char)

        if small_alphabet_index !=-1 :
            new_index= (small_alphabet_index +shift)%26
            new_char= small_alphabet[new_index]

        elif cap_alphabet_index !=-1 :
            new_index= (cap_alphabet_index +shift)%26
            new_char= cap_alphabet[new_index]
        
        elif digits_index !=-1 :
            new_index= (digits_index +shift)%10
            new_char= digits[new_index]

        else :
            new_char = char
        
        encrypted_input = encrypted_input + new_char
    
    return encrypted_input

def decrypt(input,shift=4) :
    small_alphabet='abcdefghijklmnopqrstuvwxyz' 
    cap_alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits='0123456789'
    decrypted_input=''


    for char in input :
        small_alphabet_index= small_alphabet.find(char)
        cap_alphabet_index= cap_alphabet.find(char)
        digits_index= digits.find(char)

        if small_alphabet_index !=-1 :
            new_index= (small_alphabet_index -shift)%26
            new_char= small_alphabet[new_index]

        elif cap_alphabet_index !=-1 :
            new_index= (cap_alphabet_index -shift)%26
            new_char= cap_alphabet[new_index]
        
        elif digits_index !=-1 :
            new_index= (digits_index -shift)%10
            new_char= digits[new_index]

        else :
            new_char = char
        
        decrypted_input = decrypted_input + new_char
    
    return decrypted_input


def take_input() :

    encrypted_username= encrypt(input('Enter a username of your choice : '))

    matchfound= False

    for user in users :
        
        if user.get('username')== encrypted_username :
            matchfound= True
            print('Registration not allowed. Username exists !!')
            break
    
    if not matchfound :
        print('Username allowed !')
        encrypted_password= encrypt( input('Enter a password : '))
        users.append({'username':encrypted_username,'password':encrypted_password })

def show_users():
    print('Users registered so far :\n')
    for i in range(len(users)) : 
        
        print('Username : ',decrypt(users[i].get('username')), 'Password : ',users[i].get('password'))

    
def main() :
    print("Welcome to our Event Registration System :\n")

    while True :
        x=input('Do you want to register ? Y/N ')

        if x.lower()=='y' :
            take_input()
        else :
            break

    show_users()

main()



