import pandas as pd

from utils.helper import bersihkan_harga
from utils.parsers.steel_parser import parse_steel


def load_steel(df):

    hasil = []

    # B = Nama Barang
    # D = Harga Net
    # F = Harga Per Roll
    data = df.iloc[:, [1, 3, 5]].copy()

    data.columns = [
        "Produk",
        "Harga Net",
        "Harga Roll"
    ]

    data = data.dropna(subset=["Produk"])


    for _, row in data.iterrows():

        produk = str(row["Produk"]).strip()

        if not produk:
            continue


        info = parse_steel(produk)


        hasil.append({

            "Brand": "STEEL",
            "Produk": produk,

            "Jenis": info["jenis"],
            "Type": info["type"],
            "Kode": info["kode"],
            "Ukuran": info["ukuran"],
            "Warna": info["warna"],

            # default pakai harga roll
            "Harga": bersihkan_harga(row["Harga Roll"]),

            # simpan harga meter juga
            "Harga Net": bersihkan_harga(row["Harga Net"])

        })


    return pd.DataFrame(hasil)