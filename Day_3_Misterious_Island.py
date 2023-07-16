import time

def text_game():
    def get_valid_input(question, valid_choices):
        while True:
            choice = input(question).lower()
            if choice in valid_choices:
                return choice
            else:
                print('Invalid choice! Please try again.')
    
    

    sleep = time.sleep(2)
    sleep
    print('Welcome to the game!')
    sleep
    print('''                                                 ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\V/ `
       ' oX`
          X                            v
          X             -HELP!
          X                                                 .
          X        \O/                                      |\
          X.a##a.   M                                       |_\
       .aa########a.>>                                    __|__
    .a################aa.                                 \   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                 David S. Issel''')
    sleep
    print('You woke up on an unknown island after a shipwreck. As you open your eyes, you find yourself surrounded by lush vegetation and the sound of crashing waves. The sun is shining brightly overhead, and the salty breeze fills the air.')
    sleep
    print('''Feeling disoriented, you try to gather your thoughts and figure out your next move. Suddenly, you notice two paths in front of you, each leading in a different direction. The first path appears to head deeper into the dense forest, while the second path leads to a secluded beach.''')
    sleep
    way = get_valid_input('Chose your option: forest or beach ', ('forest', 'first', 'beach', 'left', 'right', 'sea'))  
    sleep
    if way in ('forest', 'first' ,'left'):
        sleep
        print('''                     _______
                .-'"" ,-,-. ""`-.
             .-' ,-,-.`._.',-,-. `-.
           ,'    `._.'     `._.'    `.
         ,'     .-.     .-.     .-.   `.
        /-.`._.'.-.`._.'.-.`._.'.-.`._.'\
       /.-.`._.'.-.`._.'.-.`._.'.-.`._.'.\
      ;    `._.'   `._.'   `._.'   `._.'  :
      :                                   :
      |-.   ,--.   ,--.   ,--.   ,--.   ,-|
      :  )-(    )-(    )-(    )-(    )-(  :
      :-'   `--'   `--'   `--'   `--'   `-;
       \                                 /
        \  .o.   .o.   .o.   .o.   .o.  /
         \(   )=(   )=(   )=(   )=(   )/
          \)=(   )=(   )=(   )=(   )=(/
           \  'o'   'o'   'o'   'o'  /
            \                       /
             \       .-. .-.       /
              \ -=- (   `   ) -=- /
               \ -=- `.   .' -=- /
                \ -=-  `.'  -=- /
                 \             /
                  )___________(
                 ' |         | `
                 | |         | |
                 | I_________I |    
                 |/,-=-. ,-&-.\|    
                 I_\ '.#_'.' /_I    
                 |=o===o=======|    
                ;|=|;===;===;==|;   
               (_|=(_)=(_)=(_)=|_)  
                 `-|-----------'             C.J.
                   |
                 ._I_,''') 
        sleep
        print('you come across a clearing where a mysterious hot air balloon stands. The balloon is beautifully adorned with colorful patterns and seems ready for a journey.')
        sleep
        baloon = get_valid_input('to get into a hot air balloon? yes or no ', ('yes', 'no'))  
        if baloon in 'yes':
            sleep
            print('''                                 _ .--.
                                ( `    )
                             .-'      `--,
                  _..----.. (             )`-.
                .'_|` _|` _|(  .__,           )
               /_|  _|  _|  _(        (_,  .-'
              ;|  _|  _|  _|  '-'__,--'`--'
              | _|  _|  _|  _| |
          _   ||  _|  _|  _|  _|
        _( `--.\_|  _|  _|  _|/
     .-'       )--,|  _|  _|.`
    (__, (_      ) )_|  _| /
   jgs`-.__.\ _,--'\|__|__/
                    ;____;
                     \YT/
                      ||
                     |""|
                     '==''')
            sleep
            print('Curiosity overwhelms you, and you step into the basket of the balloon. Without warning, the balloon takes off, carrying you high above the island. From above, you witness breathtaking views of the turquoise ocean and distant islands. ')
            sleep
            print('''However, as the balloon drifts further away, you realize it's losing altitude rapidly. In a panic, you notice a parachute stored in the basket.''')
            sleep
            parachute = get_valid_input('Will you have the courage to jump and trust the parachute? yes or no', ('yes', 'no'))
            if parachute in 'yes':
                sleep
                
                print('''                           _______________
                          /               \
                         /                 \
                        /                   \
                        |   XXXX     XXXX   |
                        |   XXXX     XXXX   |
                        |   XXX       XXX   |
                        |         X         |
                        \__      XXX     __/
                          |\     XXX     /|
                          | |           | |
                          | I I I I I I I |
                          |  I I I I I I  |
                           \_           _/
                            \_         _/
                              \_______/
                    XXX                        XXX
                  XXXXX                        XXXXX
                   XXXXXXXXXX             XXXXXXXXXX
                           XXXXX     XXXXX
                               XXXXXXX
                           XXXXX     XXXXX
                   XXXXXXXXXX             XXXXXXXXXX
                  XXXXX                        XXXXX
                    XXX                        XXX''')
                sleep
                print('''you put on a parachute, jumped out of the balloon, but the parachute was folded in a haphazard manner, and it did not open. The game is over''')
                return print('Never panic!')
            else:
                sleep
                print('Gathering all your will in a fist, you decide that you can control the balloon yourself, and get down to business')
                sleep
                print(''':::8888888888888888888888888888888P""""""48888888888888888888888::::88
::::8888888888888888888888P   ____.------.____   488888888888888:::888
::::88888888888888888P __.--""    _._         ""--.__ 4888888888:::888
:::::888888888888P _.-"        .-~ | ~-.             "-._ 488888:::888
:::::888888888P _-"            |   |   |                 "-_ 488::8888
::::::888888P ,'               |  _:_  |                    .-:~--.._8
8:::::88888 ,'            .  .-"~~ | ~~"-.                .~  |      |
88:::::88P /_.-~:.   .   :   |     |     |       .        |   |      |
888::::8P /|    | `.o    !   |     |     |        :       |   |      |
8P_..--~:-.|    |  |    d    |     |     | .       o      |   |      |
8|      |  ~.   |  |    o    |  __.:.__  | ;       b      |   |      |
8|      |   |   |  |   d8  .-"~~   |   ~~"-.o       8     |   |      |
8|      |   |  _|.--~:-98  |       |       |8b      8.:~-.|   |      |
8|      A   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
8|      M   | |      |   | |       |  |   |     |  |  |   |   |      |
8|      C   | |      |   | |       |  |   |     |  |  |   |   O      |
8|      |   | |      |   | |       |  |   |     |  |  |   |   j      |
8|      9   | |      |   | |       |  |   |     |  |  |   |   o      |
8|      9   | |      |   | |       |  |   |     |  |  |   |   |      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
                sleep
                print('You succeed, and you successfully land the balloon outside the deserted island, near civilization - you are saved! ')
                sleep
                return print('you are winner!')
        elif baloon in 'no':
          sleep
          print('''                (
                 \
                  )
             ##-------->        b'ger
                  )
                 /
                (''')          
          sleep
          return print('You were accidentally killed by an Indian hunter who mistook you for a wild boar. What a bad luck!')    
    elif way in ('beach', 'right', 'sea'):
      sleep
      print('''           |
         \ _ /
       -= (_) =-
         /   \         _\/_
           |           //o\  _\/_
    _____ _ __ __ ____ _ | __/o\\ _
  =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
   =- _=-=- -_=-=_,-"          |
 jgs =- =- -=.--"''')
      sleep
      answer = get_valid_input('''You are walking along a picturesque beach, and you think you see a chest in the depths of the jungle, while a little further down the beach you hear people's voices. Which do you choose? The chest or the people?''', ('chest', 'people', 'box', 'crowd', 'voices' ))
      if answer in ('chest', 'box', 'treasure'):
        sleep
        print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''') 
        sleep
        return print('''When you open the chest, a snake bites your hand. You're dead. Tell me, why do you need treasure on a desert island?''')
      elif answer in ( 'people', 'crowd', 'voices' ):
        sleep
        print('''              ,
             /:\
             >:<
             >:<
             >:<
        ,,,,,\:/
       #########
      //////\\\\\
     // /_\ /_\ \\
     \(  0 _ 0  )/
     /\\=  _\ =//\
     \\/\ --- /\//
     //\ '---' /\\
     \//       \\/
     /\\       //\
     \\/       \//
      #         #
 jgs  "         "''')
        indians = get_valid_input('You decide to follow the voices of the people. As you get closer, you realize that they are Indians who have just noticed you. What are you going to do? Should you wave, or should you calmly approach them? Chose: waving or walking ', ('waving', 'wave', 'go', 'continue', 'walking' ))
        if indians in ('waving', 'wave'):
            sleep
            print('''            _,-+-._
         .-'       ''-._
        /               \
       '        ~.       \
      /    ~`'    ) .=" , )
     |           I (   ~ (
     \        '""   `='  +
      `.,_   `";:L0Ve'   *'
          `~'~.'  )_Y_0_U!\ ''')
            print('They misunderstood your gesture and shot you with their bows. You died. Be careful with strange languages and customs! ')
        elif indians in ('go', 'continue', 'walking'):
          sleep
          print('''    .                      ) /( ( (  .    .
             /\   .       )\ )\  /(         /\    /\
            /=/           \(/ _\/ /(        \=\  /=/   .
     .     /=/___       ()__)/ /(__()   .    \=\/=/
          /=/////\\         (_)             __\=|/
          \_\////_(_                       ////(_)\  .
          //////   _\       .             _)_\\\\\\\
          \///(.  _\                     /_   .)\\\\\
   .       (:) | _\              __     __/___o/\\\\\\_    .
        ___(:) ' \___ .__/\/\___/_/    /         \\\\\\\
       /   (:)       \   \  /         /(*)(*)(*)(*\\\\\\\
      /  _ (:)     _  \  / /          | _  _  _  _ \\\\\\
     /  / \__   __/ \  \/ /           |/_\/_\/_\/_\/_\/_|
     (  \ |       |__\   /   .         \_/\_/\_/\_/\_/\/  .
      \  \|       |   \_/              |/_\/_\/_\/_\/_\|
       \  |_______|/   \               |\_/\_/\_/\_/\_/|
  .     \/         \   /         .    /              jro\   .
        /           \ /              /(*)(*)(*)(*)(*)(*)(\
        \___________//   .           \___________________/
     .                       \|/ .             .            .''')
          sleep
          return print('You calmly approach the Indians, sit down in their circle, and light a pipe. They accept you as one of their own, and after a while you learn all their traditions and language. You are saved!')

text_game()
            