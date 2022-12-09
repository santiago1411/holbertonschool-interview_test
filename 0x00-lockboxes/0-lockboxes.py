#!/usr/bin/python3
"""method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """se recorren las posiciones de las cajas que se pueden abrir"""
    for j in range(len(boxes)):
        if boxes[j]:
            continue
        else:
            if (j != len(boxes) - 1):
                return False
    return True
