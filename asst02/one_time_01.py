import array

def bitwise_xor_match(s1, s2, arr):
    return



byte1 = 'e9 3a e9 c5 fc 73 55 d5'.replace(' ', '')
byte2 = 'f4 3a fe c7 e1 68 4a df'.replace(' ', '')

c1 = bytearray.fromhex(byte1)
c2 = bytearray.fromhex(byte2)



# a = array.array('B', 'ABCD')
# print(a)

word_list = []
with open('/usr/share/dict/words', 'r') as f:
    word_list = f.read().split('\n')
# print(word_list)

# for l in word_list:
#     if len(l) != 8:
#         word_list.remove(l)

print(len(word_list))

temp = [elem.encode("hex") for elem in 'ABC']

'''
for m1 in word_list:
    for m2 in word_list:
        if m1 != m2 and 

'''