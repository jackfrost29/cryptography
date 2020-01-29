from functools import reduce
import collections

def factors(n):    
    return list(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

with open('char_freq.txt', 'r') as f:
    temp = f.readline().replace('\n', '').split(',')
    char_list = f.readline().replace('\'', '').split(',')
    freq_list = [float(i) for i in temp]
    temp_dic = dict(zip(char_list, freq_list))
    char_freq = {k: v for k, v in sorted(temp_dic.items(), key=lambda item: item[1])}
    print(char_freq)