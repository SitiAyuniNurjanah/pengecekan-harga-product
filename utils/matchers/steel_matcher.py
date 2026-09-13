from utils.helper import bersihkan_text
import re

def match_steel(row, df_steel):


    if df_steel is None or df_steel.empty:
        return df_steel

    nama = bersihkan_text(row["Nama Barang"])

    master_match = df_steel.copy()

    # =========================
    # HOLLOW
    # =========================
    if "HOLLOW" in nama:

        master_match = master_match[
            master_match["Jenis"].str.upper() == "HOLLOW"
        ]

        # ambil ukuran dari pesanan
        ukuran_order = None

        ukuran = re.search(r"(\d+)\s*[Xx]\s*(\d+)", nama)

        if ukuran:
            ukuran_order = (
                ukuran.group(1) +
                "X" +
                ukuran.group(2)
            )


        if ukuran_order:

            master_match["ukuran_normal"] = (
                master_match["Ukuran"]
                .astype(str)
                .str.upper()
                .str.replace(" ", "", regex=False)
            )

            master_match = master_match[
                master_match["ukuran_normal"] == ukuran_order
            ]

    # =========================
    # BONDEK
    # =========================
    elif "BONDEK" in nama:

        master_match = master_match[
            master_match["Produk"].str.contains(
                "BONDEK",
                case=False,
                na=False,
            )
        ]

        if "6 M" in nama:
            master_match = master_match[
                master_match["Produk"].str.contains(
                    "6 M",
                    case=False,
                    na=False,
                )
            ]

    # =========================
    # CANAL / CANNAL
    # =========================
    elif "CANAL" in nama:

        master_match = master_match[
            master_match["Produk"].str.contains(
                "CANNAL",
                case=False,
                na=False,
            )
        ]

        if "75" in nama:
            master_match = master_match[
                master_match["Produk"].str.contains(
                    "75",
                    case=False,
                    na=False,
                )
            ]

        if "ECO" in nama:
            master_match = master_match[
                master_match["Produk"].str.contains(
                    "ECO",
                    case=False,
                    na=False,
                )
            ]

        elif "PREMIUM" in nama:
            master_match = master_match[
                master_match["Produk"].str.contains(
                    "PREMIUM",
                    case=False,
                    na=False,
                )
            ]

    # =========================
    # GALVALUM
    # =========================
    elif "GALVALUM" in nama:

        for kata in ["0.25", "0.30", "500", "600", "700", "914"]:

            if kata in nama:

                master_match = master_match[
                    master_match["Produk"].str.contains(
                        kata,
                        case=False,
                        na=False,
                    )
                ]

    # =========================
    # KASSO
    # =========================
    elif "KASSO" in nama:

        master_match = master_match[
            master_match["Produk"].str.contains(
                "KASSO",
                case=False,
                na=False,
            )
        ]

        if "28.25" in nama:
            master_match = master_match[
                master_match["Produk"].str.contains(
                    "28.25",
                    case=False,
                    na=False,
                )
            ]

        elif "28.30" in nama:
            master_match = master_match[
                master_match["Produk"].str.contains(
                    "28.30",
                    case=False,
                    na=False,
                )
            ]

        if "PREMIUM" in nama:
            master_match = master_match[
                master_match["Produk"].str.contains(
                    "PREMIUM",
                    case=False,
                    na=False,
                )
            ]

    # =========================
    # GENTENG METAL
    # =========================
    elif "GENTENG" in nama:

        master_match = master_match[
            master_match["Produk"].str.contains(
                "GENTENG METAL",
                case=False,
                na=False,
            )
        ]

        if "MERAH" in nama:
            master_match = master_match[
                master_match["Produk"].str.contains(
                    "MERAH",
                    case=False,
                    na=False,
                )
            ]

    # =========================
    # SENG GELOMBANG
    # =========================
    elif "SENG" in nama:

        master_match = master_match[
            master_match["Produk"].str.contains(
                "SENG GELOMBANG",
                case=False,
                na=False
            )
        ]

        if "180" in nama:
            ukuran = 1.8

        elif "210" in nama:
            ukuran = 2.1

        elif "240" in nama:
            ukuran = 2.4

        elif "300" in nama:
            ukuran = 3

        else:
            ukuran = None

    # =========================
    # SPANDEK PASIR
    # =========================
    elif "SPANDEK PASIR" in nama:

        master_match = master_match[
            master_match["Produk"].str.contains(
                "SPANDEK PASIR|PREMIUMDEK",
                case=False,
                na=False
            )
        ]


        # warna
        if "MERAH" in nama:
            master_match = master_match[
                master_match["Produk"].str.contains(
                    "MERAH",
                    case=False,
                    na=False
                )
            ]


        # feet
        if "4F" in nama or "4 F" in nama:

            master_match = master_match[
                master_match["Produk"].str.contains(
                    "4 FEET|4F",
                    case=False,
                    na=False
                )
            ]
            
    # =========================
    # SUTERA TRIMDEK
    # =========================
    elif "TRIMDEK" in nama:

        if "0.25" in nama or "0,25" in nama:

            master_match = master_match[
                master_match["Produk"].str.contains(
                    "TRIMDEK",
                    case=False,
                    na=False,
                )
            ]

            master_match = master_match[
                master_match["Produk"].str.contains(
                    "0.25",
                    case=False,
                    na=False,
                )
            ]

        elif "0.30" in nama or "0,30" in nama:

            master_match = master_match[
                master_match["Produk"].str.contains(
                    "PREMIUMDEK",
                    case=False,
                    na=False,
                )
            ]

            master_match = master_match[
                master_match["Produk"].str.contains(
                    "0.30",
                    case=False,
                    na=False,
                )
            ]
    if "SENG" in nama and not master_match.empty:

        if ukuran:

            harga_meter = master_match.iloc[0]["Harga Net"]

            harga_total = harga_meter * ukuran

            master_match = master_match.copy()

            master_match["Harga"] = harga_total

    return master_match