# this is Sentence Checking Programme
digit=0
words=0
letter=0

user_input=input("Enter Your Text : ")

for x in user_input:
    x=x.lower()
    if x>="a" and x<="z" :
        letter=letter+1
    elif x>="0"  and x<="9":
        digit=digit+1
    elif x==" " :
        words=words+1
print("Numbers : ", digit)
print("Letters : ", letter)
print("Words: ", words)
