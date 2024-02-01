import art
print(art.logo)

def ceaser_cypher(direction,text,shift):
    plain_text = ''
    if direction == 'encode':
        for i in range(len(text)):
            if text[i] != ' ' and text[i] not in list('1234567890'):
                if (ord(text[i]) + shift) >= 122:
                    plain_text += alphabet[-(122-(ord(text[i])+shift))-1]
                else:
                    plain_text += alphabet[ord(text[i]) + shift-97]
            else:
                plain_text += text[i]
    elif direction == 'decode':
        for i in range(len(text)):
            if text[i] != ' ' and text[i] not in list('1234567890'):
                plain_text += alphabet[ord(text[i]) - shift -97]
            else:
                plain_text += text[i]
        
    print(f"The {direction}d text is {plain_text}")

count = 0
alphabet = list('abcdefghijklmnopqrstuvwxyz')
while count != 1:
    direction = input("What do you want to do? encode or decode? \n").lower()
    if direction == 'encode' or direction =='decode':
        text = input(f"Enter the text you want to {direction}: ").lower()
        shift = int(input(f"Enter the shift: "))
        ceaser_cypher(direction=direction,text=text,shift=shift)
    else:
        print("Enter a valid choice")
    repeat = input("do you want to go again? ").lower()
    if repeat != 'yes':
        count = 1
