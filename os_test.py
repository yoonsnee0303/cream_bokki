import os
from pathlib import Path

path = r'C:\Users\Data2\OneDrive\바탕 화면\네이버판매순'

print(os.path.abspath(path))
print(path.split(os.path.sep))