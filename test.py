
import os
print(os.path.abspath(os.path.dirname(__file__)))

# change current working directory
os.chdir(os.path.abspath(os.path.dirname(__file__)))
# current working directory
print(os.getcwd())