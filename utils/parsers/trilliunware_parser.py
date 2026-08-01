def parse_trilliunware(text):

    text = str(text).upper().strip()

    result = {
        "brand": "TRILLIUNWARE",
        "jenis": "",
        "type": "",
        "varian": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
        "produk": "",
    }

    # ======================
    # VARIAN
    # ======================

    if "MALACHITE" in text:

        if "GARNET" in text:
            result["varian"] = "GARNET"

        elif "LILAC" in text:
            result["varian"] = "LILAC"

    # ======================
    # JENIS
    # ======================

    jenis_list = [
        "CLOSET DUDUK",
        "CLOSET JONGKOK",
        "WALL HUNG",
        "WASTAFEL",
        "URINAL",
        "SOAP DISH",
        "AVENA",
    ]

    for j in jenis_list:
        if j in text:
            result["jenis"] = j
            break

    # ======================
    # TYPE
    # ======================

    type_list = [
        "AMETHYST",
        "ANDALUZITE",
        "CHRYSOLITE",
        "COBALT",
        "CARRIBEAN",
        "CAPRI",
        "CITRINE",
        "EMERALD",
        "EUREKA",
        "GARNET",
        "HARVEST",
        "JASPER",
        "JUNIPER",
        "KROOZ",
        "LILAC",
        "MALACHITE",
        "MARION",
        "OBSIDIAN",
        "OPAL",
        "PERIDOT",
        "PYRITE",
        "RHODOLITE",
        "RUBY",
        "SAPPHIRA",
        "SODALITE",
        "SPENE",
        "TOURMALINE",
        "VELVET",
        "VISCARIA",
    ]

    for t in type_list:
        if t in text:
            result["type"] = t
            break

    # ======================
    # VARIAN
    # ======================

    if result["type"] == "MALACHITE":

        if "GARNET" in text:
            result["varian"] = "GARNET"

        elif "LILAC" in text:
            result["varian"] = "LILAC"

    # ======================
    # WARNA
    # ======================

    warna_list = [
        "BRILLIANT WHITE",
        "WHITE",
        "IVORY",
        "BLACK",
        "GREY",
        "MAROON",
        "LIGHT BLUE",
        "SORRENTO BLUE",
        "APPLE GREEN",
        "PINK",
    ]

    for w in warna_list:
        if w in text:
            result["warna"] = w
            break

    result["produk"] = text

    return result
