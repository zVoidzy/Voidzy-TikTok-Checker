from random import choice

query = "qwertyuiopasdfghjklzxcvbnm0123456789._"
file = open("names.txt","w")

leng = int(input("Username lenght: "))
lc = input("l/c? ")
if lc == "l":
    query = "qwertyuiopasdfghjklzxcvbnm"
else:
    query = "qwertyuiopasdfghjklzxcvbnm0123456789._"

num = int(input("How many usernames you want to generate: "))

for x in range(0,num):
    username = ""
    for x in range(0,leng):
        username_char = choice(query)
        username = username + username_char
    try:
        int(username)
    except:
        digit = False
    else:
        digit = True
    if username[-1] != '.' and digit == False:
        print(username)
        file.write(username + "\n")
    
    

input()
