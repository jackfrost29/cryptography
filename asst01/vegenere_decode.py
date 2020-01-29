
'''
decryption without key is implemented for case insensitive cypher.
Because there are no existing character relative frequency statistical
data on the internet for case sensitive cypher.
'''
from functools import reduce
import operator
import collections

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def initMap():
    dic = {}
    val = 0
    for i in range(ord('A'), ord('Z')+1):
        dic.update({chr(i) : val})
        val += 1
    for i in range(ord('a'), ord('z')+1):
        dic.update({chr(i) : val})
        val += 1
    return dic


cypher = None

with open('cypher_case_insensitive.txt', 'r') as f:
    cypher = f.read()

dic_div = {}
for i in range(2, len(cypher)):
    dic_div[i] = factors(i)

# print(dic_div)

key_length, cypher_length = 2, len(cypher)

key_length_guess = [0 for temp in range(cypher_length)]

while key_length < cypher_length:
    i = 0
    j = i + key_length
    count = 0
    while j < cypher_length:
        if cypher[i] == cypher[j]:
            count += 1
        j += 1
        i += 1
    for temp in dic_div[key_length]:
        key_length_guess[temp] += count
    
    key_length += 1

max = 2
for i in range(3, cypher_length):
    if key_length_guess[i] >= key_length_guess[max]:
        max = i

guess = max

char_freq = {}

with open('char_freq.txt', 'r') as f:
    temp = f.readline().replace('\n', '').split(',')
    char_list = f.readline().replace('\'', '').split(',')
    freq_list = [float(i) for i in temp]
    temp_dic = dict(zip(char_list, freq_list))
    char_freq = {k: v for k, v in sorted(temp_dic.items(), key=lambda item: item[1])}

sample_freq = {}
for i in range(0, 26):
    sample_freq[chr(i+ord('a'))] = 0

for i in range(0, len(cypher)):
    sample_freq[cypher[i]] += 1

for item in sample_freq.keys():
    sample_freq[item] = sample_freq[item] / cypher_length


sample_freq = {k: v for k, v in sorted(sample_freq.items(), key=lambda item: item[1])}

final_map = {}
for a, b in sample_freq, char_freq:
    final_map[a] = b

with open('decode_without_key.txt', 'w+') as f:
    for i in range(0, cypher_length):
        f.write(final_map[cypher[i]])
