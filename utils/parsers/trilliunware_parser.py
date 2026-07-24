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
        "EUREKA", "EMERALD", "CAPRI", "CARRIBEAN", "MARION",
        "RUBY", "SAPPHIRA", "OPAL", "JASPER", "HARVEST",
        "ANDALUZITE", "CHRYSOLITE", "RHODOLITE", "SODALITE",
        "SPENE", "MALACHITE", "GARNET", "COBALT", "LILAC",
        "KROOZ", "PYRITE", "JUNIPER", "TOURMALINE", "VISCARIA",
        "VELVET", "PARTISI", "CITRINE", "PERIDOT",
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
