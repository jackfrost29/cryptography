import array

def bitwise_xor_match(s1, s2, arr):
    ar1 = s1.encode()
    ar2 = s2.encode()
    xor = bytearray(8)
    for i in range(8):
        xor[i] = ar1[i] ^ ar2[i]
    for i in range(8):
        if xor[i] != arr[i]:
            return False
    return True


byte1 = 'e9 3a e9 c5 fc 73 55 d5'.replace(' ', '')
byte2 = 'f4 3a fe c7 e1 68 4a df'.replace(' ', '')

c1 = bytearray.fromhex(byte1)
c2 = bytearray.fromhex(byte2)
c1_xor_c2 = bytearray(8)
for i in range(8):
    c1_xor_c2[i] = c1[i] ^ c2[i]



# a = array.array('B', 'ABCD')
# print(a)

word_list = []
with open('/usr/share/dict/words', 'r') as f:
    word_list = f.read().split('\n')


word_list = [i for i in word_list if len(i) == 8]

# x = 'Python'.encode()
# for a in x:
#     print (a)


for m1 in word_list:
    for m2 in word_list:
        if m1 != m2 and bitwise_xor_match(m1, m2, c1_xor_c2):
            print(m1)
            print(m2)
            break