# 吸光度
ABs750 = 0.0035
ABs663 = 0.1091
ABs645 = 0.0333
ABs630 = 0.0275

# 抽出した溶媒の容量 [mL]
a = 8.0

# 分光光度計のセルの厚さ [cm]
L = 1.0

# 濾過湖水量 [L]
V = 0.5

E663 = ABs663 - ABs750
E645 = ABs645 - ABs750
E630 = ABs630 - ABs750

Chl_a = (11.64 * E663 - 2.16 * E645 + 0.10 * E630) * a / (V * L)
Chl_b = (20.97 * E645 - 3.94 * E663 - 3.66 * E630) * a / (V * L)
Chl_c = (54.22 * E630 - 14.81 * E645 - 5.53 * E663) * a / (V * L)

print(f"吸光度 750nm       : {ABs750}")
print(f"吸光度 663nm       : {ABs663}")
print(f"吸光度 645nm       : {ABs645}")
print(f"吸光度 630nm       : {ABs630}")
print(f"アルコール容量     : {a} [mL]")
print(f"分光光度計セル厚み : {L} [cm]")
print(f"濾過湖水量         : {V} [L]")

print(f"E663               : {E663}")
print(f"E645               : {E645}")
print(f"E630               : {E630}")

print(f"クロロフィル a     : {Chl_a} [ug/L]")
print(f"クロロフィル b     : {Chl_b} [ug/L]")
print(f"クロロフィル c     : {Chl_c} [ug/L]")
