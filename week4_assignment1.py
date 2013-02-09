#!/usr/bin/python

#
# Coursera - Cryptography course (crypto-005)
# 
# Week 4 - Assignment 1
# Padding oracle attack on AES CBC encryption cyphertext
#

import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
ct = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd"  + \
	  "4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"

def strxor(a, b):     # xor two strings of same lengths
	return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])

#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
	def query(self, q):
		''' Issue HTTP query with the given argument '''
		target = TARGET + urllib2.quote(q)    # Create query URL
		req = urllib2.Request(target)         # Send HTTP request to server
		try:
			f = urllib2.urlopen(req)          # Wait for response
		except urllib2.HTTPError, e:          
			#print "We got: %d" % e.code       # Print response code
			if e.code == 404:
				 #print 'Good padding!'
				 return True 
			#print 'Bad padding'
			# 403 -> invalid pad
			return False 

block_len = 16 # 16 bytes -> 128 bits		
def decrypt_session_info(secret):	
	po = PaddingOracle()
	
	msg = ""
	
	num_blocks = len(secret)/block_len
	# Start guessing from previous-to-last block 
	for i in range(num_blocks-2, -1, -1):
		block = secret[i*16: (i+1)*16]
		
		# Current guessed byte 
		curr_guess = [chr(0)] * 16
		for j in range(block_len-1, -1, -1):
			print "Guessing msg[%d]..." % (i*16+j)
			curr_pad = [chr(0)] * j + [chr(16-j)] * (16-j)
			#print "Current guess: ", list(curr_guess)
			for guess_byte in range(0, 256):
				curr_guess[j] = chr(guess_byte)
				new_block = strxor(block, "".join(curr_guess))
				new_block = strxor(new_block, curr_pad)
				
				# Convert to list to manipulate immutable string
				tmp_list = list(secret[:(i+2)*16])	# end the request at the current block
				tmp_list[i*16: (i+1)*16] = new_block
				new_ct = "".join(tmp_list).encode('hex')
				
			 	if po.query(new_ct):
			 		print "  [+] msg[%d] = 0x%x. (Block no: %d, byte pos: %d)" % (i*16+j, guess_byte, i, j)
					break
				if (guess_byte ==255):
					print "  [-] Failed to guess msg[%d]." % (i*16+j)
					# Use previous guess if nothing found
					curr_guess[j] = curr_guess[j+1]
		print "[*] Guessed block %d: " % i
		print "".join(curr_guess)
		msg = "".join(curr_guess) + msg
		
	print "Decrypted session info: ", msg
	
if __name__ == "__main__":
	decrypt_session_info(ct.decode('hex'))
