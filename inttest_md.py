import md
import os.path
md.run_md()
from pathlib import Path
my_file = Path("./cu.traj")
if my_file.exists():
    print("file exists")
else:
    print("file doesn't exist")
