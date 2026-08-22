import streamlit as st
import pandas as pd

def summery(df):

    columns=df.columns
    unique=[df.shape[0]-df[[i]].duplicated().sum() for i in df.columns]

    #column information
    st.markdown("## Columns Information :memo:")
    summary_df = pd.DataFrame({
        "Columns": df.columns.astype(str),
        "Data Types": df.dtypes.astype(str),
        "Missing Values": df.isna().sum().astype(int),
        "Unique Values": unique
    })

    st.dataframe(summary_df, hide_index=True,width="stretch")
    # st.write(data_summery)

    # missing values rows
    st.markdown("## :red[Missing Values Rows]")
    if df.isna().sum().sum()>0:
        st.warning("Missing Values Found !")
        st.dataframe(
            df[df.isna().any(axis=1)].astype(str),
            width="stretch"
            )

        #button for duplicate val
        if st.button("Show Duplicate Rows :repeat:"):
            st.write("Total Duplicates Rows : ",df.duplicated().sum())

        if st.button("Show Duplicate Columns :repeat:"):
            st.write("Total Duplicates Columns :",df.T.duplicated().T.sum())
    else:
        st.success("No Duplicates Row Found.")
