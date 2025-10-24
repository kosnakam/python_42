import sys

try:
	assert len(sys.argv) <= 2, "more than one argument is provided"

	if len(sys.argv) <= 1:
		sys.exit()

	num = int(sys.argv[1])
	if num % 2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")

except AssertionError as e:
	print(f"AssertionError: {e}")
except ValueError:
	print("AssertionError: argument is not an integer")