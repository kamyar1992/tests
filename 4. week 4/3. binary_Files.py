with open('sampleBinary', 'bw') as bf:
    bf.write(bytes(3))
with open('sampleBinary', 'bw') as bf:
    bf.write(bytes(range(17)))

with open('sampleBinary', 'br') as binary_file:
    for num in binary_file:
        print(num)

# writing numbers in a binary file
# each two hex is one byte

a = 65534       # 0x FF FE
b = 65535       # 0x FF FE
c = 65536       # 0x 00 01 00 00
d = 655364      # 0x 00 0A 00 04

with open('sampleBinary','bw') as binary_file:
    binary_file.write(a.to_bytes(2, 'big'))
    binary_file.write(b.to_bytes(2, 'big'))
    binary_file.write(c.to_bytes(4, 'big'))
    binary_file.write(d.to_bytes(4, 'big'))
    binary_file.write(d.to_bytes(4, 'little'))
with open('sampleBinary', 'br') as binary_file:
    new_a = int.from_bytes(binary_file.read(2),'big')
    new_b = int.from_bytes(binary_file.read(2),'big')
    new_c = int.from_bytes(binary_file.read(4),'big')
    new_d = int.from_bytes(binary_file.read(4),'big')
    new_d_wrong = int.from_bytes(binary_file.read(4),'big')

print(new_a)
print(new_b)
print(new_c)
print(new_d)
print(new_d_wrong)


