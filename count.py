import sys


str1 = ""
alphabet = digit = special = 0

for line in sys.stdin:
    str1 = line
    for i in range(len(str1)):
        if((str1[i] >= 'a' and str1[i] <= 'z') or (str1[i] >= 'A' and str1[i] <= 'Z')): 
            alphabet = alphabet + 1 
        elif(str1[i] >= '0' and str1[i] <= '9'):
            digit = digit + 1
        else:
            special = special + 1

sys.stdout.write("Total angka: " + str(digit))
sys.stdout.write('\n')
sys.stdout.write("Total huruf: " + str(alphabet))
sys.stdout.write('\n')
sys.stdout.write("Total symbol: " + str(special))
sys.stdout.write('\n')
