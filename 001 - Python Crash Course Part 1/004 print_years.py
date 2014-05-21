#!/usr/bin/env python3

# Wankyu Choi (c) 2014
# For Creative Works of Knowledge Python Training

# defining functions, arguments, etc

def print_years(start, end, step=1, per_line=10):

	year = start
	count = 1
	for year in range(start, end+1):
		end_char = "\n" if count % per_line == 0 else "\t"
		print(year, end=end_char)

		year += step
		count += 1

def main():
	"""program entry point
	"""
	
	print_years(1800, 2014, step=3, per_line=5)


if __name__ == '__main__': main()