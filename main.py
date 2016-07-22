import sys
#created by zahiruddinnorzain email:kepaknaga@gmail.com [22-july-2016][4:44PM]


def testOverInput(test1):
    if test1 >= 12:
        print('ERROR\nThere are no chord number 12 or above')
        return sys.exit()

    elif test1 <0:
        print('ERROR\nThere are no chord number below than 0')
        return sys.exit()
    
#MAIN    

keyall = ['A ','A#','B ','C ','C#','D ','D#','E ','F ','F#','G ','G#','A ','A#','B ','C ','C#','D ','D#','E ','F ','F#','G ','G#']

keyalln = ['0 =A','1 =A#','2 =B','3 =C','4 =C#','5 =D','6 =D#','7 =E','8 =F','9 =F#','10=G','11=G#']


for k in keyalln :  #soalan
	print(k)


# mula bagi starting key

keymula = input('\nstarting key?= ')  #input jawapan
nomborMulaKey = int(keymula)
    
testOverInput(keymula)  #Fix over input


#print(nomborMulaKey) #nombor array key starting


keymula1 = keyall[nomborMulaKey]

print('\nYour first key = ' + keymula1) #key mula bagi starting


maxnokey=nomborMulaKey+12

keyAkhir1 = keyall[maxnokey] #key akhir bagi starting

#print(keyAkhir1)




#mula bagi shift key

keyshift = input('\nshift key to?= ')
nomborShiftKey = int(keyshift)

testOverInput(keyshift)  #Fix over input

#print(nomborShiftKey) #nombor array key shift
print('\nYour shift key = ' + keyall[nomborShiftKey])

tolak = nomborShiftKey - nomborMulaKey
bezaKey=int(tolak)

print('\nDiffrence key = ' + str(bezaKey))  #beza key awal dan shift



print("\n=========ANSWERS=========")

print('\nOriginal = shift\n')

keycalc = nomborMulaKey+bezaKey #key mula tambah nilai nak shift
keycalcEnd = maxnokey+bezaKey   #key akhir tambah nilai nak shift utk dpt nilai akhir baru

while keycalc <= (keycalcEnd-1) : #ni untuk output tapi tak siap lagi

    print(keyall[nomborMulaKey] + ' = ' + keyall[keycalc])          #ini shift key
    keycalc += 1
    nomborMulaKey += 1

    

