#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

categoryURL = "https://opentdb.com/api_category.php"

def main():

    difficulty = input("Choose a difficulty? Easy, Medium, Hard? ").lower()
    question_type = input("Choose a type? boolean or multiple or any? ").lower()
    num_questions = int(input("Number of questions? "))

    #if question type is not boolean or multiple will remove from URL
    if question_type == 'any':
        URL= f"https://opentdb.com/api.php?amount={num_questions}&category=21&difficulty={difficulty}"
    else:
        URL= f"https://opentdb.com/api.php?amount={num_questions}&category=21&difficulty={difficulty}&type={question_type}"
    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    
    number_of_question = 1
    for question in data['results']:
        questions = question.get('question')
        correct_answer = question.get('correct_answer')
        
        #print question
        print(f'\n{number_of_question}): {questions}')

        #loop through all the wrong answers 
        for answer in question.get('incorrect_answers'):
            print(f'Wrong answer: {answer}')

        print(f'Correct answer: {correct_answer}')

        number_of_question += 1
    """
    categoryData = requests.get(categoryURL).json()
    
    for data in categoryData['trivia_categories']:
        print(data['name'], data['id'])

    category = input("Choose a category above? ").lower()
    """





if __name__ == "__main__":
    main()

