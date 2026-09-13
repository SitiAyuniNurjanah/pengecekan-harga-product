import pandas as pd

from utils.helper import bersihkan_harga
from utils.parsers.accsware_parser import parse_accsware


def load_accsware(df):

    hasil = []

    data = df.iloc[:, [0, 1]].copy()

    data.columns = [
        "Produk",
        "Harga"
    ]

    data = data.dropna(subset=["Produk"])

    for _, row in data.iterrows():

        produk = str(row["Produk"]).strip()

        if not produk:
            continue

        info = parse_accsware(produk)

        hasil.append({
            "Brand": "ACCSWARE",
            "Produk": produk,
            "Jenis": info["jenis"],
            "Type": info["type"],
            "Kode": info["kode"],
            "Ukuran": info["ukuran"],
            "Warna": info["warna"],
            "Harga": bersihkan_harga(row["Harga"]),
        })

    return pd.DataFrame(hasil)