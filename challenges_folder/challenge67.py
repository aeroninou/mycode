#!/usr/bin/env python3
"""aeroninou | aeron.inouye@tlgcohort.com"""

def main():
    """runtime function"""

    count = 0
    with open ("dracula.txt", "r") as dracula:
        with open("vampytimes.txt", "w") as new_dracula:
            for line in dracula:
                if "vampire" in line.lower():
                    count += 1
                    new_dracula.write(f"{count}): {line}")
    print(count)

# call our main function
if __name__ == "__main__":
    main()
