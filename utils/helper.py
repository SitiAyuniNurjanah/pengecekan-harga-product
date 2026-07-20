import pandas as pd
import re



# =====================================================
# BERSIHKAN HARGA
# =====================================================

def bersihkan_harga(harga):

    if pd.isna(harga):
        return None


    # =========================
    # JIKA SUDAH ANGKA DARI EXCEL
    # =========================

    if isinstance(harga, (int, float)):

        angka = float(harga)


        # contoh:
        # 1221000.0
        # 4100.0
        return int(round(angka))


    harga = str(harga).upper().strip()


    if harga == "":
        return None


    # hapus tulisan
    harga = harga.replace("RP", "")
    harga = harga.replace(" ", "")


    # ambil angka saja
    harga = re.sub(r"[^\d.,]", "", harga)


    if harga == "":
        return None



    # =================================================
    # FORMAT INDONESIA
    #
    # 1.256.610
    # 51.700
    # 19.750
    #
    # titik = pemisah ribuan
    # =================================================

    if "." in harga and "," not in harga:

        bagian = harga.split(".")


        # semua bagian setelah titik panjang 3
        # berarti titik ribuan

        if all(len(x) == 3 for x in bagian[1:]):

            harga = "".join(bagian)


        else:

            # kemungkinan desimal excel
            try:

                angka = float(harga)

                return int(round(angka))

            except:
                return None



    # =================================================
    # FORMAT:
    #
    # 1,256,610
    # 19,750
    #
    # koma = ribuan
    # =================================================

    if "," in harga:

        harga = harga.replace(",", "")



    try:

        return int(float(harga))


    except:

        return None





# =====================================================
# BERSIHKAN TEXT UNTUK MATCHING
# =====================================================

def bersihkan_text(text):

    if pd.isna(text):
        return ""


    text = str(text).upper().strip()


    # =========================
    # NORMALISASI KUTIP
    # =========================

    text = text.replace("”", '"')
    text = text.replace("“", '"')
    text = text.replace("'", '"')



    # =========================
    # NORMALISASI X
    # =========================

    text = text.replace(" X ", " x ")
    text = text.replace("X", "x")



    # =========================
    # NORMALISASI SPASI
    # =========================

    text = re.sub(
        r"\s+",
        " ",
        text
    )



    # =================================================
    # UKURAN PIPA
    #
    # 11/2"  -> 1 1/2"
    # 11/4"  -> 1 1/4"
    # 21/2"  -> 2 1/2"
    #
    # supaya master dan customer sama
    # =================================================

    text = re.sub(
        r"\b([1-9])1/([2-9])",
        r"\1 1/\2",
        text
    )



    # =========================
    # RAPIKAN X
    # =========================

    text = re.sub(
        r"\s*x\s*",
        " x ",
        text
    )


    # hapus spasi sebelum quote

    text = re.sub(
        r'\s+"',
        '"',
        text
    )


    return text.strip()