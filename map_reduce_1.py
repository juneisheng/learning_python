def normalize(name):
	caplow = {
	'A':'a', 'B':'b', 'C':'c', 'D':'d',
	'E':'e', 'F':'f', 'G':'g', 'H':'h',
	'I':'i', 'J':'j', 'K':'k', 'L':'l',
	'M':'m', 'N':'n', 'O':'o', 'P':'p',
	'Q':'q', 'R':'r', 'S':'s', 'T':'t', 
	'U':'u', 'V':'v', 'W':'w', 'X':'x',
	'Y':'y', 'Z':'z'
	}
	lowcap = {k:v for v,k in caplow.items()}
	L = []
	
	for i in range(len(name)):
		if i == 0:
			if name[0] == 'a' or name[0] == 'b' or name[0] == 'l':
				L.append(lowcap.get(name[0]))
			else:
				L.append(name[0])
		else:
			if name[i] == 'A' or name[i] == 'L' or name[i] == 'I' or name[i] == 'S' or name[i] == 'T':
				L.append(caplow.get(name[i]))
			else:
				L.append(name[i])
	return ''.join(L)
			
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)