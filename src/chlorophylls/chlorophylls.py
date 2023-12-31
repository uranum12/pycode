from csv import DictReader, DictWriter
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path


def main() -> None:
    # データファイル
    data_path = Path("data/chlorophylls/7-18.csv")
    print(f"ファイル           : {data_path}")

    # 出力先ファイル
    out_path = Path("out/chlorophylls") / data_path.name
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with data_path.open("r") as data_file, out_path.open("w") as out_file:
        reader = DictReader(data_file)
        writer = DictWriter(
            out_file,
            ["name", "marker", "unesco_a", "unesco_b", "unesco_c"],
        )
        writer.writeheader()

        for row in reader:
            abs750 = Decimal(row["abs750"])
            e665 = Decimal(row["abs665"]) - abs750
            e663 = Decimal(row["abs663"]) - abs750
            e645 = Decimal(row["abs645"]) - abs750
            e630 = Decimal(row["abs630"]) - abs750

            f = Decimal(row["a"]) / (Decimal(row["V"]) * Decimal(row["L"]))

            # マーカー法
            chl_marker = e665 * 1000 / Decimal("83.4") * f

            # ユネスコ法
            chl_unesco_a = (
                Decimal("11.64") * e663
                - Decimal("2.16") * e645
                + Decimal("0.10") * e630
            ) * f
            chl_unesco_b = (
                Decimal("20.97") * e645
                - Decimal("3.94") * e663
                - Decimal("3.66") * e630
            ) * f
            chl_unesco_c = (
                Decimal("54.22") * e630
                - Decimal("14.81") * e645
                - Decimal("5.53") * e663
            ) * f

            # 小数点以下3桁に四捨五入
            exp = Decimal("0.001")
            chl_marker = chl_marker.quantize(exp, ROUND_HALF_UP)
            chl_unesco_a = chl_unesco_a.quantize(exp, ROUND_HALF_UP)
            chl_unesco_b = chl_unesco_b.quantize(exp, ROUND_HALF_UP)
            chl_unesco_c = chl_unesco_c.quantize(exp, ROUND_HALF_UP)

            print("====================")
            print(f"地点               : {row['name']}")
            print(f"吸光度 750nm       : {row['abs750']}")
            print(f"吸光度 665nm       : {row['abs665']}")
            print(f"吸光度 663nm       : {row['abs663']}")
            print(f"吸光度 645nm       : {row['abs645']}")
            print(f"吸光度 630nm       : {row['abs630']}")
            print(f"アルコール容量     : {row['a']} [mL]")
            print(f"分光光度計セル厚み : {row['L']} [cm]")
            print(f"濾過湖水量         : {row['V']} [L]")
            print("マーカー法")
            print(f"クロロフィル       : {chl_marker} [ug/L]")
            print("ユネスコ法")
            print(f"クロロフィル a     : {chl_unesco_a} [ug/L]")
            print(f"クロロフィル b     : {chl_unesco_b} [ug/L]")
            print(f"クロロフィル c     : {chl_unesco_c} [ug/L]")

            writer.writerow(
                {
                    "name": row["name"],
                    "marker": chl_marker,
                    "unesco_a": chl_unesco_a,
                    "unesco_b": chl_unesco_b,
                    "unesco_c": chl_unesco_c,
                },
            )


if __name__ == "__main__":
    main()
