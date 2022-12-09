#!/usr/bin/python3


def canUnlockAll(boxes):
    "method that determines if all the boxes can be opened."

    '#se recorren las posiciones de las cajas que se pueden abrir'
    for j in range(len(boxes)):
        if boxes[j]:
            continue
        else:
            '#se evaluan la longitud total de las'
            '#cajas con la longitud de las cajas abiertas'
            if (j != len(boxes) - 1):
                return False
    return True
