stuff = raw_input('> ')

def scan(input):
	words = input.split()
	sent_list = []
	word_list = {'north': 'direction', 'south': 'direction', 'east': 'direction', 'go': 'verb', 'kill': 'verb', 'eat': 'verb', 'the': 'stop', 'in': 'stop', 'of': 'stop', 'bear': 'noun', 'princess': 'noun'}
	for item in words:
		num_test = convert_number(item)
		if num_test:
			sent_list.append(('number', num_test))
		else:
			if word_list.has_key(item):
				sent_list.append((word_list[item], item))
			else:
				sent_list.append(('error', item))
	return sent_list
	
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

sentence = scan(stuff)
