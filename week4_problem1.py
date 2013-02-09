#!/usr/bin/python

#
# Coursera - Cryptography course (crypto-005)
# 
# Week 4 - Problem 1
# CBC provides no integrity!
# 

def strxor(a, b):     # xor two strings of different lengths
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

cypher_text = "20814804c1767293b99f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d"
hex_ct = cypher_text.decode('hex')


pt = "Pay Bob 100$\x00\x00\x00\x00"
new_pt = "Pay Bob 500$\x00\x00\x00\x00"

iv = hex_ct[:16]
new_iv = strxor(iv, pt)
new_iv = strxor(new_iv, new_pt)

print new_iv.encode('hex'), hex_ct[16:].encode('hex')
print iv.encode('hex'), hex_ct[16:].encode('hex')

