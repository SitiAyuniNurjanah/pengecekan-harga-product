import pandas as pd
from utils.parsers.pintu_parser import pintu_parser
from utils.helper import bersihkan_harga


def load_pintu(df):
    hasil = []

    sections = [
        (0, 1),  # PVC
        (4, 5),  # ALUMUNIUM
        (7, 8),  # UPVC
    ]

    for col_nama, col_harga in sections:
        data = df.iloc[:, [col_nama, col_harga]].copy()
        data.columns = ["Nama Barang", "Harga"]

        # Buang baris tanpa nama barang
        data = data.dropna(subset=["Nama Barang"])

        # Hanya ambil produk pintu
        data = data[
            data["Nama Barang"].astype(str).str.contains("PINTU", case=False, na=False)
        ]

        for _, row in data.iterrows():
            p = pintu_parser(row["Nama Barang"])

            hasil.append(
                {
                    "Brand": "PINTU",
                    "Jenis": p["jenis"],
                    "Type": p["type"],
                    "Kode": p["kode"],
                    "Ukuran": p["ukuran"],
                    "Warna": p["warna"],
                    "Produk": row["Nama Barang"],
                    "Harga": bersihkan_harga(row["Harga"]),
                }
            )

    df_hasil = pd.DataFrame(hasil)
    return df_hasil
