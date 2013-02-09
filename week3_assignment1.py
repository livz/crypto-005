#!/usr/bin/python

#
# Coursera - Cryptography course (crypto-005)
# 
# Week 3 - Assignment 1
# Chained blocks hashing 
#

from Crypto.Hash import SHA256

# Split a file into smaller chunks
def splitFile(inputFile, chunkSize):

	#read the contents of the file
	f = open(inputFile, 'rb')
	data = f.read() # read the entire content of the file
	f.close()

	# get the length of data, ie size of the input file in bytes
	bytes = len(data)

	chunks = []
	for i in range(0, bytes+1, chunkSize):
		chunks.append(data[i: i+chunkSize])
	
	return chunks

# Hash a file using the specified hash chaining algorithm
def chain_hash(inFile):
	chunkSize = 1024 # 1 KB

	current_hash = ''
	chunks = splitFile(inFile, chunkSize)
	for i in range(len(chunks)-1, -1, -1):
		sha = SHA256.new(chunks[i])

		chunks[i] = chunks[i] + current_hash
	
		sha = SHA256.new(chunks[i])
		current_hash = sha.digest()
		
	return current_hash.encode('hex')


if __name__ == "__main__":
	target_file = "6 - 1 - Introduction (11 min).mp4"
	test_file = "6 - 2 - Generic birthday attack (16 min).mp4"

	print "Chain hash for %s is:\n %s" % (test_file, chain_hash(test_file))

	print "Chain hash for %s is:\n %s" % (target_file, chain_hash(target_file))
