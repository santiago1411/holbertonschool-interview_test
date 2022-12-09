#!/usr/bin/python3

def canUnlockAll(boxes):
    for j in range(len(boxes)):
        if boxes[j]:
            continue
        else:
            if (j < len(boxes) - 1):
                return False
    return True