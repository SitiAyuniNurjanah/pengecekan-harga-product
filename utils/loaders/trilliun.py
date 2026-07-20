import pandas as pd


def load_trilliun(df):

    # Mengambil tabel utama dari excel price list
    # (Header berada pada baris ke-5)

    df = df.iloc[1:, [0, 1, 2, 4, 5, 6]].copy()
    df.columns = ["Nama Barang", "Ukuran", "Meter50", "Harga50", "Meter100", "Harga100"]

    # Mengisi nama barang yang kosong

    df["Nama Barang"] = df["Nama Barang"].ffill()

    hasil = []

    # Membaca setiap baris

    for _, row in df.iterrows():

        nama = (
            str(row["Nama Barang"]).upper().replace("”", '"').replace("″", '"').strip()
        )

        # Menentukan jenis selang dari excel pesanan

        if "SPIRAL PREMIUM" in nama:
            jenis = "SPIRAL PREMIUM"

        elif "SPIRAL" in nama:
            jenis = "SPIRAL"

        elif "SUPERFLEX" in nama:
            jenis = "SUPERFLEX"

        elif "HIPREX" in nama:
            jenis = "HIPREX"

        elif "DOF" in nama:
            jenis = "DOF"

        elif "STABILO" in nama:
            jenis = "STABILO"

        elif "ELASTIS TEBAL" in nama:
            jenis = "ELASTIS TEBAL"

        elif "TRANSPARAN" in nama:
            jenis = "TRANSPARAN"

        elif "AIR HOSE" in nama:
            jenis = "AIR HOSE"

        elif "LUBE" in nama:
            jenis = "LUBE"

        else:
            jenis = ""

        # mencoockan uk pesanan dengan data price list
        ukuran = (
            str(row["Ukuran"])
            .upper()
            .replace('"', "")
            .replace("”", "")
            .replace("″", "")
            .replace("“", "")
            .strip()
        )

        ukuran = " ".join(ukuran.split())

        # untuk selang 50m
        if pd.notna(row["Harga50"]):

            hasil.append(
                {
                    "Brand": "TRILLIUN",
                    "Jenis": jenis,
                    "Type": ukuran,
                    "Ukuran": f"{int(float(row['Meter50']))}M",
                    "Harga": pd.to_numeric(row["Harga50"], errors="coerce"),
                }
            )

        # =========================
        # Harga 100 Meter
        # =========================
        if pd.notna(row["Harga100"]):

            hasil.append(
                {
                    "Brand": "TRILLIUN",
                    "Jenis": jenis,
                    "Type": ukuran,
                    "Ukuran": f"{int(float(row['Meter100']))}M",
                    "Harga": pd.to_numeric(row["Harga100"], errors="coerce"),
                }
            )

    hasil = pd.DataFrame(hasil)

    # Membersihkan lagi supaya
    # matching lebih mudah
    hasil["Jenis"] = hasil["Jenis"].astype(str).str.upper().str.strip()

    hasil["Type"] = (
        hasil["Type"]
        .astype(str)
        .str.replace('"', "", regex=False)
        .str.replace("”", "", regex=False)
        .str.replace("″", "", regex=False)
        .str.strip()
    )

    hasil["Ukuran"] = hasil["Ukuran"].astype(str).str.upper().str.strip()

    hasil["Harga"] = pd.to_numeric(hasil["Harga"], errors="coerce")

    return hasil
