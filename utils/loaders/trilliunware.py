import pandas as pd
from utils.helper import bersihkan_harga
from utils.helper import bersihkan_harga, bersihkan_text


def load_trilliunware(df):

    hasil = []

    for _, row in df.iterrows():

        kategori = str(row.iloc[0]).upper().strip()
        produk = str(row.iloc[1]).upper().strip()

        warna_muda = row.iloc[2]
        warna_tua = row.iloc[3]

        produk_text = bersihkan_text(produk)
        kategori_text = bersihkan_text(kategori)

        # ==========================
        # JENIS
        # ==========================

        jenis = ""

        if "CD" in produk_text:
            jenis = "CLOSET DUDUK"

        elif "CJ" in produk_text:
            jenis = "CLOSET JONGKOK"

        elif kategori_text == "WASTAFEL":
            jenis = "WASTAFEL"

        elif kategori_text == "URINAL":
            jenis = "URINAL"

        elif kategori_text == "SOAP DISH":
            jenis = "SOAP DISH"

        elif kategori_text == "AVENA":
            jenis = "AVENA"

        # ==========================
        # TYPE
        # ==========================

        type_produk = ""

        for t in [
            "EUREKA",
            "EMERALD",
            "CAPRI",
            "CARRIBEAN",
            "MARION",
            "RUBY",
            "SAPPHIRA",
            "OPAL",
            "JASPER",
            "HARVEST",
            "ANDALUZITE",
            "CHRYSOLITE",
            "RHODOLITE",
            "SODALITE",
            "SPENE",
            "MALACHITE",
            "GARNET",
            "COBALT",
            "LILAC",
            "KROOZ",
            "PYRITE",
            "JUNIPER",
        ]:
            if t in produk_text:
                type_produk = t
                break

        # hasil.append(
        #     {
        #         "Brand": "TRILLIUNWARE",
        #         "Kategori": bersihkan_text(kategori),
        #         "Produk": bersihkan_text(produk),
        #         "Jenis": "",
        #         "Type": "",
        #         "Harga Muda": bersihkan_harga(warna_muda),
        #         "Harga Tua": bersihkan_harga(warna_tua),
        #     }
        # )

        hasil.append(
            {
                "Brand": "TRILLIUNWARE",
                "Kategori": kategori_text,
                "Produk": produk_text,
                "Jenis": jenis,
                "Type": type_produk,
                "Harga Muda": bersihkan_harga(warna_muda),
                "Harga Tua": bersihkan_harga(warna_tua),
            }
        )

    return pd.DataFrame(hasil)
