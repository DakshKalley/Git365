# Git365 ~ Daily Commit Generator 

I use a crontab script to run `logger.py` daily.

The program can also be run manually without crontab.
```bash
crontab -e
* 10 * * * cd /Path/to/working/directory && python3 logger.py
``` 