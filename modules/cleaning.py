import streamlit as st
import pandas as pd

def clean_operation(df):

    df=st.session_state.df

         
    #Cleaning opeartion 
    st.markdown("## :rainbow[Cleaning] 🧹")
    st.info(
        "🛡️ Your original dataset is safe. "
        "All cleaning operations are performed on a copy of the uploaded data."
        )

    #Missing data

    #Replace Missing values with agg function

    if df.isna().sum().sum()>0:

         with st.expander("Replace Missing Values",width=650):
            replace_value=st.text_input("Replace All None with:")

            if replace_value:
                st.write(f"Replace All :red[None] with :green[{replace_value}] are you sure ?")

                if st.button(":green[Replace]",type="secondary",key="replace_missing"):
                    st.session_state.df=st.session_state.df.fillna(replace_value)
                    st.success("Values Replaced Successfully",icon="✅")
                    st.rerun()

            st.write("Aggregate Function For Numerical Columns")

            numeric_columns=[i for i in df.columns if df[i].dtypes in ["int32","int64","float32","float64"] ]

            selected_col=st.selectbox("Select Column",numeric_columns)

            if selected_col and df[selected_col].isna().sum()>0:

                if st.button(":green[Replace With Avarage]",type="secondary",key="replace_missing_mean"):
                    st.session_state.df[selected_col]=st.session_state.df[selected_col].fillna(df[selected_col].mean())
                    st.rerun()

                if st.button(":green[Replace With Minimum]",type="secondary",key="replace_missing_min"):
                    st.session_state.df[selected_col]=st.session_state.df[selected_col].fillna(df[selected_col].min())
                    st.rerun()

                if st.button(":green[Replace With Maximum]",type="secondary",key="replace_missing_max"):
                    st.session_state.df[selected_col]=st.session_state.df[selected_col].fillna(df[selected_col].max())
                    st.rerun()

                if st.button(":green[Replace With Median]",type="secondary",key="replace_missing_median"):
                    st.session_state.df[selected_col]=st.session_state.df[selected_col].fillna(df[selected_col].median())
                    st.rerun()

            else:

                st.write(f"There Is No Missing Valuses in {selected_col} Columns")
            
            

    # Drop Missing values
    if df.isna().sum().sum()>0:        

        with st.expander("Delete Missing Values",width=650):

            st.dataframe({
                            "Columns":df.columns,
                            "Missing Values":df.isna().sum()
                        },hide_index=True,width=300)

            if st.button("Delete NANs",type="primary",key="delete_nans"):
                # df.dropna(inplace=True)
                st.session_state.df=st.session_state.df.dropna()
                st.success("Missing Values Deleted Successfully",icon="✅")
                st.rerun()

                    
    #duplicate data    
    # Drop Duplicate rows                
    if (df.duplicated().sum()>0) or (df.T.duplicated().T.sum()>0):
        with st.expander("Delete Duplicates",width=650):

            if df.duplicated().sum()>0:

                st.write("Total Duplicated Rows:",df.duplicated().sum())
                if st.button("Delete Duplicates",type="primary",key="delete_duplecate_rows"):
                    st.session_state.df=st.session_state.df.drop_duplicates()
                    st.success("Duplicated Rows Deleted Successfully",icon="✅")
                    st.rerun()

            if df.T.duplicated().T.sum()>0:

                st.write("Total Duplicated Columns:",df.T.duplicated().T.sum())

                if st.button("Delete Duplicates",type="primary",key="delete_duplicate_columns"):

                    duplicate_columns = df.T.duplicated()

                    st.session_state.df = df.loc[:, ~duplicate_columns]
                    st.success("Duplicated Rows Deleted Successfully",icon="✅")
                    st.rerun()
                

    #Column operations
    #rename column
    with st.expander("Rename Columns",width=650):
        rename_col=st.selectbox("Available column to rename",df.columns)
        rename_val=st.text_input("Rename with:")
        st.write(f"Rename :red[{rename_col}] TO  :green[{rename_val}]")
        
        if st.button("Rename",type="primary",key="rename_columns"):
            st.session_state.df=st.session_state.df.rename(columns={rename_col:rename_val})
            st.success("Column Renamed Successfully",icon="✅")
            st.rerun()

    # change datatype

    if df.isna().sum().sum()==0:

        with st.expander("Change column datatype",width=650):

            selected_col=st.selectbox("Select Column",df.columns)

            converted=pd.to_datetime(df[selected_col],errors="coerce",format="mixed")
            num_converted=pd.to_numeric(df[selected_col],errors="coerce")

            current_dtype=df[selected_col].dtype
            unique_val=set(df[selected_col].unique())

            st.write("Current DataType:",current_dtype)
            
            #if int
            if (str(current_dtype) in ["int32","int64"]) and (len(unique_val)!=2):
                st.success("DataType Suggest : float64")
                selected_dtype=st.selectbox("Available Datatype",["int64","float64","object"])
                st.write(f":red[{current_dtype}] TO :green[{selected_dtype}]")

                if st.button("Change",key="change_int"): 
                    st.session_state.df[selected_col]=st.session_state.df[selected_col].astype(selected_dtype)
                    st.success("Data type converted")
                    st.rerun()
            # if float
            elif str(current_dtype) in ["float32","float64"]:
                st.success("DataType Suggest : int64")
                selected_dtype=st.selectbox("Available Datatype",["int64","float64","object"])
                st.write(f":red[{current_dtype}] TO :green[{selected_dtype}]")

                if st.button("Change",key="change_float"): 
                    st.session_state.df[selected_col]=st.session_state.df[selected_col].astype(selected_dtype)
                    st.success("Data type converted")
                    st.rerun()

            #if object or str or string
            elif (str(current_dtype) in ["object","str","string"]) and (num_converted.notna().all()) and (len(unique_val)!=2):
                st.success("DataType Suggest : int64")
                selected_dtype=st.selectbox("Available Datatype",["int64","float64"])

                st.write(f":red[{current_dtype}] TO :green[{selected_dtype}]")

                if st.button("Change",key="change_object_str"): 

                    if selected_dtype == "int64":

                        st.session_state.df[selected_col] = num_converted.astype("int64")

                    else:

                        st.session_state.df[selected_col] = num_converted.astype("float64")                        
                    st.success("Data type converted")
                    st.rerun()

            # to bool
            elif (
                (str(current_dtype) in ["int64","float64","object","str","string"])
                and (len(unique_val)==2)
                and (unique_val.issubset({0,1}))
                ):

                st.success("DataType Suggest : bool")
                selected_dtype=st.selectbox("Available Datatype",["int64","float64","bool"])
                st.write(f":red[{current_dtype}] TO :green[{selected_dtype}]")

                if st.button("Change",key="change_to_bool"):
                    st.session_state.df[selected_col]=st.session_state.df[selected_col].astype(selected_dtype)
                    st.success("Data type converted")
                    st.rerun()

                if selected_dtype != "bool":

                    st.warning("Make sure the selected datatype is compatible with the column values.")
                    
            elif (str(current_dtype)in ["int64","float64","object","str","string"]) and (len(df[selected_col].unique()) < len(df[selected_col])/2):
                st.success("DataType Suggest : catagory")
                selected_dtype=st.selectbox("Available Datatype",["category","object"])
                st.write(f":red[{current_dtype}] TO :green[{selected_dtype}]")
                if st.button("Change",key="change_category"): 
                    st.session_state.df[selected_col]=st.session_state.df[selected_col].astype(selected_dtype)
                    st.success("Data type converted")
                    st.rerun()

            elif (str(current_dtype) in ["int64","float64","object","str","string"]) and (converted.notna().all()):

                st.success("DataType Suggest : datetime")
                st.write(f":red[{current_dtype}] TO :green[datetime]")
                if st.button("Change",key="change_date_time"): 
                    st.session_state.df[selected_col]=converted
                    st.success("Data type converted")
                    st.rerun()
            
                    

            #if bool    
            elif (str(current_dtype) == "bool"):
                selected_dtype=st.selectbox("Available Datatype",["int64","float64","object"])
                st.write(f":red[{current_dtype}] TO :green[{selected_dtype}]")

                if st.button("Change",key="change_bool"): 
                    st.session_state.df[selected_col]=st.session_state.df[selected_col].astype(selected_dtype)
                    st.success("Data type converted")
                    st.rerun()

    #Advanced edit option

    if st.toggle("Edit a specific values"):
        edited_df=st.data_editor(st.session_state.df)

        if st.button(":green[Apply Changes]"):
            st.session_state.df=edited_df
            st.rerun()

    if st.toggle("See Changes"):
        st.dataframe(df.astype(str),width="stretch")

    if st.button("🔄 Reset All Changes"):
        st.session_state.df = st.session_state.original_df.copy()
        st.success("Dataset restored to its original state.")
        st.rerun()  