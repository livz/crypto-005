#!/usr/bin/python

#
# Coursera - Cryptography course (crypto-005)
# 
# Week 5 - Problem 5
# 7a + 23b = 1 in Z 23
# (Using Euclid's Extended Algorithm
# 

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

if __name__ == "__main__":
	print modinv(7, 23)        
