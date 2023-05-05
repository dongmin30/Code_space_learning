# %%
num2 = dict() #{}
e = dict([('python', 1990)])
# %%
e = dict([(list('python'), 1990)])
# %%
import math
math.pi
# %%
math.e
# %%
help(round)
# %%
p = dict(apple=0.4, orange=0.3, banana=0.25)
p
# %%
for k, v in p.items():
    p[k] = round(v * 0.9, 2)
p
# %%
for i in p.items():
    p[i[0]] = round(i[1] * 0.9, 2)
p
# %%
lst = [1, 2, 3]
a, b, c = lst
c
# %%
data = lst
print(data[0], data[1], data[2])
# %%
