#!/usr/bin/env python3

# Wankyu Choi (c) 2014
# For Creative Works of Knowledge Python Training

# while loop
# python documentation: https://docs.python.org/3/index.html

def main():
	"""program entry point
	"""
	
	start = 1800
	end = 2014

	year = start
	while year <= end:
		print(year)
		year +=1

if __name__ == '__main__': main()