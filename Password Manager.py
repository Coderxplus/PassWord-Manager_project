import json
from pathlib import Path
import random
import string
from pprint import pprint

PASSWORD_LENGTH = 13

def Password_gen():
    gen_upper= random.choices(string.ascii_uppercase, k=4)
    gen_lower = random.choices(string.ascii_lowercase, k=4)
    gen_digits = random.choices(string.digits ,k=4)
    gen_char = random.choices("#$!@%^&*", k=3)
    
    generated_val=random.choices(gen_digits+gen_char+gen_lower+gen_upper,k=PASSWORD_LENGTH)
    
    sorted_val = "".join(generated_val)

    print(sorted_val)
   

def save_password(name, password):
   

    current_save = Path("User.json").read_text()
    q = current_save.replace("\"","")
    user_data = [
            current_save.replace("\"", "").strip(""),
            {"password_name": name, "password":password}
        ]
    data = json.dumps(user_data)
  
    
    Path("User.json").write_text(data)

def password_manager():
    print("Welcome to Password manager")
    print("Do you want to see saved password type(open)>>"," or do  you want to Generate a new password type(gen)>>")
    answer =input("()>>").lower()
    
    if answer == "open":
        saves = Path("User.json").read_text()
        pprint(saves)
    elif answer == "gen":
        Password_gen()

        answer=input("do you want to save password input (y/n)>>")
        if answer == "y" or "yes":
            name = input("input the name of password name>>")
            password=input("copy the password above and paste here>>")
            save_password(name, password)
        else:
            pass



if __name__ == '__main__':
    password_manager()
    
    
    


