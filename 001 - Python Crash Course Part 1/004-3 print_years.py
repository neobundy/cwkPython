#!/usr/bin/env python3

# Wankyu Choi (c) 2014
# For Creative Works of Knowledge Python Training

# format string

def print_years(start, end, step=1, per_line=10):

	year = start
	count = 1
	for year in range(start, end+1, step):
		end_char = "\n" if count % per_line == 0 else "\t"
		print(year, end=end_char)

		count += 1

	print("\n\n")
	print("{} year(s) printed.".format(count-1))
	print("{0} year(s) printed: from {1} to {2}".format(count-1, start, end))
	print("{num} year(s) printed: from {start} to {end}".format(num=count-1, start=start, end=end))


def main():
	"""program entry point
	"""
	
	print_years(1800, 2014, step=3, per_line=5)


if __name__ == '__main__': main()