from pathlib import Path
import os
import datetime

# Creates log.txt file in working directory if it doesn't exist
logPath = Path(str(Path.cwd()) + "/log.txt")
if logPath.is_file() == False:
    logPath.write_text('GIT365 LOG\n')

# Writes the date and time to the log
if logPath.is_file():
    print(logPath)
    logFile = open(logPath, 'a')
    msg = ('\nGit365 LOG ~ ') + str(datetime.datetime.now())
    logFile.write(msg)
    logFile.close()
    logFile = open(logPath)
    print(logFile.read())

# Checks if Commiter is Executable
if os.access('commit.sh', os.X_OK) != True:
    print("Making commit file executable")
    os.system('chmod 755 commit.sh')

# Git Commiter
os.system('./commit.sh')