import art as a

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(a.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift %=26
 
def ceasar(msg, shif,drct): 
    cyper = ""
    if drct =="decode":
        shif*=-1
    for let in msg:
        pos = alphabet.index(let)
        new_pos = pos + shif
        new = alphabet[new_pos]
        cyper+=new
    print(f" your {drct} msg is  {cyper}")

ceasar(text,shift,direction)



# select either you want to encode or decode a message and give the input message


