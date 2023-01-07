#!/usr/bin/env python3
"""aeroninou | aeron.inouye@tlgcohort.com"""

#learning about for logic

def main():
    """runtime function"""

    
    # create the list called vendors
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
   
   # loop across the list vendors
    for x in vendors:
        print("The vendor is:" + x) 
        #each time through the loop print value of x

    print("\nOur loop has ended.")
    #when the loop ends print this

# call our main function
if __name__ == "__main__":
    main()
