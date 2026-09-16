from tabulate import tabulate

h1 = [21.1, 23.9, 23.7, 21.8, 23.6, 23.4, 23.2, 23.9]
h2 = [5.1, 5.8, 5.7, 5.1, 5.7, 5.6, 5.6, 5.8]

x = []
for a, b in zip(h1, h2):
    x.append(b / a)

gamma = []
for i in x:
    gamma.append(1 / (1 - i))
avggamma = sum(gamma) / len(gamma)
avgx = sum(map(abs, x)) / len(x)

dtx = []
for i in x:
    dtx.append(i - avgx)

avgdtx = sum(map(abs, dtx)) / len(dtx)


dtx2 = [i * i for i in dtx]
s_nx = (sum(dtx2) / len(dtx2) / (len(dtx2) - 1)) ** .5

table = {
    'h1': h1, 'h2': h2, 'x': x,
    'gamma': gamma, '<gamma>': [avggamma],
    '<x>': [avgx], 'dtx': dtx,
    '<dtx>': [avgdtx], 'dtx^2': dtx2, "S'nx": [s_nx]
}
print(tabulate(table, headers="keys", tablefmt='grid', floatfmt=(
    '', '', '.2e', '.3f', '.3f', '.3f', '.2e', '.2e', '.2e', '.2e'
)))


s_gamma = s_nx / (1 - avgx) ** 2
student = [('0.68', 1.1), ('0.80', 1.4), ('0.95', 2.4), ('0.99', 3.5), ('0.995', 5.4)]


for p, tpn in student:
    print("----------")
    print(f'Student ratio: p = {p}, t = {tpn}')
    print(f'dtgamma = {tpn * s_gamma:.2e}')
    dtgamma = tpn * s_gamma
    print('y = ' +  f' {avggamma:.2e}' + " +"  + f' {tpn * s_gamma:.2e}')