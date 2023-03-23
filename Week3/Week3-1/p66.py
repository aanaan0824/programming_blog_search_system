def test_local(a, r):
    print('local original ', a, r)
    a = 12
    r[1] = 999
    print('local changed  ', a, r)

a = -5
r = [0, 1, 2]
print('global original', a, r)
test_local(a, r)
print('global changed ', a, r)
