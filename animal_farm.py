#!/usr/bin/python3

"""Our own little animal farm."""

import sys

from animals import sheep
from animals import lion
from animals import leopard
from animals import goat
from animals import cat
from animals import dog
import animal
import farm

def create_animal(kind):
    """Create an animal class."""
    if kind == 'cat':
        result = cat.Cat()
    if kind == 'dog':
        result = dog.Dog()
    if kind == 'sheep':
        result = sheep.Sheep()
    if kind == 'lion':
        result = lion.Lion()
    if kind == 'leopard':
        result = leopard.Leopard()
    if kind == 'goat':
        result = goat.Goat()
    else:
        result = animal.Animal(kind)
    return result

def main(animals):
    """This is the main function"""
    animal_farm = farm.Farm()
    for animal_kind in animals:
        animal_farm.add_animal(create_animal(animal_kind))
    animal_farm.print_contents()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Pass at least one animal type!')
        sys.exit(1)
    main(sys.argv[1:])
