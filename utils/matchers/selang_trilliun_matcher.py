import pandas as pd
from utils.helper import bersihkan_text


def match_trilliun(row, df_trilliun):

    if df_trilliun is None or df_trilliun.empty:
        return pd.DataFrame()

    master_match = df_trilliun[
        (
            df_trilliun["Jenis"].apply(bersihkan_text)
            == bersihkan_text(row["Jenis"])
        )
        & (
            df_trilliun["Type"].apply(bersihkan_text)
            == bersihkan_text(row["Type"])
        )
        & (
            df_trilliun["Ukuran"].apply(bersihkan_text)
            == bersihkan_text(row["Ukuran"])
        )
    ]

    return master_match