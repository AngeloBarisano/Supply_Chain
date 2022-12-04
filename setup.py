import os
import sys
# directory of script file
print(os.path.abspath(os.path.dirname(sys.argv[0])))
# change current working directory
os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
# current working directory
print(os.getcwd())


# directory of script file
print(os.path.abspath(os.path.dirname(__file__)))
# change current working directory
os.chdir(os.path.abspath(os.path.dirname(__file__)))
# current working directory
print(os.getcwd())



import sys

def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix


def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if is_venv():
    print('inside virtualenv or venv')
else:
    print('outside virtualenv or venv')




running_in_virtualenv = sys.prefix != sys.base_prefix
print(running_in_virtualenv)


real_prefix = getattr(sys, "real_prefix", None)
base_prefix = getattr(sys, "base_prefix", sys.prefix)

running_in_virtualenv = (base_prefix or real_prefix) != sys.prefix
print(running_in_virtualenv)



import os

if os.getenv('VIRTUAL_ENV'):
    print('Using Virtualenv')
else:
    print('Not using Virtualenv')