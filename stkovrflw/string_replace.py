# https://stackoverflow.com/questions/54493854/program-to-iteratively-remove-consecutive-characters-which-come-just-one-after-a

def get_string(s):
	l = len(s)
	i = 0

	count = 0
	while s and i < (len(s) - 1):
		start = i
		end = i
		found = False

		while i < (len(s) -1) and s[i].isalpha() and s[i].isalpha() and ((ord(s[i]) + 1) == ord(s[i + 1])):
			count += 1
			found = True
			end += 1
			i += 1

		if found:
			s = s[:start] + s[end + 1:]
			i = end + 1
		else:
			i += 1

	if count:
		return get_string(s)

	return s

print(get_string('axefyzijkmoq'))