from binary_decoder import decode

code = 3

amount_of_bits = input('Input How Many Bits Are per Character Returned')

sep_code = [code[i:i+1] for i in range(0, len(code), 1)]