# import pandas as pd

# from utils.helper import bersihkan_harga
# from utils.parsers.unnu_parser import parse_unnu


# def load_unnu(df):

#     hasil = []

#     nama_sekarang = ""

#     for _, row in df.iterrows():

#         nama = row.iloc[0]
#         ukuran = row.iloc[1]
#         harga = row.iloc[2]

#         # simpan nama terakhir jika ada
#         if pd.notna(nama):
#             nama_sekarang = str(nama).upper().strip()

#         # skip jika ukuran kosong
#         if pd.isna(ukuran):
#             continue

#         nama_upper = nama_sekarang

#         ukuran_bersih = str(ukuran).upper().replace(" ", "")

#         harga_bersih = bersihkan_harga(harga)

#         info = parse_unnu(nama_upper)

#         # =================================
#         # TS01 WHITE IVORY PINK BLUE BLACK
#         # =================================

#         if "TS01" in nama_upper and "WHITE" in nama_upper:

#             for warna in ["WHITE", "IVORY", "PINK", "BLUE", "BLACK"]:

#                 hasil.append(
#                     {
#                         "Brand": "UNNU",
#                         "Jenis": info["jenis"],
#                         "Type": "TS01",
#                         "Ukuran": ukuran_bersih,
#                         "Warna": warna,
#                         "Harga": harga_bersih,
#                     }
#                 )

#             continue

#         # =================================
#         # TS01 CROME
#         # =================================

#         if "TS01" in nama_upper and "CROME" in nama_upper:

#             hasil.append(
#                 {
#                     "Brand": "UNNU",
#                     "Jenis": info["jenis"],
#                     "Type": "TS01",
#                     "Ukuran": ukuran_bersih,
#                     "Warna": "CROME",
#                     "Harga": harga_bersih,
#                 }
#             )

#             continue

#         # =================================
#         # NORMAL
#         # =================================

#         info = parse_unnu(nama_upper)

#     hasil.append(
#         {
#             "Brand": "UNNU",
#             "Jenis": info["jenis"],
#             "Type": info["type"],
#             "Ukuran": ukuran_bersih,
#             "Warna": info["warna"],
#             "Harga": harga_bersih,
#         }
#     )

#     return pd.DataFrame(hasil)


import pandas as pd

from utils.helper import bersihkan_harga
from utils.parsers.unnu_parser import parse_unnu


def load_unnu(df):

    hasil = []

    nama_sekarang = ""

    for _, row in df.iterrows():

        nama = row.iloc[0]
        ukuran = row.iloc[1]
        harga = row.iloc[2]

        # simpan nama terakhir
        if pd.notna(nama):
            nama_sekarang = str(nama).upper().strip()

        # skip jika ukuran kosong
        if pd.isna(ukuran):
            continue

        nama_upper = nama_sekarang

        ukuran_bersih = str(ukuran).upper().replace(" ", "")

        harga_bersih = bersihkan_harga(harga)

        info = parse_unnu(nama_upper)

        # =================================
        # TS01 WHITE IVORY PINK BLUE BLACK
        # =================================

        if "TS01" in nama_upper and "WHITE" in nama_upper:

            for warna in ["WHITE", "IVORY", "PINK", "BLUE", "BLACK"]:

                hasil.append(
                    {
                        "Brand": "UNNU",
                        "Jenis": info["jenis"],
                        "Type": "TS01",
                        "Ukuran": ukuran_bersih,
                        "Warna": warna,
                        "Harga": harga_bersih,
                    }
                )

            continue

        # =================================
        # TS01 CROME
        # =================================

        if "TS01" in nama_upper and "CROME" in nama_upper:

            hasil.append(
                {
                    "Brand": "UNNU",
                    "Jenis": info["jenis"],
                    "Type": "TS01",
                    "Ukuran": ukuran_bersih,
                    "Warna": "CROME",
                    "Harga": harga_bersih,
                }
            )

            continue

        # =================================
        # NORMAL
        # =================================

        hasil.append(
            {
                "Brand": "UNNU",
                "Jenis": info["jenis"],
                "Type": info["type"],
                "Ukuran": ukuran_bersih,
                "Warna": info["warna"],
                "Harga": harga_bersih,
            }
        )

    return pd.DataFrame(hasil)