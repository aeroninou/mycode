#!/usr/bin/env python3
"""aeroninou | aeron.inouye@tlgcohort.com"""

#shell utilities will be used to move files
import shutil

#provides access to low level os operations
import os

def main():
    """runtime function"""

    #move to working dir
    os.chdir('/home/student/mycode/')
    
    #move file raynor into ceph
    shutil.move('raynor.obj', 'ceph_storage/')

    #get input from user for name
    xname = input('What is the new name for kerrigan.obj? ')
    
    #moving files in ceph/newname
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

    

# call our main function
if __name__ == "__main__":
    main()
