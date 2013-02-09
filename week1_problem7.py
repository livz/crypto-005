#!/usr/bin/python

#
# Coursera - Cryptography course (crypto-005)
# 
# Week 1 - problem 7
#

def strxor(a, b):     # xor two strings of different lengths
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


# Question 7 solution
m1 = "attack at dawn" 
c1 = "09e1c5f70a65ac519458e7e53f36"
k1 = strxor(m1, c1.decode('hex'))
print k1
m2 = "attack at dusk"
c2 = strxor(m2, k1)
print c2.encode('hex')
