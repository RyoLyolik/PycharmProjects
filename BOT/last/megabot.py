# def convert_base(num, from_base = 10, to_base = 10):
#     # first convert to decimal number
#     n = int(str(num), from_base)
#     # now convert decimal to 'to_base' base
#     alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     print(n)
#     if n < to_base:
#         print(n,1)
#         return alphabet[n]
#     else:
#         print(alphabet[n% to_base], 'alpabet %')
#         return convert_base(n // to_base, 10, to_base) + alphabet[n % to_base]
#
# print(convert_base('10a', 16, 10))
