sp = 67836.43
rf = 36678.66
mg = 29229.88
es = 27165.48
out = 19849.53

total = sp+rf+mg+es+out


def calc_percentage(value):
    return (value/total)*100


print("total percentage SP: {:.0f}%".format(calc_percentage(sp)))
print("total percentage RF: {:.0f}%".format(calc_percentage(rf)))
print("total percentage MG: {:.0f}%".format(calc_percentage(mg)))
print("total percentages ES: {:.0f}%".format(calc_percentage(es)))
print("total percentage Outros: {:.0f}%".format(calc_percentage(out)))
