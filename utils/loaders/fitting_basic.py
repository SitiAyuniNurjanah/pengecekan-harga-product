import pandas as pd

from utils.helper import bersihkan_harga


def load_blok(df, col_nama, col_harga):

    hasil = []

    jenis = ""

    daftar_jenis = [
        "KNEE",
        "SOCKET",
        "TEE",
        "PLUG",
        "FAUCET KNEE",
        "FAUCET SOCKET",
        "FAUCET TEE",
        "VALVE SOCKET",
        "WATERMUR",
        "DOP",
        "LONG ELBOW",
    ]

    for i in range(len(df)):

        nama = df.iloc[i, col_nama]

        harga = df.iloc[i, col_harga]

        if pd.isna(nama):
            continue

        nama = str(nama).upper().strip()

        if nama in ("", "NAN"):
            continue

        # ketemu judul merah
        if nama in daftar_jenis:
            jenis = nama
            continue

        # skip header harga
        if "HARGA" in nama:
            continue

        if pd.isna(harga):
            continue

        parts = nama.split(" ", 1)

        if len(parts) == 2:
            tipe = parts[0]
            ukuran = parts[1]
        else:
            tipe = ""
            ukuran = nama

        hasil.append(
            {
                "Brand": "TRILLIUN",
                "Jenis": jenis,
                "Type": tipe,
                "Ukuran": ukuran.replace("X", "x").strip(),
                "Harga": bersihkan_harga(harga),
            }
        )

    return hasil


def load_fitting_basic(df):

    hasil = []

    # blok kiri (A-B)
    hasil.extend(load_blok(df, 0, 1))

    # blok tengah (F-G)
    hasil.extend(load_blok(df, 5, 6))

    # blok kanan (K-L)
    hasil.extend(load_blok(df, 10, 11))

    return pd.DataFrame(hasil)
