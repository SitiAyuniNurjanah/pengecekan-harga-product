import pandas as pd

from utils.helper import bersihkan_harga

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
                "Harga": int(float(str(row["Harga"]).replace(",", ".")) * 1000),
            }
        )
    return pd.DataFrame(hasil)
