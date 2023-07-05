import random
import os
import time

def print_with_delay(delay=000.1):
    animation = [
        "\033[0;35m__________                    .__               __________             .__          __    __           \033[0;35m",
        "\033[0;35m\______   \__ __  ______ _____|__|____    ____  \______   \ ____  __ __|  |   _____/  |__/  |_  ____   \033[0;35m",
        "\033[0;35m |       _/  |  \/  ___//  ___/  \__  \  /    \  |       _//  _ \|  |  \  | _/ __ \   __\   __\/ __ \  \033[0;35m",
        "\033[0;35m |    |   \  |  /\___ \ \___ \|  |/ __ \|   |  \ |    |   (  <_> )  |  /  |_\  ___/|  |  |  | \  ___/  \033[0;35m",
        "\033[0;35m |____|_  /____//____  >____  >__(____  /___|  / |____|_  /\____/|____/|____/\___  >__|  |__|  \___  > \033[0;35m",
        "\033[0;35m        \/           \/     \/        \/     \/         \/                       \/                \/  \033[0;35m",
    ]
    for line in animation:
        print(line)
        time.sleep(delay)

def main():
    os.system('clear')
    print_with_delay(delay=00.1)

    number = random.randint(1, 10)
    
    while True:
        print(" ")
        guess = int(input("\033[1;32mTest your luck, choose a number between 1 and 10: \033[1;32m"))
        if guess < 1 or guess > 10:
            print("")
            print("\033[0;31mYour number should be between 1 and 10.\033[0;31m")
            time.sleep(2)
            main()
        else:
            break
    
    if guess == number:
        print(" ")
        print("Good job, you won the roulette")
        time.sleep(2)
        main()
    else:
        print(" ")
        print("You are dead, your number was:", number)
        time.sleep(2)
        main()

while True:
    main()
