


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

def __get(dic, value):
    for a, b in dic.items():
        if b == value:
            return a
    return '-1'



plain = None
key = None
cypher = None
with open('plain.txt', 'r') as f1, open('key.txt', 'r') as f2:
    plain = f1.read()
    key = f2.read()


plain = ''.join([i if (ord(i) <= ord('z') and ord(i) >= ord('a')) or \
                        (ord(i) >= ord('A') and ord(i) <= ord('Z')) else '' for i in plain])

plain_case_insensitive = plain.lower()

char_set_map = initMap()


with open('cypher.txt', 'w+') as f3:
    for i in range(0, len(plain)):
        x = char_set_map.get(plain[i])
        y = char_set_map.get(key[i%len(key)])
        z = (x + y) % len(char_set_map)
        f3.write(__get(char_set_map, z))
        if (i+1)%5 == 0:
            f3.write('\n')

with open('cypher.txt', 'r') as f1:
    cypher = f1.read().replace('\n', '')
    
with open('decoded.txt', 'w+') as f:
    for i in range(0, len(cypher)):
        x = char_set_map.get(cypher[i])
        y = char_set_map.get(key[i%len(key)])
        z = (x - y) % len(char_set_map)
        f.write(__get(char_set_map, z))

with open('cypher_case_insensitive.txt', 'w+') as f:
    for i in range(0, len(plain_case_insensitive)):
        x = ord(plain_case_insensitive[i]) - ord('a')
        y = ord(key[i%len(key)]) - ord('a')
        z = ((x+y)%26) + ord('a')
        f.write(chr(z))
        