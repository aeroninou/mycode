#!/usr/bin/env python3

def main():
    """runtime function"""
    
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    
    print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")

    a = trial[2].get('goggles')
    b = trial[2].get('eyes')
    c = trial[3]
    print(f"My {a}! The {b} do {c}!")
    
    a = nightmare[0].get('user').get('name').get('first')
    b = nightmare[0].get('kumquat')
    c = nightmare[0].get('d')

    print(f"My {a}! The {b} do {c}!")

# call our main function
if __name__ == "__main__":
    main()

