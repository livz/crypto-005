#!/usr/bin/python

#
# Coursera - Cryptography course (crypto-005)
# 
# Week 2 - Assignment 1
# AES CBC and CTR  decryption
#

from Crypto.Cipher import AES	

# CBC mode decryption
cbc_key = "140b41b22a29beb4061bda66b6747e14"
cbc_ciphers = ["4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee" +
					 "2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81",
					 "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48" +
					 "e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"]				

for c in cbc_ciphers:
	iv = c.decode('hex')[:16]
	ciphertext = c.decode('hex')[16:]
	
	cipher = AES.new(cbc_key.decode('hex'), AES.MODE_CBC, iv)
	print cipher.decrypt(ciphertext)
	

# Counter mode decryption
ctr_key = "36f18357be4dbd77f050515c73fcf9f2"
ctr_ciphers = ["69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc3" + 
					"88d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329",
					"770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa" +
					"0e311bde9d4e01726d3184c34451"]

class myCounter(object):
	def __init__(self, val):
		self.counter = val
    
	def __call__(self):
		# Increment the internal counter 
		# workaround for few blocks: increment only last byte of the counter
		tmp = self.counter
		self.counter = self.counter[:len(self.counter)-1] + chr(ord(self.counter[len(self.counter)-1]) + 1)

		return tmp
    					
for c in ctr_ciphers:
	iv = c.decode('hex')[:16]
	ciphertext = c.decode('hex')[16:]
	
	ctr = myCounter(iv)
	cipher = AES.new(ctr_key.decode('hex'), AES.MODE_CTR, iv, counter=ctr)
	
	# pad cihertext with '0' 
	if len(ciphertext) % 16 != 0:
		dif = 16 - len(ciphertext) % 16
		ciphertext = ciphertext + '\x00' * dif
		
	print cipher.decrypt(ciphertext)
