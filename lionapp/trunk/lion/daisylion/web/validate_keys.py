import re

# descriptive string of valid keys
VALID_KEYS = "A-Z, Ctrl, Alt, Shift, Up, Down, Left, Right, Esc, Space, +, -"

def validate_keys(key):
    """Make sure the key falls within the valid range"""
    # A-Z
    expr = "[a-z]"
    named_keys = ("ctrl", "alt", "shift", "up", "down", "left", "right", "esc", "space", 
        "+", "-", "uparrow", "downarrow", "rightarrow", "leftarrow")
    
    p = re.compile(expr, re.IGNORECASE)
    if p.match(key) and len(key) == 1:
        return True
    if key.lower() in named_keys:
        return True
    
    return False


    