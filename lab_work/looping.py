#!/usr/bin/env python3
"""aeroninou | aeron.inouye@tlgcohort.com"""

def main():
    """runtime function"""
    
    count = int(input("pick a number to start bottles of beer on the wall?: "))

    for i in range(count):
        print(count, "bottles of beer on the wall!")
        print(f"{count} bottles of beer on the wall! {count} bottles of beer! You take one down, pass it around!\n")
        count -= 1

# call our main function
if __name__ == "__main__":
    main()
