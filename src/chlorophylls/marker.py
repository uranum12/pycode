# 吸光度
ABs750 = 0.0035
ABs665 = 0.1077

# 抽出した溶媒の容量 [mL]
a = 8.0

# 分光光度計のセルの厚さ [cm]
L = 10.0

# 濾過湖水量 [L]
V = 0.5

Chl = ((ABs665 - ABs750) * a * 1000) / (83.4 * V * L)

print(f"吸光度 750nm       : {ABs750}")
print(f"吸光度 665nm       : {ABs665}")
print(f"アルコール容量     : {a} [mL]")
print(f"分光光度計セル厚み : {L} [cm]")
print(f"濾過湖水量         : {V} [L]")

print(f"クロロフィル       : {Chl} [ug/L]")
