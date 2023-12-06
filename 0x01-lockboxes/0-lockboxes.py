#!/usr/bin/python3
'''A module for working with locked boxes.'''

def canUnlockAll(boxes):
    ''''Determines if all the boxes can be opened.'''
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False
