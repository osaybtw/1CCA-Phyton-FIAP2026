# eng2sp = dict()
# eng2sp['one'] = 'uno'
# print(eng2sp)
# print()
# eng2sp = {
#     'one': 'uno',
#     'two': 'dos',
# }
# print(eng2sp)
# print()
# print(eng2sp['two'])
# print()
# print('dos' in eng2sp)

def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d





