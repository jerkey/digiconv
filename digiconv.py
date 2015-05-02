#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys

#  0 Datasheets                         "http://www.cooperindustries.com/content/dam/public/bussmann/Electronics/Resources/product-datasheets/Bus_Elx_DS_4308_PM_Series.pdf",
#  1 Image                              "http://media.digikey.com/Photos/Cooper%20Bussmann%20Photos/PM-5R0H474-R.JPG",
#  2 Digi-Key Part Number               "283-4004-ND",
#  3 Manufacturer Part Number           "PM-5R0H474-R",
#  4 Manufacturer                       "Eaton Bussmann",
#  5 Description                        "CAP 470MF -20% +80% 5V T/H",
#  6 Quantity Available                 42,
#  7 Factory Stock                      0,
#  8 Unit Price (USD)                   "7.31000",
#  9 @ qty                              0,
# 10 Minimum Quantity                   1,
# 11 Packaging                          "Bulk",
# 12 Series                             "PowerStor® PM",
# 13 Capacitance                        "470mF",
# 14 Tolerance                          "-20%, +80%",
# 15 Voltage - Rated                    "5V",
# 16 ESR (Equivalent Series Resistance) "500 mOhm",
# 17 Lifetime @ Temp.                   "1000 Hrs @ 60°C",
# 18 Termination                        "-",
# 19 Mounting Type                      "Through Hole",
# 20 Package / Case                     "Radial, Can, Horizontal",
# 21 Lead Spacing                       "0.465"" (11.80mm)",
# 22 Size / Dimension                   "0.571"" L x 0.681"" W (14.50mm x 17.30mm)",
# 23 Height - Seated (Max)              "0.354"" (9.00mm)",
# 24 Operating Temperature              "-40°C ~ 60°C"

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

def normalize_voltage(s):
    if s[-1] != 'V':
        return s
    return s[0:-1]

def normalize_ESR(s):
    if s.find("mOhm") > 0:
        return s.split(" ")[0]
    if s.find("Ohm") > 0:
        return (float(s.split(" ")[0]) * 1000)
    return s

inFile = open('digikeyultracaps500.csv','r')
inRows = csv.reader(inFile, delimiter=',', quotechar='"')
outFile = csv.writer(sys.stdout, delimiter=',', quotechar='"')
for row in inRows:
    dim1 = extract_paren(row[22]).split(" ")[0]
    if len(extract_paren(row[22]).split(" ")) > 2:
        dim2 = extract_paren(row[22]).split(" ")[2]
    else:
        dim2 = dim1
    stuff = ( row[0], row[2], row[3], row[5], row[6], row[8], # row[8] is price
              row[10], normalize_capacitance(row[13]),
              normalize_voltage(row[15]), normalize_ESR(row[16]),
              dim1.split("mm")[0],
              dim2.split("mm")[0],
              extract_paren(row[23].split("mm")[0]) )
    outFile.writerow(stuff)
