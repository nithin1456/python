def check_pass(password):
    upper = any(i.isupper() for i in password)
    lower = any(i.islower() for i in password)
    digit = any(i.isdigit() for i in password)
    spcl = any( not i.isalnum() for i in password)


    if len(password)>8 and  upper and lower and digit and spcl:
        return "Strong"
    elif len(password)>6 and  len(password)<=8:
        return "medium"
    else:
        return "weak"




# if __name__ == "__main__":
re = input(" enetr the password :  ")
strength = check_pass(re)

print(f" you got {strength} password")