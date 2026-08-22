import streamlit as st
import pandas as pd

def statestics(df):

    cols=df.columns
    numeric_cols=[i for i in cols if pd.to_numeric(df[i],errors="coerce").notna().all()]
    str_cols=[i for i in cols if not pd.to_numeric(df[i],errors="coerce").notna().all()]

    col1,col2=st.columns(2)

    with col1:
        # discriptive statestics
        with st.expander("Discriptive Statestics"):
            st.markdown("### Statistical Summary :chart_with_upwards_trend:")
            st.dataframe(df.describe(include="all").astype(str))

        #Central Tendency
        with st.expander("Central Tendency"):
            selected_col=st.selectbox("Select Column",cols,key="select_for_central_tendency")
            num_converted=pd.to_numeric(df[selected_col],errors="coerce")

            if num_converted.notna().all():
                st.metric("Average Value Of Column",num_converted.mean(),border=True)
                st.metric("Middle Value Of Column",num_converted.median(),border=True)
                st.write("Frequently Occurring Value:",num_converted.mode())
            else:
                st.info("Select Numerical Columns Only / Remove None Values!")

        #Dispersion
        with st.expander("Dispersion"):
            selected_col=st.selectbox("Select Column",cols,key="select_for_dispersion")
            num_converted=pd.to_numeric(df[selected_col],errors="coerce")

            if num_converted.notna().all():
                st.metric("Variance",num_converted.var(),border=True)
                st.metric("Standard Deviation",num_converted.std(),border=True)
                if df[selected_col].dtypes != "bool":
                    st.metric("Range",num_converted.max() - num_converted.min(),border=True)
                else:
                    st.metric("Range",1,border=True)
            else:
                st.info("Select Numerical Columns Only / Remove None Values!")

    with col2:
        #Distribution
        with st.expander("Distribution"):
            selected_col=st.selectbox("Select Column",cols,key="select_for_distribution")
            num_converted=pd.to_numeric(df[selected_col],errors="coerce")
    
            if num_converted.notna().all():
                st.metric("Skewness",num_converted.skew(),border=True)
                st.metric("Kurtosis",num_converted.kurt(),border=True)
            else:
                st.info("Select Numerical Columns Only / Remove None Values!")
    
        #Correlation
        with st.expander("Correlation"):
        
            if num_converted.notna().all():
                st.write(df[numeric_cols].corr())
    
                st.write("Given Columns have A String Values Cant Correlation")
                st.dataframe(
                    {
                        "Columns":str_cols,
                        "Data Type":df[str_cols].dtypes.astype(str)
                        },
                    hide_index=True,
                    width=350
                )
                
            else:
                st.info("Column Should Not Have None Values")
            
    
    
