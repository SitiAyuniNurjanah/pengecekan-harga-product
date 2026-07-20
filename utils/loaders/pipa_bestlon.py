import pandas as pd


def load_pipa_bestlon(df):

    df = df.iloc[2:, [0, 1, 3]].copy()

    df.columns = ["Type", "Ukuran", "Harga"]

    # isi type yang kosong
    df["Type"] = df["Type"].ffill()

    hasil = []

    for _, row in df.iterrows():

        hasil.append(
            {
                "Brand": "BESTLON",
                "Jenis": "PIPA",
                "Type": str(row["Type"]).upper().strip(),
                "Ukuran": (
                    str(row["Ukuran"])
                    .replace('"', "")
                    .replace("”", "")
                    .replace("″", "")
                    .strip()
                ),
                "Warna": "PUTIH",
                "Harga": pd.to_numeric(row["Harga"], errors="coerce"),
            }
        )

    return pd.DataFrame(hasil)
