import pandas as pd


def load_trilliun(df):

    hasil = []


    # ==================================================
    # SELANG BESAR (A-G)
    # ==================================================

    df_besar = df.iloc[1:, [0, 1, 2, 4, 5, 6]].copy()

    df_besar.columns = [
        "Nama Barang",
        "Ukuran",
        "Meter50",
        "Harga50",
        "Meter100",
        "Harga100",
    ]

    df_besar["Nama Barang"] = df_besar["Nama Barang"].ffill()


    for _, row in df_besar.iterrows():

        nama = str(row["Nama Barang"]).upper().strip()

        jenis = get_jenis(nama)

        ukuran = clean_ukuran(row["Ukuran"])


        # harga 50 meter
        if pd.notna(row["Harga50"]):

            hasil.append(
                {
                    "Brand": "TRILLIUN",
                    "Jenis": jenis,
                    "Type": ukuran,
                    "Ukuran": f"{int(float(row['Meter50']))}M",
                    "Harga": clean_harga(row["Harga50"]),
                }
            )


        # harga 100 meter
        if pd.notna(row["Harga100"]):

            hasil.append(
                {
                    "Brand": "TRILLIUN",
                    "Jenis": jenis,
                    "Type": ukuran,
                    "Ukuran": f"{int(float(row['Meter100']))}M",
                    "Harga": clean_harga(row["Harga100"]),
                }
            )



    # ==================================================
    # SELANG KECIL (J-N)
    # ==================================================

    # cari kolom yang isinya DOF persis
    kolom_kecil = None


    for col in df.columns:

        data = (
            df[col]
            .astype(str)
            .str.upper()
            .str.strip()
        )


        if data.eq("DOF").any():

            kolom_kecil = col
            break



    if kolom_kecil is not None:


        posisi = df.columns.get_loc(kolom_kecil)


        # ambil 5 kolom
        # jenis + ukuran + 4 harga
        df_kecil = df.iloc[:, posisi:posisi+5].copy()


        jenis = ""


        for _, row in df_kecil.iterrows():


            nama = (
                str(row.iloc[0])
                .upper()
                .strip()
            )


            # nama jenis
            if nama in [
                "DOF",
                "SUPERFLEX",
                "STABILLO",
                "STABILO",
                "HIPREX"
            ]:


                if nama == "STABILLO":
                    jenis = "STABILO"
                else:
                    jenis = nama


                continue



            # skip header
            if nama in [
                "",
                "NAN",
                "SIZE (INCH)",
                "(RP/ROI)"
            ]:
                continue



            ukuran = clean_ukuran(nama)



            daftar_harga = [
                ("5M", row.iloc[1]),
                ("10M", row.iloc[2]),
                ("15M", row.iloc[3]),
                ("20M", row.iloc[4]),
            ]


            for meter, harga in daftar_harga:


                harga = clean_harga(harga)


                if harga is not None:


                    hasil.append(
                        {
                            "Brand": "TRILLIUN",
                            "Jenis": jenis,
                            "Type": ukuran,
                            "Ukuran": meter,
                            "Harga": harga,
                        }
                    )



    # ==================================================
    # CLEAN DATA
    # ==================================================

    hasil = pd.DataFrame(hasil)


    if hasil.empty:
        return hasil



    hasil["Jenis"] = (
        hasil["Jenis"]
        .astype(str)
        .str.upper()
        .str.strip()
    )


    hasil["Type"] = (
        hasil["Type"]
        .astype(str)
        .str.upper()
        .str.replace('"',"", regex=False)
        .str.replace("”","", regex=False)
        .str.replace("″","", regex=False)
        .str.strip()
    )


    hasil["Ukuran"] = (
        hasil["Ukuran"]
        .astype(str)
        .str.upper()
        .str.strip()
    )


    hasil["Harga"] = pd.to_numeric(
        hasil["Harga"],
        errors="coerce"
    )

    return hasil




# ==================================================
# HELPER
# ==================================================

def get_jenis(nama):


    if "SPIRAL PREMIUM" in nama:
        return "SPIRAL PREMIUM"

    elif "SPIRAL" in nama:
        return "SPIRAL"

    elif "SUPERFLEX" in nama:
        return "SUPERFLEX"

    elif "HIPREX" in nama:
        return "HIPREX"

    elif "DOF" in nama:
        return "DOF"

    elif "STABILO" in nama or "STABILLO" in nama:
        return "STABILO"

    elif "ELASTIS TEBAL" in nama:
        return "ELASTIS TEBAL"

    elif "TRANSPARAN" in nama:
        return "TRANSPARAN"

    elif "AIR HOSE" in nama:
        return "AIR HOSE"

    elif "LUBE" in nama:
        return "LUBE"

    return ""




def clean_ukuran(x):

    return (
        str(x)
        .upper()
        .replace('"',"")
        .replace("”","")
        .replace("″","")
        .replace("“","")
        .strip()
    )




def clean_harga(x):

    try:

        if pd.isna(x):
            return None


        x = (
            str(x)
            .replace(".","")
            .replace(",","")
            .strip()
        )


        return int(float(x))


    except:

        return None