from pathlib import Path
from datetime import datetime


file_path = Path("main.py")
stats = file_path.stat()
time_created = stats.st_ctime
print(stats)
time_created = datetime.fromtimestamp(time_created)
print(time_created)
print(time_created.strftime("%Y-%m-%d %H:%M:%S"))
