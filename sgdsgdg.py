def main():
    while True:
        again = input("Would you like to play again? Enter y/n: ")

        if again == "n":
            print ("Thanks for Playing!")
            return
        elif again == "y":
            print ("Lets play again..")
        else:
            print ("You should enter either \"y\" or \"n\".")

if __name__ == "__main__":
    main()