import pandas as pd

from utils.parser import parse_penguin


def load_penguin(df):

    # =========================
    # DATA WARNA STANDAR
    # =========================

    std = df.iloc[5:, [0, 1]].copy()

    std.columns = ["Nama Barang", "Harga"]

    std = std.dropna(subset=["Nama Barang"])

    parsed = std["Nama Barang"].apply(parse_penguin)

    std["Brand"] = parsed.apply(lambda x: x["brand"])
    std["Jenis"] = parsed.apply(lambda x: x["jenis"])
    std["Type"] = parsed.apply(lambda x: x["type"])
    std["Ukuran"] = parsed.apply(lambda x: x["ukuran"])

    # Semua warna selain orange & kuning
    std["Warna"] = "STANDAR"

    # =========================
    # DATA ORANGE & KUNING
    # =========================

    ok = df.iloc[5:, [5, 6]].copy()

    ok.columns = ["Nama Barang", "Harga"]

    ok = ok.dropna(subset=["Nama Barang"])

    parsed = ok["Nama Barang"].apply(parse_penguin)

    ok["Brand"] = parsed.apply(lambda x: x["brand"])
    ok["Jenis"] = parsed.apply(lambda x: x["jenis"])
    ok["Type"] = parsed.apply(lambda x: x["type"])
    ok["Ukuran"] = parsed.apply(lambda x: x["ukuran"])
    ok["Warna"] = parsed.apply(lambda x: x["warna"])
    ok.loc[ok["Type"] == "TQ", "Warna"] = "HITAM"

    # =========================
    # GABUNGKAN
    # =========================

    final = pd.concat([std, ok], ignore_index=True)

    final["Harga"] = pd.to_numeric(final["Harga"], errors="coerce")

    return final
