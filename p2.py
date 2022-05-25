def main(): 
    s = "(*)("
    
    counter = 0
    starCounter = 0
    isBroken = False

    for c in s:
        if c == "(":
            counter += 1
        if c == ")":
            counter -= 1
        if c == "*":
            starCounter += 1

        if counter < 0 and starCounter == 0:
            isBroken = True
            break


    retVal = False
    if(isBroken):
        retVal = False
    else:
        retVal = starCounter >= abs(counter)


    print( retVal )


if __name__ == "__main__":
    main()