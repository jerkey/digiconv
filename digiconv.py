import csv
import sys

#
# entries
#
# 0 URL
# 2 ?
# 3 ?
# 5
# 8 ?
# 10
# 13 Capacitance
# 15 (5V)
# 16 (300 mOhm)
# 21
# 22
# 23

def extract_paren(s):
    start = s.find('(')
    stop = s.find(')')
    return s[start+1:stop]

def normalize_capacitance(s):
    if s[-1] != 'F':
        return s
    if s[-2] == 'm':
        return "%.3f" % (float(s[0:-2]) * 0.001)
    return s[0:-1]

f = open('digikey.csv','r')
r = csv.reader(f, delimiter=',', quotechar='"')
w = csv.writer(sys.stdout, delimiter=',', quotechar='"')
for row in r:
    out = ""
    idx = 0
    stuff = ( row[0], row[2], row[3], row[5],
              row[8], row[10], normalize_capacitance(row[13]),
              row[15], row[16], extract_paren(row[21]),
              extract_paren(row[22]), extract_paren(row[23]) )
    w.writerow(stuff)
            

