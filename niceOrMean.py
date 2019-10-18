#
#
#
# Python:       3.7.4
#
# Author:       Keith Korter
#
#
#
# Purpose:      How to pass variables from function to function
#               while producing a functional game.
#



def start(nice=0,mean=0,name=""):
    # get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)



def describe_game(name):
    """
        check if its a new game or not
        if new, get users name.
        if not new, thank player for playing again.
    """

    if name !="":
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at end of the game your fate \nwill be sealed by your actions.")
                    stop = False

    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input ("\nA stranger approaches for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenancingly and storms off....")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass 3 variable to the score()



def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the values stored within 3 variables
    if nice > 2: #if condition is valid call win function
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call the lose function passing in the variable
        lose(nice,mean,name)
    else:    #else, call nice_mean function passing in the var so it can use them
            nice_mean(nice,mean,name)


def win(nice,mean,name):
    # Substitute the () wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    #sub the {} the variable values
    print("\nAhhhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user is playing
    start(nice,mean,name)


if __name__ == "__main__":
    start()
