
# Encode string to binary
z = ''.join(['{:08b}'.format(ord(x.encode('utf-8'))) for x in 'rio'])

# Decode binary string
bytes([int(z[:8], base=2), int(z[8:16], 2), int(z[16:], 2)]).decode('utf-8')
