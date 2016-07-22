keyall = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A']

keyalln = ['0 =A','1 =A#','2 =B','3 =C','4 =C#','5 =D','6 =D#','7 =E','8 =F','9 =F#','10=G','11=G#']

#for k in keyall[:12]:
#	print(k)

for k in keyalln :
	print(k)


keymula = input('starting key?= ')
nomborMulaKey = int(keymula)

print(nomborMulaKey)

print(keyall[nomborMulaKey])