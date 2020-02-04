'''
decryption without key is implemented for case insensitive cypher.
Because there are no existing character relative frequency statistical
data on the internet for case sensitive cypher.
'''

from functools import reduce
import operator
import collections
import math
import re


def gen_per(dic, eng_char_freq):
    # get the number of characters map for a particular position
    # dic -> cypher freq
    # eng_char_freq -> original english frequency
    # both are sorted
    # print(type(dic))
    
    map_from = (list(dic.keys()))[0]
    map_to = (list(eng_char_freq.keys()))[0]
    key = '' + chr( ( ( ord(map_from) - ord(map_to) ) % 26) + ord('a'))
    __list = list(dic)
    for k in dic:
        if k != map_from and abs(dic[k] - dic[map_from]) <= 0.01:
            key = key + chr( ( ( ord(k) - ord(map_to) ) % 26) + ord('a'))
    
    return key




def get_permutated_keys(lst, string):
    # print(lst, string)
    new_list = []
    for s in lst:
        for i in range(0, len(string)):
            new_list.append(s + string[i])
        lst = new_list
    return lst


def decrypt_and_write(f, key):
    l = len(key)
    
    temp = 'decryption for key: ' + key + '\n\n'
    f.write(temp)
    for i in range(0, cypher_len):
        x = ord(cypher[i]) - ord('a')
        y = ord(key[i % l]) - ord('a')
        z = ((x - y) % 26) + ord('a')
        f.write(chr(z))
        if ((i+1) % 5) == 0:
            f.write(' ')
        if((i+1) % 50) == 0:
            f.write('\n')
    f.write('\n')


def KMP_String(pattern, text):
    a = len(text)
    b = len(pattern)

    prefix_arr = get_prefix_arr(pattern, b)

    initial_point = []

    m = 0
    n = 0

    while m != a:

        if text[m] == pattern[n]:
            m += 1
            n += 1

        else:
            n = prefix_arr[n-1]

        if n == b:
            initial_point.append(m-n)
            n = prefix_arr[n-1]
        elif n == 0:
            m += 1

    return initial_point

def get_prefix_arr(pattern, b):
    prefix_arr = [0] * b
    n = 0
    m = 1

    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
            n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1

    return prefix_arr


'''
string = "ABABDABACDABABCABABCABAB"
pat = "ABABCABAB"

initial_index = KMP_String(pat, string)

for i in initial_index:
    print('Pattern is found in the string at index number',i)
'''

