file = open("mem.coe", "w")
file.write("memory_initialization_radix = 16;\n")
file.write("memory_initialization_vector = \n")

count = 0

try:
    f = open("MyDriver.rom", "rb")
    b = f.read(0)
    str = ""
    while True:
        b = f.read(1)
        if b == b'':
            break
        str += b.hex()
    f.close()
except IOError:
    print('error')

i = 7
print(len(str))
for item in str:
    file.write(str[i-1])
    file.write(str[i])
    file.write(str[i-3])
    file.write(str[i-2])
    file.write(str[i-5])
    file.write(str[i-4])
    file.write(str[i-7])
    file.write(str[i-6])
    if i == len(str)-1:
        file.write(';')
    else:
        file.write(',\n')
    i = i + 8
    if i >= len(str):
        break
file.close()
f.close()