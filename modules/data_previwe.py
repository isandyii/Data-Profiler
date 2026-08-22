import streamlit as st
import pandas as pd

def data_previwe(data,df):

    file_name=str(data).split("'")[3]
    trows=df.shape[0]
    tcol=df.shape[1]
    t_nan=df.isna().sum().sum()
    dup_r=df.duplicated().sum().sum()
    dup_c=df.T.duplicated().T.sum()
    size=data.size

    
    st.markdown("## Dataset Preview :eyes:")

    st.write(f"File Name :file_folder: : :green[{file_name}]")
    st.write(f"File Size  :floppy_disk: : :green[{size}] bytes")
    st.write(f"Shape :black_square_button: : :green[{df.shape}]")

    start,stop=st.slider(
        "Select The Range To Preview Dataset",
        min_value=0,
        max_value=len(df),
        value=(0,5),
        step=1
    )
    
    st.dataframe(df[start:stop].astype(str), width="stretch")
    st.write(":red[Note: This is only a preview. Changing the number of displayed rows does not modify the original dataset.]")

    st.markdown("## Data Overviwe :bar_chart:")

    rows, col, missing_val, d_row,d_col = st.columns(5)

    with rows:
        st.metric(":green[Rows]", trows,border=True)

    with col:
        st.metric(":green[Columns]", tcol,border=True)

    with missing_val:
        st.metric(":red[Missing Values]", t_nan,border=True)

    with d_row:
        st.metric(":red[Duplicate Rows]", dup_r,border=True)

    with d_col:
        st.metric(":red[Duplicate Columns]",dup_c,border=True)




    
    
        