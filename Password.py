# Write a C program that checks if a given password is strong, weak or moderate as 
# per the rules given below. 
# i) If it contains a combination of digits, alphabets and special characters, 
# then the password is strong. 
# ii) If it contains a combination of only digits and alphabets, then the  
# password is moderate. 
# iii) If it contains only alphabets, then the password is weak. 
 

def check_password(password):
    if len(password)<8:
        print("password should be more than 8 characters ")
    else:
        is_digit=False
        is_alpha=False
        special_char=False
        alphabets=0
        digits=0
        special_char=0
        for ch in password:
            if ch.isdigit():
                is_digit=True
                digits+=1
            elif ch.isalpha():
                is_alpha=True
                alphabets+=1
            else:
                special_char=True
                special_char+=1
        if is_digit and is_alpha and special_char:
            print("password is strong")
        elif is_digit and is_alpha or is_alpha and special_char or is_digit and special_char:
            print("passoword is moderate")
        else:
            print("password is weak")
    print(f"total digits: {digits} \ntotal alphabets {alphabets} \ntotal special_char {special_char}")

def main():
    password = input("Enter the password: ")
    check_password(password)
    
if __name__ == '__main__':
    main()