"""Greet a user

Usage:

    python3 greetings.py <name>
"""


import sys


def greet(name):
    """Greet a user.

        Args:
            name: Name of a user.
        
        Returns:
            No return value.  
    """
    print("Hello {}!".format(name))


def main(name):
    """Greet a user.

    Args:
        name: Name of a user.
        
    Returns:
        No return value.  
    """    
    greet(name)
    

if __name__ == "__main__":
    main(sys.argv[1])
