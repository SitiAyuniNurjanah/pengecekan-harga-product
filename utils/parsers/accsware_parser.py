from utils.helper import bersihkan_text


def parse_accsware(text):

    text = bersihkan_text(text)

    result = {
        "brand": "ACCSWARE",
        "jenis": "AKSESORIS WARE",
        "type": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
    }

    return result