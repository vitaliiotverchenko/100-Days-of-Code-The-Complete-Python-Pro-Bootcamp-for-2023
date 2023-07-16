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
    print('You woke up on an unknown island after a shipwreck. As you open your eyes, you find yourself surrounded by lush vegetation and the sound of crashing waves. The sun is shining brightly overhead, and the salty breeze fills the air.')
    sleep
    print('''Feeling disoriented, you try to gather your thoughts and figure out your next move. Suddenly, you notice two paths in front of you, each leading in a different direction. The first path appears to head deeper into the dense forest, while the second path leads to a secluded beach.''')
    sleep
    way = get_valid_input('Chose your option: forest or beach', 'forestfirstoneleftdense')  
    sleep
    if way in ('forestfirstoneleftdense'):
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
        print('you come across a clearing where a mysterious hot air balloon stands. The balloon is beautifully adorned with colorful patterns and seems ready for a journey.')
        sleep
        baloon = get_valid_input('to get into a hot air balloon? yes or no', 'yesno')  
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
            print('Curiosity overwhelms you, and you step into the basket of the balloon. Without warning, the balloon takes off, carrying you high above the island. From above, you witness breathtaking views of the turquoise ocean and distant islands. ')
            sleep
            print('''However, as the balloon drifts further away, you realize it's losing altitude rapidly. In a panic, you notice a parachute stored in the basket.''')
            sleep
            parachute = get_valid_input('Will you have the courage to jump and trust the parachute?', 'yesno')
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
                print('You succeed, and you successfully land the balloon outside the deserted island, near civilization - you are saved! ')
                return 'you are winner!'
                
            
text_game()
            