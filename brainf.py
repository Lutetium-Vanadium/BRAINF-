# it prints out all viables at every loop and outputs to an output text file
debug = False


# prints to console or text file based on debug
def out(string="", string2="", end="\n"):
	if debug:
		with open("output.txt", "a+") as f:
			f.write(str(string) + str(string2) + end)
	else:
		print(str(string) + str(string2), end=end)

def interpret(arg, arg_type):
	if arg_type == "file":
		with open(arg, "r") as file:
			s = file.read().replace("\n", "")
	elif arg_type == "string":
		s = arg

	# the memory array
	mem = [0]

	# open_n and close_n count the number of brackets while in a loop
	open_n = close_n = 0
	
	# mem_loc is the current location in the memory and i is the letter in the program
	i = mem_loc = 0

	# back and skip control skipping of blocks or returning to open bracket
	back = skip = False

	while -len(s) <= i < len(s):
		char = s[i]

		if skip:
			if char == "[":
				open_n += 1
			elif open_n == 0 and s[i+1] == "]":
				if mem[mem_loc] != 0:
					back = True
				skip = False
				open_n = 0
			i += 1
			continue

		elif back:
			if char == "]":
				close_n += 1
			elif close_n == 1 and s[i-1] == "[":
				back = False
				close_n = 0
			i -= 1
			continue

		elif char == "[" and mem[mem_loc] == 0:
			skip = True

		elif char == "]" and mem[mem_loc] != 0:
			back = True		

		if char == "<":
			mem_loc -= 1
		elif char == ">":
			mem_loc += 1
			while mem_loc >= len(mem):
				mem.append(0)
		elif char == "+":
			mem[mem_loc] += 1
		elif char == "-":
			mem[mem_loc] -= 1
		elif char == ".":
			out(chr(mem[mem_loc]), end="")
		elif char == ",":
			inp = input("[INPUT]: " if debug else "")
			if debug: out(inp[-1])
			mem[mem_loc] = ord(inp[-1])
		elif char == "*":
			mem[mem_loc] -= 48
		elif char == "^":
			mem[mem_loc] += 48
		elif char == ";":
			out()

		if debug and mem[mem_loc] > 100:
			return 

		if debug: print(f"char: {char}, mem: {mem}, mem_loc: {mem_loc}, skip: {skip}, back: {back}, i: {i}, open_n: {open_n}, close_n: {close_n}")

		i += 1


def brainf(arg, arg_type):
	'''
	POSSIBLE Arg types are "file" and "string" these change how the bf program is read from arg

	arg_type == "file": arg must be a string which has the file name with the extension (can be any type of file though)
	arg_type == "string": arg must be the program you wish to run in a string

	LEGAL LETTERS:
		< --previous memory address
		> --next memory address
		+ --adds one to the memory address
		- --subtracts one from the memory address
		[ --if current memory address is non-zero executes block, else skips to the closing bracket
		] --if current memory address is non-zero goes to opening bracket and executes the block, else continues with the rest of the program
		* --subtracts 48(ascii value of 0) to the current memory address
		^ --adds 48 to the current memory address
		. --outputs the ascii value of the current memory address
		, --inputs one char and converts it from ascii to int and stores in current memory address NOTE: if multiple characters are given only last one will be taken
		; --goes to next line

		NOTE: Any non legal letters will not throw and error, they will simply be ignored
	'''


	if debug: 
		with open("output.txt", "w") as f:
			f.write("")

	out("start")
	interpret(arg, arg_type)
	out("done")