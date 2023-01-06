#!/usr/bin/env python3
"""aeroninou | aeron.inouye@tlgcohort.com"""

import html

def main():
    """runtime function"""

    
    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
    

    

    print(trivia["question"])
    
    #all html cleaned up using html module
    correct = html.unescape(trivia["correct_answer"])
    a = html.unescape(trivia["incorrect_answers"][0])
    b = html.unescape(trivia["incorrect_answers"][1])
    c = html.unescape(trivia["incorrect_answers"][2])
    
    

    #print all the wrong answers
    print("wrong answer A) ", a)
    print("wrong answer B) ", b)
    print("wrong answer C) ", c)

    #correct answer printed
    print(f"correct D) {correct}\n")




#call our main function
if __name__ == "__main__":
    main()