def __factors(n):
    s = set(reduce(list.__add__,
                   ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    s.discard(1)
    s.discard(2)
    return s

def difference(_list):   # list of differences
    ret = []
    for a in _list:
        for b in _list:
            if a != b:
                ret.append(abs(a-b))
    return ret

def generate_keys(message, n):  # generate possible keys of length n from message
    len_mes = len(message)
    char_freq = {}      # english alphabet statistical frequency
    with open('char_freq.txt', 'r') as f:
        temp = f.readline().replace('\n', '').split(',')
        char_list = f.readline().replace('\'', '').split(',')
        freq_list = [float(i) for i in temp]
        temp_dic = dict(zip(char_list, freq_list))
        char_freq = {k: v for k, v in sorted(temp_dic.items(), key=lambda item: item[1], reverse=True)}
    
    sample_freq = []    # frequency of the sample taking approx len
    for i in range(0, n):
        sample_freq.append({})
        for j in range(0, 26):
            sample_freq[i][chr(j+ord('a'))] = 0.


    for i in range(0, len_mes):  # number of chars at monoalphabatic positions
        sample_freq[i % n][cypher[i]] += 1


    for i in range(0, n):
        for j in range(0, 26):
            sample_freq[i][chr(j+ord('a'))] /= (math.floor((len_mes+n-i-1)/n))
            
    # Now every monoalpha pos has the relative freq count inside sample_freq
    # Now we have to sort it

    for i in range(0, n):
        sample_freq[i] = {k: v for k, v in sorted(sample_freq[i].items(), key=lambda item: item[1], reverse=True)}

    keys = ['']
    # print(sample_freq[0])
    for i in range(0, n):
        per = gen_per(sample_freq[i], char_freq)
        keys = get_permutated_keys(keys, per)
    #print(keys)
    return keys


####################      IOC       ###################

cypher = None
IC_english = 0.0667

with open('cypher_case_insensitive.txt', 'r') as f:
    cypher = f.read()

cypher_len = len(cypher)
IOC = {}
freq_count = []

for gues_len in range(2, int(cypher_len/2)):

    for i in range(gues_len):
        freq_count.append({})
        for j in range(26):
            freq_count[i][chr(j+ord('a'))] = 0.
    for i in range(cypher_len):
        freq_count[i%gues_len][cypher[i]] += 1

    for i in range(gues_len):
        for j in range(26):
            freq_count[i][chr(j+ord('a'))] /= (math.floor((cypher_len+gues_len-i-1)/gues_len))

    IOC_temp = [0. for i in range(gues_len)]
    for i in range(gues_len):
        nm = 0.
        for key in freq_count[i]:
            if freq_count[i][key] != 0:
                freq_count[i][key] *= (freq_count[i][key]-1)
            nm += freq_count[i][key]
        c = (math.floor((cypher_len+gues_len-i-1)/gues_len))
        IOC_temp[i] += (nm / (c * (c-1)) - IC_english)
    
    tmp = .0
    for i in range(gues_len):
        tmp += IOC_temp[i]
    IOC[gues_len] = tmp / gues_len

####################       IOC       ####################




'''
####################       N-GRAMS       ####################

factors = {}
already_checked = set()

for sub_str_len in range(2, 6):
    for i in range(0, cypher_len-sub_str_len):
        x = cypher[i:i+sub_str_len]
        if x not in already_checked:
            already_checked.add(x)
            l = [m.start() for m in re.finditer(x, cypher)]
            diffs = difference(l)
            for d in diffs:
                facts = __factors(d)
                for f in facts:
                    if f not in factors:
                        factors[f] = 1
                    else:
                        factors[f] += 1

####################       N-GRAMS       ####################




####################       Key Length       ####################

max_key = 0
for f in factors:
    if max_key == 0:
        max_key = f
        min_val = factors[f]
    elif (factors[f] == factors[max_key] and f > max_key) or (factors[f] > factors[max_key]):
        # then update
        max_key = f

key_len_list = []
for f in factors:
    if (float(factors[f]) / factors[max_key]) >= 0.8:
        key_len_list.append(f)

#print(key_len_list)

factors = {k: v for k, v in sorted(factors.items(), key=lambda item: item[1], reverse=True)}
# print(type(factors))


pos_key_len = 0
for temp in key_len_list:
    if pos_key_len == 0:
        pos_key_len = temp
    elif IOC[temp] < IOC[pos_key_len]:
        pos_key_len = temp
####################       Key Length       ####################
'''



pos_key_len = IOC[min(IOC.keys(), key=(lambda k: IOC[k]))]


keys = generate_keys(cypher, pos_key_len)
print(pos_key_len)

with open('decode_without_key.txt', 'w+') as f:
    for key in keys:
        decrypt_and_write(f, key)


'''


approx_key_len = min(IOC.items(), key=operator.itemgetter(1))[0]

# now find out the stats with this key len

sample_freq = []    # frequency of the sample taking approx len

for i in range(0, approx_key_len):
    sample_freq.append({})
    for j in range(0, 26):
        sample_freq[i] [chr(j+ord('a'))] = 0.

for i in range(0, cypher_len): # number of chars at monoalphabatic positions
    sample_freq[i%approx_key_len] [cypher[i]] += 1


for i in range(0, approx_key_len):
    for j in range(0, 26):
        sample_freq[i] [chr(j+ord('a'))] /= (math.floor((cypher_len+approx_key_len-i-1)/approx_key_len))

# Now every monoalpha pos has the relative freq count inside sample_freq
# Now we have to sort it

for i in range(0, approx_key_len):
    sample_freq[i] = {k: v for k, v in sorted(sample_freq[i].items(), key=lambda item: item[1], reverse=True)}

char_freq = {}      # english alphabet statistical frequency

with open('char_freq.txt', 'r') as f:
    temp = f.readline().replace('\n', '').split(',')
    char_list = f.readline().replace('\'', '').split(',')
    freq_list = [float(i) for i in temp]
    temp_dic = dict(zip(char_list, freq_list))
    char_freq = {k: v for k, v in sorted(temp_dic.items(), key=lambda item: item[1], reverse=True)}

keys = []
keys.append(str(''))
for i in range(0, approx_key_len):
    per = gen_per(sample_freq[i])
    keys = get_permutated_keys(keys, per)

print(approx_key_len)

for key in keys:
    decrypt_and_write(key)
'''
