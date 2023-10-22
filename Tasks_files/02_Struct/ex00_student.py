import struct

# распаковка из файла
with open('student.data', 'rb') as student_file:
    student = student_file.read()
    print(struct.unpack_from('10sif', student))
    name, age, avg_score = struct.unpack('10sif', student)
    name = name.decode().rstrip('\x00')
    avg_score = round(avg_score, 2)
# Вывод Ivan 21 8.83

