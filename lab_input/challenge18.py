
#! usr/bin/python3

def main():
    
    #get input of name of user
    name = input("What is you name? ")

    #get input of day of week
    day_of_week = input("What day of the week is it? ")

    #print out the input and string concat
    print(f"Hello, {name}! Happy {day_of_week}!")
    print("Hello, " + name + "! Happy " + day_of_week + "!")
    print("Hello, ", name, "! Happy ", day_of_week, "!", sep="") 


if __name__ == "__main__":
    main()
