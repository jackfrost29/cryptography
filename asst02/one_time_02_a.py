import random

m = 'MyNameIsJo'.encode()
k = bytearray([random.randint(0, 255) for i in range(10)])
c = bytearray(10)
c[0] = m[0] ^ k[0]
# encode
for i in range(1, 10):
    c[i] = m[i] ^ ((k[i] + c[i-1]) % 256)

# print("Encrypted message")
# print(c)

# decrypt the message back now
m_d = bytearray(10)
m_d[0] = k[0] ^ c[0]

for i in  range(1, 10):
    m_d[i] = c[i] ^ ((k[i] + c[i-1]) % 256)

# print(m_d)
message_decrypted = m_d.decode('utf-8')
print(message_decrypted)
