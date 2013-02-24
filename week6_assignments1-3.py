#!/usr/bin/python

#
# Coursera - Cryptography course (crypto-005)
# 
# Week 6 - Assignments 1-3
# 
# Break RSA when the public modulus N is generated incorrectly.
#

import gmpy2
import sys
from gmpy2 import mpz

# Challenge 1
N1= "17976931348623159077293051907890247336179769789423065727343008115" + \
    "77326758055056206869853794492129829595855013875371640157101398586" + \
    "47833778606925583497541085196591615128057575940752635007475935288" + \
    "71082364994994077189561705436114947486504671101510156394068052754" + \
    "0071584560878577663743040086340742855278549092581"

(A, dif) = gmpy2.isqrt_rem(gmpy2.mpz(N1))
A = A + 1
delta = gmpy2.mpz(A)**2 - gmpy2.mpz(N1)
(x, dif) = gmpy2.isqrt_rem(delta)
(p, q) = (A - x, A + x)
print "Challenge 1 solution: ", min(p,q)

# Challenge 2
N2 = "6484558428080716696628242653467722787263437207069762630604390703787" + \
     "9730861808111646271401527606141756919558732184025452065542490671989" + \
     "2428844841839353281972988531310511738648965962582821502504990264452" + \
     "1008852816733037111422964210278402893076574586452336833570778346897" + \
     "15838646088239640236866252211790085787877"
     
A = gmpy2.isqrt(gmpy2.mpz(N2))
A = A + 1  # ceil round
while(True):
	delta = gmpy2.mpz(A)**2 - gmpy2.mpz(N2)
	x = gmpy2.isqrt(delta)
	(p, q) = (A - x, A + x)
	tmp = gmpy2.mpz(N2) - p*q
	if (tmp == 0):
		print "Challenge 2 solution: ",  min(p,q)
		break
	A = A + 1
	
# Challenge 3
N3 = "72006226374735042527956443552558373833808445147399984182665305798191" + \
     "63556901883377904234086641876639384851752649940178970835240791356868" + \
     "77441155132015188279331812309091996246361896836573643119174094961348" + \
     "52463970788523879939683923036467667022162701835329944324119217381272" + \
     "9276147530748597302192751375739387929"
N3 = gmpy2.mpz(N3)

A = gmpy2.isqrt(6*N3)
# We don't use ceil on sqrt(6N), as A is not an integer
# But 2A is, so we use 2*A i nall computations!!
# 2*A = 2sqrt(6N) + 1
AA = 2*A+1

# 3p + 2q = 2A (A is odd)
# |3p - 2q| = sqrt(4A^2-24N)

# Test to see we got a perect square
(res, rem) = gmpy2.isqrt_rem(AA**2-24*N3)
#print rem # 0

# Test the reminder in both cases. One should be 0
(p, rem1) = gmpy2.c_divmod(res + AA, 4)
(q, rem2) = gmpy2.c_divmod(res - AA, 6)

if(rem != 0) or (rem2 != 0):
	(p, rem1) = gmpy2.c_divmod(res - AA, 4)
	(q, rem2) = gmpy2.c_divmod(res + AA, 6)

if (abs(p*q) == N3):
	print "Challenge 3 solution: ", min(abs(p), abs(q))
