import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def visualization(df):

    cols=df.columns

    numeric_cols=[i for i in cols if pd.to_numeric(df[i],errors="coerce").notna().all()]

    category_cols = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    try:
        selected_charts=st.multiselect(
            "Select Charts",
            [
                "Histogram",
                "Bar Chart",
                "Line Chart",
                "Scatter Plot",
                "Box Plot",
                "Pie Chart"
                ],
                accept_new_options=True

                )

        #Histogram
        if "Histogram" in selected_charts:

            st.title("Histogram")
            if not numeric_cols:

                st.warning("Histogram requires at least one numeric column.")
            else:

                title=st.text_input("Enter Title For Histogram")
                select_col=st.selectbox("Select Column",numeric_cols,key="for histogram")
                bins=int(st.number_input("Enter bins",min_value=1,value=10))

                fig, ax = plt.subplots()
                ax.hist(df[select_col],bins=bins,color="#f0fc0d",edgecolor="black",label=select_col)
                ax.legend()
                ax.set_title(title)
                ax.set_xlabel(select_col)
                ax.set_ylabel("Frequency")

                if st.toggle("Grid"):
                    ax.grid(True)
                st.pyplot(fig)

        #Bar chart
        if "Bar Chart" in selected_charts:
            st.title("Bar Chart")
            if not numeric_cols:
                st.warning("Bar Chart requires at least one numeric column.")   
            else:
                category=st.selectbox("Select X Axis Column",df.columns,key="bar x axis")
                numeric=st.selectbox("Select Y Axis Column",numeric_cols,key="bar y axis")

                st.bar_chart(df,x=category,y=numeric,color="#8e45d6",height=500)

        #Line Chart
        if "Line Chart" in selected_charts:

            st.title("Line Chart")

            if not numeric_cols:
                st.warning("Line Chart requires at least one numeric column.")

            else:
                linx_data=st.selectbox("Select X Axis Column",df.columns,key="line x axis")
                liny_data=st.selectbox("Select Y Axis Column",numeric_cols,key="line y axis")

                st.line_chart(df,x=linx_data,y=liny_data,color="#21dfd9")

        #Box Plot
        if "Box Plot" in selected_charts:

            st.title("Box Plot")

            if not numeric_cols:
                st.warning("Box Plot requires at least one numeric column.")

            else:
                data=st.selectbox("Select Column",numeric_cols,key="box plot")

                fig,ax=plt.subplots()
                ax.boxplot(df[data])
                st.pyplot(fig)

        #Scatter Plot
        if "Scatter Plot" in selected_charts:
            st.title("Scatter Plot")

            if len(numeric_cols)<2:

                st.warning("Scatter plot requires at least two numeric columns.")

            else:

                scatx=st.selectbox("Select X Axis Column",numeric_cols,key="scatx plot")
                scaty=st.selectbox("Select Y Axis Column",numeric_cols,key="scaty plot")

                st.scatter_chart(df,x=scatx,y=scaty,color="#ab19ff")

        #Pie Chart
        if ("Pie Chart" in selected_charts):

            st.title("Pie Chart")

            if not category_cols:

                st.warning("Pie charts requires at least one categorical columns.")
            else:
                selected_cat=st.selectbox("Select Categorys Column",category_cols,key="pie category")

                if df[selected_cat].nunique()>10:

                    st.warning("Pie chart is recommended for categorical columns with fewer than 10 categories.")

                else:
    
                    grouped = df[selected_cat].value_counts()

                    angle = st.slider("Rotate Chart",0,360)

                    colors = plt.cm.tab20(
                            np.linspace(0, 1, len(grouped))
                        )


                    fig,ax = plt.subplots()

                    ax.pie(grouped.values,
                           labels=grouped.index,
                           autopct="%0.1f%%",
                           colors=colors,
                           startangle=angle)

                    st.pyplot(fig)

    except Exception as e:
        st.error(f"Visualization Error: {e}")