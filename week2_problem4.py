#!/usr/bin/python

#
# Coursera - Cryptography course (crypto-005)
# 
# Week 2 - Problem 4
#

def strxor(a, b):     # xor two strings of different lengths
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
		
left = [("4af53267", "87a40cfa"), ("7b50baab", "ac343a22"), ("9d1a4f78", "75e5e3ea"), ("290b6e3a", "d6f491c5"), \
			("5f67abaf", "bbe033c0"), ("2d1cfa42", "eea6e3dd"), ("e86d2de2", "1792d21d"), 
			("7c2822eb", "325032a9"), ("9f970f4e", "6068f0b1"), ("5f67abaf", "bbe033c0")]

for p in left:
	print p[0], [c for c in strxor(p[0].decode('hex'), p[1].decode('hex'))]
