#!/usr/bin/env python3
"""aeroninou | aeron.inouye@tlgcohort.com"""

"""movie/tv quote drinking game. Answer all the questions, wrong answers will result in a shot. after 10 shots you are drunk and will need a ride home.  
"""
#import random for random number
import random

def main():
    """runtime function"""

    #list with famous movie/tv quotes.
    #my_quotes = ["May the Force be with you", "I'll be back","Just keep swimming", "You’re killin’ me, Smalls", "To infinity and beyond!","Bye, Felicia", "So you’re telling me there’s a chance..", "Tina, you fat lard! Come get some dinner!","Keep the change, ya filthy animal.", "Do you understand the words that are coming out of my mouth?!"]

    #list will all the correct answers to the quotes. 
    #my_answers = ["star wars", "terminator", "finding nemo", "sandlot", "toy story", "friday", "dumb and dumber", "napoleon dynamite", "home alone", "rush hour"]

    quotes_answers = {"star wars": "May the Force be with you", "terminator": "I'll be back", "finding nemo" :"Just keep swimming", "sandlot":"Youre killin me, Smalls", "toy story": "To infinity and beyond", "friday":"Bye Felicia", "dumb and dumber":"So youre telling me theres a chance...", "napoleon dynamite":"Tina, you fat lard! Come get some dinner!","home alone":"Keep the change, ya filthy animal","rush hour":"Do you understand the words that are coming out of my mouth?!"}    
   
   # movie(key) and quote
    # movie, quote = random.choice(list(quotes_answers.items()))


    # count to keep track of wrong answers.
    shot_count = 0;

    #while loop 
    while shot_count < 10:

        #random generator number.
        #random_num = random.randint(0, 9)
        
        # movie(key) and quote
        movie, quote = random.choice(list(quotes_answers.items()))

        #input from user
        #answer = input(f"\nWhats this quote from? '{ my_quotes[random_num]}'\n").lower()
        answer = input(f"\nWhats this quote from? '{quote}'\n").lower()

        #checking input from user and answers list
        #if answer == my_answers[random_num]:
        if answer == movie:
            print("CORRECT. great job!\n")
            del quotes_answers[movie] # someone got the answer correct, remove it from the stack
        else:

            #will add to shot count if wrong answer.
            shot_count += 1

            #print message saying answer and input. with shots left.  
            #print(f"WRONG, take a SHOT. You said: {answer}. but correct answer was {my_answers[random_num]}\nSHOTS left: {10 - shot_count}\n")
            print(f"WRONG, take a SHOT. You said: {answer}. but correct answer was {movie}\nSHOTS left: {10 - shot_count}\n")

    #Once while loop reaches limit. exit message here. 
    print("---Sorry you lost, call an Uber and go watch Netflix---")

# call our main function
if __name__ == "__main__":
    main()
