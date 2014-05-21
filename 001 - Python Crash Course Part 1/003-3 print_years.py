#!/usr/bin/env python3

# Wankyu Choi (c) 2014
# For Creative Works of Knowledge Python Training

# for loop and iterators: custom iterator 

def my_year_range(start, end, step=1):
	"""
		iterator should yield resulting value
	"""
	result = start
	while result < end:
		yield result
		result += step

def my_year_range_with_bug(start, end, step=1):
	"""
		return breaks the code
	"""
	result = start
	while result < end:
		return result

		# the following line will never run
		result += step


def main():
	"""program entry point
	"""
	
	start = 1800
	end = 2014
	step = 1
	per_line = 10

	year = start
	count = 1
	for year in my_year_range(start, end+1):
		end_char = "\n" if count % per_line == 0 else "\t"
		print(year, end=end_char)

		year += step
		count += 1

if __name__ == '__main__': main()