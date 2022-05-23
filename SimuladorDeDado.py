#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

def Menu():
    op = str(input('[0] Sair | [1] Rolar um dado: '))
    return op

def main():
    while(Menu() != '0'):
        print('\nO número sorteado foi:', randint(1, 6), "\n")

if __name__ == "__main__":
    main()