import pandas as pd


def load_campur(df):

    hasil = []

    # =====================================================
    # TOREN POLOS
    # A = Produk
    # B = Harga
    # =====================================================

    toren = df.iloc[1:, [0, 1]].copy()
    toren.columns = ["Produk", "Harga"]

    for _, row in toren.iterrows():

        if pd.isna(row["Produk"]):
            continue

        produk = str(row["Produk"]).strip()

        hasil.append(
            {
                "Brand": "CAMPUR",
                "Produk": produk,
                "Jenis": "TOREN POLOS",
                "Type": "",
                "Ukuran": "",
                "Warna": "",
                "Harga": pd.to_numeric(
                    row["Harga"],
                    errors="coerce"
                ),
            }
        )

    # =====================================================
    # FIBER PAGAR
    # D = Produk
    # E = Harga
    # =====================================================

    fiber = df.iloc[1:, [3, 4]].copy()
    fiber.columns = ["Produk", "Harga"]

    for _, row in fiber.iterrows():

        if pd.isna(row["Produk"]):
            continue

        produk = str(row["Produk"]).strip()

        hasil.append(
            {
                "Brand": "CAMPUR",
                "Produk": produk,
                "Jenis": "FIBER PAGAR",
                "Type": "",
                "Ukuran": "",
                "Warna": "",
                "Harga": pd.to_numeric(
                    row["Harga"],
                    errors="coerce"
                ),
            }
        )

    # =====================================================
    # BAK MANDI
    # G = Produk
    # H = Harga
    # =====================================================

    bak_mandi = df.iloc[1:, [6, 7]].copy()
    bak_mandi.columns = ["Produk", "Harga"]

    for _, row in bak_mandi.iterrows():

        if pd.isna(row["Produk"]):
            continue

        produk = str(row["Produk"]).strip()

        hasil.append(
            {
                "Brand": "CAMPUR",
                "Produk": produk,
                "Jenis": "BAK MANDI",
                "Type": "",
                "Ukuran": "",
                "Warna": "",
                "Harga": pd.to_numeric(
                    row["Harga"],
                    errors="coerce"
                ),
            }
        )

    # =====================================================
    # LEM
    # J = Produk
    # K = Harga
    # =====================================================

    lem = df.iloc[1:, [9, 10]].copy()
    lem.columns = ["Produk", "Harga"]

    for _, row in lem.iterrows():

        if pd.isna(row["Produk"]):
            continue

        produk = str(row["Produk"]).strip()

        hasil.append(
            {
                "Brand": "CAMPUR",
                "Produk": produk,
                "Jenis": "LEM",
                "Type": "",
                "Ukuran": "",
                "Warna": "",
                "Harga": pd.to_numeric(
                    row["Harga"],
                    errors="coerce"
                ),
            }
        )

    return pd.DataFrame(hasil)