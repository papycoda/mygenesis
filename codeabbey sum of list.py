data = '1206 301 64 412 382 1162 780 362 804 226 1115 1204 709 291 1044 938 568 247 763 51 945 825 857 576 392 340 1053 1101 1183 1086 189 1089 86 244 201 459'
datum = data.replace(" ", ",")

print(datum)
cad = eval('[' + datum + ']')

summ = 0
for i in cad:
    summ += i

print(summ)
