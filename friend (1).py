x = str(input("welcome! where are you from?"))
y = ['new york', 'texas', 'california']

if (x == y[0]) or (x == y[1]) or (x == y[2]):
    z = str(input ("\(0 . 0)/ :D welcome! what do you wanna do today?"))

if z == "idk":
    a = "enter one for a random activity or two for nothing"
    print (a)

b = int(input('enter here:'))
if b < 2:
    print ("great! let's get started :)")
    import random
    num = random.randint(0, 5)
    print (num)
    if num == 1:
        print ("--you're gonna go for a run!")
    if num == 2:
        print ("--you're gonna listen to music!")
    if num == 3:
        print ("--you're gonna watch a random romcom!")
    if num == 4:
        print ("--you're gonna reread your favorite book! or comic, i don't judge!")
    if num == 5:
        print ("--buddy, this is your signal to do just nothing.")

