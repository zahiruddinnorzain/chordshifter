keyall = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

keyalln = ['0 =A','1 =A#','2 =B','3 =C','4 =C#','5 =D','6 =D#','7 =E','8 =F','9 =F#','10=G','11=G#']

#for k in keyall[:12]:
#	print(k)



for k in keyalln :  #soalan
	print(k)


# mula bagi starting key

keymula = input('starting key?= ')  #input jawapan
nomborMulaKey = int(keymula)

print(nomborMulaKey) #nombor array key starting


keymula1 = keyall[nomborMulaKey]

print(keymula1) #key mula bagi starting


maxnokey=nomborMulaKey+12

keyAkhir1 = keyall[maxnokey] #key akhir bagi starting

print(keyAkhir1)


#mula bagi shift key

keyshift = input('shift key to?= ')
nomborShiftKey = int(keyshift)

print(nomborShiftKey) #nombor array key shift

tolak = nomborShiftKey - nomborMulaKey
bezaKey=int(tolak)

print(bezaKey)  #beza key awal dan shift

print("=========")

keycalc = nomborMulaKey+bezaKey
keycalcEnd = maxnokey+bezaKey

while keycalc <= (keycalcEnd-1) : #ni untuk output tapi tak siap lagi
    print(keyall[keycalc])
    keycalc+= 1


#while keymula1 <= keyAkhir1 : #ni untuk output tapi tak siap lagi
#    print(keyall[keymula1])
#    keymula += 1
    
