user = input("")
conv = open("conv.txt").read()
if user in conv:
    print(conv[conv.find(user)+len(user):].strip().split("\n")[0])
else:
    open("conv.txt","at+").write(user+"\n"+input("Então o que deveriamos reponder?? ")+"\n\n")
input("")
