import pandas as pd
from utils.helper import bersihkan_text


def match_fitting_basic(row, df_fitting_basic):

    master_match = df_fitting_basic[
        (
            df_fitting_basic["Jenis"].apply(bersihkan_text)
            == bersihkan_text(row["Jenis"])
        )
        & (
            df_fitting_basic["Type"].apply(bersihkan_text)
            == bersihkan_text(row["Type"])
        )
        & (
            df_fitting_basic["Ukuran"].apply(bersihkan_text)
            == bersihkan_text(row["Ukuran"])
        )
    ]

    return master_match