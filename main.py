import os

# File Logger
os.system('python3 logger.py')

# Checks if Commiter is Executable
if os.access('commit.sh', os.X_OK) != True:
    print("Making commit file executable")
    os.system('chmod 755 commit.sh')

# Git Commiter
os.system('./commit.sh')