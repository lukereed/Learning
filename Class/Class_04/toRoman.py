#!/usr/bin/env python
#  __author__ = 'willandmei'

import sys


arabic_to_roman = '1:I,4:IV,5:V,9:IX,10:X,40:XL,50:L,90:XC,100:C,400:CD,500:D,900:CM,1000:M'

roman  = dict([(int(k),v) for k,v in [e.split(':') for e in arabic_to_roman.split(',')]])
arabic = dict([(v,int(k)) for k,v in [e.split(':') for e in arabic_to_roman.split(',')]])
# the difference between these two is that roman has int as key
# and arabic has the letter as the key

def to_roman(x):
    """Converts arabic numbers to roman numerals (e.g., 1920 --> MCMXX"""
    if (type(x) != int):  raise TypeError('x must be an int')

    result = ''
    i = 0
    keys = sorted(roman.keys(), reverse=True)
    while (x > 0):
        while (i < len(keys) and keys[i] > x):
            i += 1
        result += roman[keys[i]]
        x -= keys[i]
    return result

def to_arabic_helper(s, result, key):
    if (len(result) > 0 and min(result) < arabic[key]):
        raise ValueError('valid key: {0} used in invalid location in roman numeral: {1}'.format(key, s))
    result.append(arabic[key])

def to_arabic(s):
    """Converts roman numerals to arabic (e.g., MCMXX --> 1920)"""
    result = []
    i = 0
    keys = arabic.keys()
    while  i < len(s):
        # tests if the next two characters are in the dictionary
        if i + 1 < len(keys) and s[i:i+2] in keys:
            to_arabic_helper(s, result, s[i:i+2])
            i += 2
        # if not, then it checks just the next character
        elif (s[i] in keys):
            to_arabic_helper(s, result, s[i])
            i += 1
        # otherwise it throws an error that the roman numeral doesn't exist
        else:
            raise ValueError('invalid Roman numeral character')
    return sum(result)

def test_roman_numeral_solutions():
    """Tests converting arabic numbers (1, 2, 3... ) to roman numerals (I, II, III...)
       and vice-versa"""
    # for x in range(1, 4000):
    #     print('{0:>4} is: {1:<15}'.format(x, to_roman(x)))
    #     if x % 10 == 9:
    #         print()
    #
    # for i in range(1, 4000):
    #     s = to_roman(i)
    #     print('{0:>15} is {1:4}'.format(s, to_arabic(s)))
    #     if i % 10 == 9:
    #         print()
    '''
    try:
        to_roman(10)
        to_roman(3.5)
    except TypeError as e:
        print(e, file=sys.stderr)
    '''
    for yr in range(1960,2001):
        print(yr,to_roman(yr))

#    to_arabic('CCCZXII')    # test invalid roman numeral character

    # for el in 'MXXM MCMIC XII CMDXCIX IXLCM'.split():   # test valid chars in invalid positions
    #     to_arabic(el)

test_roman_numeral_solutions()

if (__name__ == '__main__'):
    print('here are some command line args...')
    for el in sys.argv[1:]:  print(el)
    print('no more args...')

#    test_roman_numeral_solutions()


