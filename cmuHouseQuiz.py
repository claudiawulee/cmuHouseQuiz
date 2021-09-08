def donnerPoints(c, f, j, m, a):
    dCount = 0
    if c == "blue":
        dCount +=1
    if f == "pasta":
        dCount +=1
    if j == "nick":
        dCount +=1
    if m == "dinner":
        dCount+=1
    if a == "cat":
        dCount+=1
    return dCount

def mudgePoints(c, f, j, m, a):
    mCount = 0
    if c == "purple":
        mCount +=1
    if f == "steak":
        mCount +=1
    if j == "joe":
        mCount +=1
    if m == "breakfast":
        mCount+=1
    if a == "dog":
        mCount+=1
    return mCount

def steverPoints(c, f, j, m, a):
    sCount = 0
    if c == "green":
        sCount +=1
    if f== "cheeseburger":
        sCount +=1
    if j == "kevin":
        sCount +=1
    if m == "lunch":
        sCount+=1
    if a == "monkey":
        sCount+=1
    return sCount

def tieBreaker(dC, mC, sC):
    if dC == mC:
        music = input("pick a music streaming platform: apple music or spotify. ")
        if music =="apple music":
            dC +=1
        elif music == "spotify":
            mC +=1
    elif dC == sC:
        writing = input("pick a wriitng utensil: pen or pencil. ")
        if writing == "pen":
            sC +=1
        elif writing == "pencil":
            dC +=1
    else:
        subject = input("pick a subject: math or science. ")
        if subject == "math":
            sC +=1
        elif subject == "science":
            mC +=1
    return dC, mC, sC

def interactiveProgram():
    name = input("What's your name?")
    age = int(input("How old are you? (Type number only)")) #casting requirement
    print("Welcome to the CMU House quiz! Answer the following questions (using all lower case) and get sorted into 1 of 3 CMU Houses: Donner, Mudge, or Stever!")
    color = input("Pick a color: blue, green, or purple. ")
    food = input("Pick a food: cheeseburger, steak, or pasta. ")
    jonasBro = input("Pick a Jonas Brother: Joe, Nick, or Kevin. ")
    meal = input("Pick a meal: breakfast, lunch, or dinner. ")
    animal = input("Pick an animal: cat, dog, monkey. ")
    dCount = donnerPoints(color, food, jonasBro, meal, animal)
    mCount = mudgePoints(color, food, jonasBro, meal, animal)
    sCount = steverPoints(color, food, jonasBro, meal, animal)
    if dCount == mCount or dCount == sCount or mCount == sCount:
        dCount, mCount, sCount = tieBreaker(dCount, mCount, sCount)
    list = []
    list.extend((dCount,mCount,sCount))
    list.sort()
    #print(list)
    highestNum = list[-1]
    if highestNum == dCount:
        print("Congrats", name +"! At", age, "years old, you have been sorted into the Donner House!")
    elif highestNum == mCount:
        print("Congrats", name + "! At", age, "years old, you have been sorted into the Mudge House!")
    else:
        print("Congrats", name + "! At", age, "years old, you have been sorted into the Stever House!")