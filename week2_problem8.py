#!/usr/bin/python

#
# Coursera - Cryptography course (crypto-005)
# 
# Week 2 - Problem 8
#

msg = ['An enciphering-deciphering machine (in general outline) of my invention has been sent to your organization.', \
	'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.', \
	'The significance of this general conjecture, assuming its truth, is easy to see. It means that it may be feasible to design ciphers that are effectively unbreakable.', \
	'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.',
	'In this letter I make some remarks on a general principle relevant to enciphering in general and my machine.', 
	'To consider the resistance of an enciphering process to being broken we should assume that at same times the enemy knows everything but the key being used and to break it needs only discover the key from this information.',
	'We see immediately that one needs little information to begin to break down the process.']

for m in msg :	
	print m[:20], len(m)
