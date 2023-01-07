#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...} """

def main():
    """runtime function"""
    marvelchars= {
    "Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

    "Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

    "Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

    
    char_name = input(" Which character do you want to know about? (Starlord, Mystique, Hulk): ").title()

    char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy): ").lower()

    value = marvelchars[char_name][char_stat]
    print(f"{char_name.title()}'s {char_stat} is: {value}")


# call our main function
if __name__ == "__main__":
    main()

