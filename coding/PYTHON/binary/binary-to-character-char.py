from binary_decoder import decode

import math

code = int(input('Input Binary Here\n'))

amount_of_bits = int(input('\nInput Number of Bits Per Character\n'))

sep_code = [code[i:i + amount_of_bits] for i in range(0, len(str(code)), amount_of_bits)]

use_sep_code = 0

while amount_of_bits != 0:
    decode(sep_code[use_sep_code])
    amount_of_bits = amount_of_bits - 1
    use_sep_code = use_sep_code + 1