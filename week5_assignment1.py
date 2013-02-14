#!/usr/bin/python

#
# Coursera - Cryptography course (crypto-005)
# 
# Week 5 - Assignment 1
# 
# Computing discrete log modulo a big prime p, using meet-in-the-middle method
# Install gmpy2: https://gmpy2.readthedocs.org/en/latest/intro.html
# Docs: https://gmpy2.readthedocs.org/en/latest/mpz.html#mpz-functions
#

import gmpy2
import sys
from gmpy2 import mpz

p = "134078079299425970995740249982058461274793658205923933" + \
    "77723561443721764030073546976801874298166903427690031" + \
    "858186486050853753882811946569946433649006084171"
g = "11717829880366207009516117596335367088558084999998952205" + \
	 "59997945906392949973658374667057217647146031292859482967" + \
    "5428279466566527115212748467589894601965568"
h = "323947510405045044356526437872806578864909752095244" + \
	 "952783479245297198197614329255807385693795855318053" + \
    "2878928001494706097394108577585732452307673444020333"


B = gmpy2.mpz(2)**gmpy2.mpz(20)+1 # B = 2^20

hash_table = {}		# dictionary

for x1 in range(0, B):
	# compute left side
	neg_x1 = gmpy2.mpz(x1) * -1	# -x1
	g_x1_inv = gmpy2.powmod(gmpy2.mpz(g), gmpy2.mpz(neg_x1), gmpy2.mpz(p)) # 1/(g^x1) mod p
	left = gmpy2.mpz(h) * gmpy2.mpz(g_x1_inv) 	# h/(g^x1)
	left = gmpy2.f_mod(gmpy2.mpz(left), gmpy2.mpz(p))
 
	# add values to a hash
	hash_table[left] = gmpy2.mpz(x1)

	#print "x1", x1, B

# match with the right side
g_B = gmpy2.powmod(gmpy2.mpz(g), gmpy2.mpz(B), gmpy2.mpz(p)) # g^B mod p

for x0 in range(0, B):
	right = gmpy2.powmod(gmpy2.mpz(g_B), gmpy2.mpz(x0), gmpy2.mpz(p)) # (g^B)^x0 mod p
	if right in hash_table:
		print hash_table[right]		# x1
		print x0
		x = gmpy2.mpz(x0)*gmpy2.mpz(B) + hash_table[right] 	# X = x0*B + x1
		print "Solution to discrete log problem is: " , x
		sys.exit()
	#print "x0", x0, B
	
