# ● Dictionary Merge:
# ○ Given two dictionaries, merge them into a new dictionary, excluding any keys
# that start with an underscore.

di_1 = {"ajsfg":15, "_jgfajgf":26, "skudgf":18}
di_2 = {"_aksfauksfg":49, "kasgfka":31, "_djfh":29}

res = {k: v for k, v in (di_1.items() | di_2.items()) if k[0] != "_"}
print(res)

