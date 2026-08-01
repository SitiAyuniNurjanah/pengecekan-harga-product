# import pandas as pd
# from utils.parsers.pintu_parser import pintu_parser
# from utils.helper import bersihkan_harga


# def load_pintu(df):

#     hasil = []

#     # ======================
#     # PVC
#     # ======================
#     print(df.iloc[:, 7])
#     pvc = df.iloc[5:18, [0, 1]].copy()
#     pvc.columns = ["Nama Barang", "Harga"]
#     pvc = pvc.dropna(subset=["Nama Barang"])

#     for _, row in pvc.iterrows():

#         p = pintu_parser(row["Nama Barang"])

#         hasil.append(
#             {
#                 "Brand": "PINTU",
#                 "Jenis": p["jenis"],
#                 "Type": p["type"],
#                 "Kode": p["kode"],
#                 "Ukuran": p["ukuran"],
#                 "Warna": p["warna"],
#                 "Produk": row["Nama Barang"],
#                 "Harga": bersihkan_harga(row["Harga"]),
#             }
#         )

#     # ======================
#     # ALUMUNIUM
#     # ======================

#     alu = df.iloc[5:18, [4, 5]].copy()
#     alu.columns = ["Nama Barang", "Harga"]
#     alu = alu.dropna(subset=["Nama Barang"])

#     for _, row in alu.iterrows():

#         p = pintu_parser(row["Nama Barang"])

#         hasil.append(
#             {
#                 "Brand": "PINTU",
#                 "Jenis": p["jenis"],
#                 "Type": p["type"],
#                 "Kode": p["kode"],
#                 "Ukuran": p["ukuran"],
#                 "Warna": p["warna"],
#                 "Produk": row["Nama Barang"],
#                 "Harga": bersihkan_harga(row["Harga"]),
#             }
#         )

#     # ======================
#     # UPVC
#     # ======================

#     upvc = df.iloc[5:18, [7, 8]].copy()
#     upvc.columns = ["Nama Barang", "Harga"]
#     upvc = upvc.dropna(subset=["Nama Barang"])

#     for _, row in upvc.iterrows():

#         p = pintu_parser(row["Nama Barang"])

#         hasil.append(
#             {
#                 "Brand": "PINTU",
#                 "Jenis": p["jenis"],
#                 "Type": p["type"],
#                 "Kode": p["kode"],
#                 "Ukuran": p["ukuran"],
#                 "Warna": p["warna"],
#                 "Produk": row["Nama Barang"],
#                 "Harga": bersihkan_harga(row["Harga"]),
#             }
#         )

#         # return pd.DataFrame(hasil)

#         df_hasil = pd.DataFrame(hasil)

#     return df_hasil


# import pandas as pd
# from utils.parsers.pintu_parser import pintu_parser
# from utils.helper import bersihkan_harga


# def load_pintu(df):

#     hasil = []

#     sections = [
#         (0, 1),   # PVC
#         (4, 5),   # ALUMUNIUM
#         (7, 8),   # UPVC
#     ]

#     for col_nama, col_harga in sections:

#         data = df.iloc[:, [col_nama, col_harga]].copy()
#         data.columns = ["Nama Barang", "Harga"]

#         # buang yang kosong
#         data = data.dropna(subset=["Nama Barang"])

#         # hanya ambil yang benar-benar pintu
#         data = data[
#             data["Nama Barang"]
#             .astype(str)
#             .str.contains("PINTU", case=False, na=False)
#         ]

#         for _, row in data.iterrows():

#             p = pintu_parser(row["Nama Barang"])

#             hasil.append(
#                 {
#                     "Brand": "PINTU",
#                     "Jenis": p["jenis"],
#                     "Type": p["type"],
#                     "Kode": p["kode"],
#                     "Ukuran": p["ukuran"],
#                     "Warna": p["warna"],
#                     "Produk": row["Nama Barang"],
#                     "Harga": bersihkan_harga(row["Harga"]),
#                 }
#             )

#     return pd.DataFrame(hasil)

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
            data["Nama Barang"]
            .astype(str)
            .str.contains("PINTU", case=False, na=False)
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

    return pd.DataFrame(hasil)