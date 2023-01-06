#!/usr/bin/env python3
"""aeroninou | aeron.inouye@tlgcohort.com"""

#import methods to move and copy files.
import shutil

import os

def main():
    #move into the working dir
    os.chdir("/home/student/mycode/")
    
    #copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    
    #copy the entire dirA to dirB
    shutil.copytree("5g_research/", "5g_research_backup/")
    
# call our main function
if __name__ == "__main__":
    main()
