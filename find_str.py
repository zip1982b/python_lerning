s = 'barbarain'
sub = 'bar'
count = 0
old_res = -1
for i in range(len(s)):
    idx = s.find(sub, i)
    if idx != -1 and idx != old_res:
        count += 1
    old_res = idx


