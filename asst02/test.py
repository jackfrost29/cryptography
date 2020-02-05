
byte1 = 'e9 3a e9 c5 fc 73 55 d5'.replace(' ', '')
byte2 = 'f4 3a fe c7 e1 68 4a df'.replace(' ', '')

c1 = bytearray.fromhex(byte1)
c2 = bytearray.fromhex(byte2)

xor = bytearray(8)
for i in range(8):
    xor[i] = c1[i] ^ c2[i]

s = ''.join('{:02x}'.format(x) for x in xor)
s = " ".join(s[i:i+2] for i in range(0, len(s), 2))
print(s)

'''
word_list = []
with open('/usr/share/dict/words', 'r') as f:
    word_list = f.read().split('\n')
# print(word_list)

len_list = len(word_list)
for i in range(len_list):
    if len(word_list[i]) != 8:
        del word_list[i]

for a in word_list:
    print(a)

'''

x = ['tanvirss', 'badhon', 'shaon']
x = [i for i in x if len(i) == 8]
print(x)