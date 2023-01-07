#!/usr/bin/env python3
"""aeroninou | aeron.inouye@tlgcohort.com"""

def main():
    """runtime function"""

    
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    
   # ne_farm = farms[0]["agriculture"]
   # for animal in ne_farm:
   #     print(animal)

    
    ask_farm = input("\nWhat farm would you like? ").lower()

    if ask_farm == "ne farm":
        result = 0
    elif ask_farm == "w farm":
        result = 1
    else: result = 2

    #this uses he result form input to find the farm in list
    farm = farms[result]["agriculture"]
    
    #loop through ag in farm if not an animal it skips over
    for agriculture in farm: 
        if agriculture == "celery" or agriculture == "carrots":
            continue
        else: 
            print(agriculture)

    

# call our main function
if __name__ == "__main__":
    main()
