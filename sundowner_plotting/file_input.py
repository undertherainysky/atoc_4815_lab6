import pandas as pd


# ATOC_4815/atoc_4815_lab6/data_files/wxobs20250213.txt
def read_file(file_name):
    url = "https://sundowner.colorado.edu/weather/atoc1/" + file_name

    df = pd.read_fwf(url, header=[0, 1], skiprows=[2])

    date_col = [c for c in df.columns if c[1] == "Date"][0]
    time_col = [c for c in df.columns if c[1] == "Time"][0]

    t = (
        df[time_col]
        .astype(str)
        .str.strip()
        .str.replace(r"a$", "AM", regex=True)
        .str.replace(r"p$", "PM", regex=True)
    )

    dt = pd.to_datetime(
        df[date_col].astype(str).str.strip() + " " + t,
        format="%m/%d/%y %I:%M%p",
        errors="coerce",
    )

    df = df.set_index(dt).drop(columns=[date_col, time_col])
    df.index.name = "datetime"

    df.columns = [
        "_".join([str(a).strip(), str(b).strip()]).replace(" ", "_").strip("_")
        for a, b in df.columns
    ]

    return df



if __name__ == "__main__":
    # Test 1: 
    test_df = read_file("wxobs20250213.txt")
    print(f"{test_df}")

    