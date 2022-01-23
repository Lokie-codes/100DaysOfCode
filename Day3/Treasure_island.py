# Treasure map ASCII code
print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----|
 \_/__________________________________________________________________|
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------|
 \_/__________________________________________________________________| 
''')

print("Welcome aboard!!! Let's find some treasure.")
in1 = input("You are on a splitting road.. which way do you wanna go? Left or right (l or r) - ")
if(in1 == 'r'):
    print("You fell into a hole. Sorry.. Game Over")
elif(in1 == 'l'):
    in2 = input("You are confronted with a river.. would you swim or wait for a ship? (s or w) - ")
    if(in2 == 's'):
        print("You were attacked by trout.. Game Over")
    elif(in2 == 'w'):
        in3 = input("A ship halted and you travelled across the river. \n You have 3 doors in front of you \n RED \t YELLOW \t GREEN \n which wud you choose? \n (r y or g) -")
        if(in3 == 'r'):
            print("You were eaten by a Lion..Game Over")
        elif(in3 == 'g'):
            print("You ate a lot of jelly and your stomach burst out.. Game Over")
        elif(in3 == 'y'):
            print("You have unlocked the treasure.. Congratulations!!!")
        else:
            print("Wrong input.. Game Over")
    else:
        print("Wrong input..Game Over")
else:
    print("Wrong input..Game Over")