import pandas as pd
from utils.helper import bersihkan_harga, bersihkan_text


def load_trilliunware(df):
    hasil = []

    type_list = [
        "AMETHYST",
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
        "CITRINE",
        "PERIDOT",
    ]

    for _, row in df.iterrows():

        kategori = bersihkan_text(row.iloc[0])
        produk = bersihkan_text(row.iloc[1])

        harga_muda = bersihkan_harga(row.iloc[2])
        harga_tua = bersihkan_harga(row.iloc[3])

        # ==========================
        # JENIS
        # ==========================
        jenis = ""

        if "CD" in produk:
            jenis = "CLOSET DUDUK"

        elif "CJ" in produk:
            jenis = "CLOSET JONGKOK"

        elif kategori == "WASTAFEL":
            jenis = "WASTAFEL"

        elif kategori == "URINAL":
            jenis = "URINAL"

        elif kategori == "SOAP DISH":
            jenis = "SOAP DISH"

        # ==========================
        # TYPE
        # ==========================
        type_produk = ""

        for t in type_list:
            if t in produk:
                type_produk = t
                break

        # ==========================
        # VARIAN
        # ==========================
        varian = ""

        # if "SET (TANPA KRAN)" in produk:
        if "SET" in produk and "TANPA KRAN" in produk:
            varian = "SET TANPA KRAN"

        elif "BODY ONLY" in produk:
            varian = "BODY ONLY"

        elif "KAKI ONLY" in produk:
            varian = "KAKI ONLY"

        # elif "SET DGN KRAN" in produk:
        elif "SET" in produk and ("DGN KRAN" in produk or "DENGAN KRAN" in produk):
            varian = "SET DGN KRAN"

        elif "BASIN TAP" in produk:
            varian = "BASIN TAP"

        if type_produk == "MALACHITE":

            if "GARNET" in produk:
                varian = "GARNET"

            elif "LILAC" in produk:
                varian = "LILAC"

            if "BODY ONLY" in produk:
                varian += " BODY ONLY"

            elif "KAKI ONLY" in produk:
                varian += " KAKI ONLY"

            elif "SET (TANPA KRAN)" in produk:
                varian += " SET TANPA KRAN"

        # ==========================
        # WARNA
        # ==========================
        warna = ""

        if "BLACK" in produk:
            warna = "BLACK"

        elif "GREY" in produk:
            warna = "GREY"

        # ==========================
        # SIMPAN
        # ==========================
        if not produk:
            continue
        hasil.append(
            {
                "Brand": "TRILLIUNWARE",
                "Kategori": kategori,
                "Produk": produk,
                "Jenis": jenis,
                "Type": type_produk,
                "Varian": varian,
                "Warna": warna,
                "Harga Muda": harga_muda,
                "Harga Tua": harga_tua,
            }
        )

    # return pd.DataFrame(hasil)
    df = pd.DataFrame(hasil)

    print(df[df["Type"] == "GARNET"].to_string())
    print(df[df["Produk"].str.contains("AMETHYST", na=False)])
    print(df[df["Produk"].str.contains("JASPER", na=False)])
    print(df[df["Produk"].str.contains("OPAL", na=False)])
    print(df[df["Produk"].str.contains("CAPRI", na=False)])

    return df

