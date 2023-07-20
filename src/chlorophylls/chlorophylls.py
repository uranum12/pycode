from pathlib import Path

import pandas as pd

file = Path("data/chlorophylls/7-18.csv")

for i in pd.read_csv(file).itertuples():
    Chl = ((i.abs665 - i.abs750) * i.a * 1000) / (83.4 * i.V * i.L)

    E663 = i.abs663 - i.abs750
    E645 = i.abs645 - i.abs750
    E630 = i.abs630 - i.abs750

    Chl_a = (11.64 * E663 - 2.16 * E645 + 0.10 * E630) * i.a / (i.V * i.L)
    Chl_b = (20.97 * E645 - 3.94 * E663 - 3.66 * E630) * i.a / (i.V * i.L)
    Chl_c = (54.22 * E630 - 14.81 * E645 - 5.53 * E663) * i.a / (i.V * i.L)

    print(f"地点               : {i.name}")
    print(f"吸光度 665nm       : {i.abs665}")
    print(f"吸光度 750nm       : {i.abs750}")
    print(f"吸光度 663nm       : {i.abs663}")
    print(f"吸光度 645nm       : {i.abs645}")
    print(f"吸光度 630nm       : {i.abs630}")
    print(f"アルコール容量     : {i.a} [mL]")
    print(f"分光光度計セル厚み : {i.L} [cm]")
    print(f"濾過湖水量         : {i.V} [L]")
    print("マーカー法")
    print(f"クロロフィル       : {Chl} [ug/L]")
    print("ユネスコ法")
    print(f"クロロフィル a     : {Chl_a} [ug/L]")
    print(f"クロロフィル b     : {Chl_b} [ug/L]")
    print(f"クロロフィル c     : {Chl_c} [ug/L]")
    print("====================")
