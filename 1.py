import string

count = 0
with open("1_input.txt") as f:
	for line in f.readlines():
		line_numbers = ""
		for i, c in enumerate(line):
			if c in string.digits:
				line_numbers+=c
			elif line.startswith('one', i):
				line_numbers+='1'
			elif line.startswith('two', i):
				line_numbers+='2'
			elif line.startswith('three', i):
				line_numbers+='3'
			elif line.startswith('four', i):
				line_numbers+='4'
			elif line.startswith('five', i):
				line_numbers+='5'
			elif line.startswith('six', i):
				line_numbers+='6'
			elif line.startswith('seven', i):
				line_numbers+='7'
			elif line.startswith('eight', i):
				line_numbers+='8'
			elif line.startswith('nine', i):
				line_numbers+='9'

		print(line, line_numbers)

		line_num = 0
		for c in line_numbers:
			if c in string.digits:
				line_num = int(c)*10
				break
		for c in reversed(line_numbers):
			if c in string.digits:
				line_num += int(c)
				break
		count += line_num
		print("->", line_num)


print(count)
