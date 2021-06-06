# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Написать программу, которая считывает текст из файла и определяет, сколько в нем слов состоящих из не менее чем семи букв.

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puncList = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
        fc = f.read()
        for i in puncList :
            fc.replace(i,'')
        words = fc.split()
print(words)
words = [i for i in words if len(i) > 3]
print(words, sep = '\n')
print(len(words))