import struct

with open("python-logo.png", "rb") as logo_file:
    logo_data = logo_file.read(24)
    print(struct.unpack('>II', logo_data[16:24]))
