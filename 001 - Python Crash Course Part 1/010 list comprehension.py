#!/usr/bin/env python3

# Wankyu Choi (c) 2014
# For Creative Works of Knowledge Python Training

# list comprehension

def main():
	"""program entry point
	"""

	years_to_print = [ str(y) for y  in range(1800, 2014, 1) ]

	print(years_to_print)
	print("\n\n")
	print(" ".join(years_to_print))
	print("=".join(years_to_print))
	print("\t".join(years_to_print))

if __name__ == '__main__': main()