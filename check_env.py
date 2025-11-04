#!/usr/bin/env python3
"""
check_venv.py
Detects if the script is running inside a virtual environment.
"""

import sys

def is_virtual_environment():
    """
    Returns True if running inside a virtual environment.
    Works for venv, virtualenv, and conda (with caveats for conda).
    """
    # Standard venv/virtualenv check
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        return True
    return False

if __name__ == "__main__":
    if is_virtual_environment():
        print("YES! You are running inside a virtual environment.")
        print(f"  Virtual env prefix: {sys.prefix}")
        print(f"  Base Python prefix: {sys.base_prefix}")
    else:
        print("NO virtual environment detected.")
        print(f"  System Python prefix: {sys.prefix}")
        if hasattr(sys, 'base_prefix'):
            print(f"  base_prefix: {sys.base_prefix}")