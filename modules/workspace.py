import streamlit as st
import pandas as pd
from modules import data_previwe as dp
from modules import summery as summ
from modules import cleaning as cln
from modules import statestics as stc
from modules import visualization as vis
from modules import report as rt
from modules import about as abt

def workspace():
    st.title("Data Profiler 📊")
    data=st.file_uploader("Select and upload your dataset file here:",type=["csv","xlsx"])


    if data:
        try:
            if data.name.split(".")[-1]=="csv":

                    if "original_df" not in st.session_state:
                        st.session_state.original_df=pd.read_csv(data)
                        st.session_state.df=st.session_state.original_df.copy()
                    df=st.session_state.df

                    st.success("File Uploaded Succsessfully")

            if data.name.split(".")[-1]=="xlsx":

                    if "original_df" not in st.session_state:
                        st.session_state.original_df=pd.read_excel(data)
                        st.session_state.df=st.session_state.original_df.copy()
                    df=st.session_state.df

                    st.success("File Uploaded Succsessfully")
                    

        except Exception as e:
                    st.error(e)    
                    # st.error("File Not readablbe! make sure file is CSV AND")    

        tab1,tab2,tab3,tab4,tab5,tab6,tab7=st.tabs([ "📂 Dataset Overview",
                                                "📋 Summary",
                                                "🧹 Cleaning",
                                                "📊 Statistics",
                                                "📈 Visualization",
                                                "📄 Report",
                                                "ℹ️ About"])
        with tab1:
             dp.data_previwe(data,df)
        with tab2:
            summ.summery(df)
        with tab3:
            cln.clean_operation(df)
        with tab4:
            stc.statestics(df)
        with tab5:
            vis.visualization(df)
        with tab6:
            rt.data_report(data,df)
        with tab7:
            abt.about()
    else :
        st.error("Upload The File First")