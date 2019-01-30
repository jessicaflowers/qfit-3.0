'''
Excited States software: qFit 3.0

Contributors: Saulo H. P. de Oliveira, Gydo van Zundert, and Henry van den Bedem.
Contact: vdbedem@stanford.edu

Copyright (C) 2009-2019 Stanford University
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

This entire text, including the above copyright notice and this permission notice
shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS, CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
'''

BondLengthTable =  {'H': {'H': '0.7380', 'C': '1.0900', 'N': '1.0100', 'O': '0.9600', 'F': '0.9200', 'Cl': '1.2800', 'Br': '1.4100', 'I': '1.6000', 'P': '1.4100', 'S': '1.3400'}, 'C': {'H': '1.0900', 'C': '1.5260', 'N': '1.4700', 'O': '1.4400', 'F': '1.3700', 'Cl': '1.8000', 'Br': '1.9400', 'I': '2.1600', 'P': '1.8300', 'S': '1.8200'}, 'N': {'H': '1.0100', 'C': '1.4700', 'N': '1.4410', 'O': '1.4200', 'F': '1.4200', 'Cl': '1.7500', 'Br': '1.9300', 'I': '2.1200', 'P': '1.7200', 'S': '1.6900'}, 'O': {'H': '0.9600', 'C': '1.4400', 'N': '1.4200', 'O': '1.4600', 'F': '1.4100', 'Cl': '1.7000', 'Br': '1.7900', 'I': '2.1100', 'P': '1.6400', 'S': '1.6500'}, 'F': {'H': '0.9200', 'C': '1.3700', 'N': '1.4200', 'O': '1.4100', 'F': '1.4060', 'P': '1.5000', 'S': '1.5800'}, 'Cl': {'H': '1.2800', 'C': '1.8000', 'N': '1.7500', 'O': '1.7000', 'Cl': '2.0310', 'P': '2.0400', 'S': '2.0300'}, 'Br': {'H': '1.4100', 'C': '1.9400', 'N': '1.9300', 'O': '1.7900', 'Br': '2.3370', 'P': '2.2400', 'S': '2.2100'}, 'I': {'H': '1.6000', 'C': '2.1600', 'N': '2.1200', 'O': '2.1100', 'I': '2.8360', 'P': '2.4900', 'S': '2.5600'}, 'P': {'H': '1.4100', 'C': '1.8300', 'N': '1.7200', 'O': '1.6400', 'F': '1.5000', 'Cl': '2.0400', 'Br': '2.2400', 'I': '2.4900', 'P': '2.3240', 'S': '2.1200'}, 'S': {'H': '1.3400', 'C': '1.8200', 'N': '1.6900', 'O': '1.6500', 'F': '1.5800', 'Cl': '2.0300', 'Br': '2.2100', 'I': '2.5600', 'P': '2.1200', 'S': '2.0380'}}
