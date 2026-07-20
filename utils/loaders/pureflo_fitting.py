import re
import pandas as pd

from utils.helper import bersihkan_harga


def load_blok(df, col_nama, col_harga):

    hasil = []

    jenis = ""
    tipe = ""

    for i in range(len(df)):

        nama = df.iloc[i, col_nama]
        harga = df.iloc[i, col_harga]

        if pd.isna(nama):
            continue

        nama = str(nama).upper().strip()

        if nama in ("", "NAN"):
            continue

        m = re.search(r"(.+?)\s*\(?\s*(AW|D)\s*\)?(?:\s+\d|\s*\*.*|$)", nama)
        if m:

            jenis = (
                m.group(1)
                .replace("REDUCER", "REDUCER SOCKET")
                .replace("INCREASER", "INCREASER SOCKET")
                .replace("FAUCET ELBOW WITH METAL", "FAUCET ELBOW METAL")
                .replace("FAUCET SOCKET WITH METAL", "FAUCET SOCKET METAL")
                .replace("METAL INSERT", "METAL")
                .strip()
            )

            tipe = m.group(2)

            continue

        # skip header

        if "UKURAN" in nama or "HARGA" in nama:
            continue

        if pd.isna(harga):
            continue

        hasil.append(
            {
                "Brand": "TRILLIUN",
                "Jenis": jenis,
                "Type": tipe,
                "Ukuran": (nama.replace("X", "x").replace("  ", " ").strip()),
                "Harga": bersihkan_harga(harga),
            }
        )

    return hasil


def load_pureflo_fitting(df):

    hasil = []

    # mulai dari baris ke-3
    df = df.iloc[2:].reset_index(drop=True)

    # blok kiri A-B
    hasil.extend(load_blok(df, 0, 1))

    # blok tengah D-E
    hasil.extend(load_blok(df, 3, 4))

    # blok kanan G-H
    hasil.extend(load_blok(df, 6, 7))

    return pd.DataFrame(hasil)
