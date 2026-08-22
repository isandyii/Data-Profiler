import streamlit as st
import pandas as pd
import datetime

def data_report(data,df):

    # DATASET INFORMATION

    file_name=data.name    
    cols = df.columns
    none_val = df.isna().sum().sum()
    duplicates_rows = df.duplicated().sum()
    duplicates_cols = df.T.duplicated().sum()
    unique_cols = df.columns.unique()

    # HEALTH SCORE
    def health_score(df,cols,none_val,duplicates_rows,duplicates_cols,unique_cols):

        health = 100
        mixed_col = 0

        # Missing values
        if none_val != 0:
            health -= 30

        # Duplicate rows
        if duplicates_rows != 0:
            health -= 20

        # Duplicate columns
        if duplicates_cols != 0:
            health -= 15

        # Duplicate column names
        if len(unique_cols) != len(cols):
            health -= 15

        # Mixed datatypes
        for col in cols:

            if df[col].dropna().map(type).nunique() > 1:
                mixed_col += 1

        health -= mixed_col * 5

        # Minimum health score = 0
        health = max(0, health)

        return health, mixed_col


    # Calculate health
    health, mixed_col = health_score(
        df,
        cols,
        none_val,
        duplicates_rows,
        duplicates_cols,
        unique_cols
    )

    # STREAMLIT HEALTH SCORE

    st.markdown("## Dataset Health Score")

    st.metric(
        "Health",
        f"{health}/100",
        border=True
    )


    # DATASET SUMMARY


    st.markdown("## Dataset Summary")
    st.markdown(f"### File Name : :green[{file_name}]")

    st.write(df.describe(include="all").astype(str))


    # Problem detected


    st.markdown("## Problems Detected ⚠️")

    problems = []

    if none_val > 0:
        problems.append(
            "Dataset contains missing values"
        )

    if duplicates_rows > 0:
        problems.append(
            "Dataset contains duplicate rows"
        )

    if duplicates_cols > 0:
        problems.append(
            "Dataset contains duplicate columns"
        )

    if mixed_col > 0:
        problems.append(
            "Dataset contains mixed datatypes"
        )

    if problems:
        for problem in problems:
            st.write(
                f":yellow[{problem} !]"
            )

    else:
        st.success(
            "✅ No major problems detected"
        )

    # Recommendation

    st.markdown("## Recommendations 😉")
    recommendations = []

    if none_val > 0:
        recommendations.append(
            "Review and handle missing values"
        )

    if duplicates_rows > 0:
        recommendations.append(
            "Review and remove duplicate rows"
        )

    if duplicates_cols > 0:
        recommendations.append(
            "Review and remove duplicate columns"
        )

    if mixed_col > 0:
        recommendations.append(
            "Review columns with mixed datatypes"
        )

    if recommendations:
        for rec in recommendations:
            st.write(
                f":green[{rec} !]"
            )

    else:
        st.success(
            "✅ No recommendation"
        )


    #current date & time
    current_time = datetime.datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    # HTML REPORT

    def generate_html_report(df,health,problems,recommendations,file_name):

        # DATASET STATISTICS

        rows = len(df)
        columns = len(df.columns)
        total_cells = df.size
        missing_values = df.isna().sum().sum()
        duplicate_rows = df.duplicated().sum()
        duplicate_columns = df.T.duplicated().sum()

        # dataset health status

        if health >= 80:
            health_status = (
                "🟢 Dataset is in good condition"
            )

        elif health >= 50:
            health_status = (
                "🟡 Dataset needs some improvement"
            )

        else:

            health_status = (
                "🔴 Dataset needs significant cleaning"
            )

        # Problems HTML
        if problems:

            problems_html = ""

            for problem in problems:

                problems_html += f"""
                    <div class="problem">
                        ⚠️ {problem}
                    </div>
                """
        else:

            problems_html = """
                <div class="no-problem">
                    ✅ No major problems detected
                </div>
            """


        #recommendation HTML


        if recommendations:

            recommendations_html = ""

            for recommendation in recommendations:

                recommendations_html += f"""
                    <div class="recommendation">
                        💡 {recommendation}
                    </div>
                """

        else:

            recommendations_html = """
                <div class="no-recommendation">
                    ✅ No recommendation
                </div>
            """


        #HTML Section

        html = f"""
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Data Profiler Report</title>


    <style>

        * {{
            box-sizing: border-box;
        }}


        body {{

            font-family: Arial, sans-serif;

            margin: 0;

            padding: 40px;

            background-color: #f4f6f8;

            color: #222;

        }}


        .container {{

            max-width: 1000px;

            margin: auto;

            background-color: white;

            padding: 35px;

            border-radius: 15px;

            box-shadow:
                0 4px 15px
                rgba(0, 0, 0, 0.08);

        }}


        /* ================================
           HEADER
        ================================= */

        .header {{

            text-align: center;

            padding-bottom: 25px;

            border-bottom:
                2px solid #eeeeee;

        }}


        .header h1 {{

            margin: 0;

            font-size: 32px;

        }}


        .header p {{

            color: #777;

            margin-top: 10px;

        }}


        /* ================================
           HEADINGS
        ================================= */

        h2 {{

            margin-top: 35px;

            margin-bottom: 15px;

            padding-bottom: 8px;

            border-bottom:
                2px solid #eeeeee;

        }}


        /* ================================
           HEALTH SCORE
        ================================= */

        .health {{

            text-align: center;

            padding: 30px;

            margin-top: 20px;

            border-radius: 12px;

            background-color: #f0f8ff;

        }}


        .score {{

            font-size: 55px;

            font-weight: bold;

            margin-bottom: 10px;

        }}


        .health-status {{

            font-size: 18px;

            color: #555;

        }}


        /* ================================
           SUMMARY TABLE
        ================================= */

        .summary-table {{

            width: 100%;

            border-collapse: collapse;

            margin-top: 15px;

        }}


        .summary-table th,
        .summary-table td {{

            border:
                1px solid #dddddd;

            padding: 12px;

            text-align: left;

        }}


        .summary-table th {{

            background-color: #f1f1f1;

        }}


        .summary-table tr:hover {{

            background-color: #f9f9f9;

        }}


        /* ================================
           PROBLEMS
        ================================= */

        .problem {{

            padding: 13px;

            margin: 10px 0;

            background-color: #fff3cd;

            border-left:
                5px solid #ffc107;

            border-radius: 6px;

        }}


        .no-problem {{

            padding: 13px;

            background-color: #d4edda;

            border-left:
                5px solid #28a745;

            border-radius: 6px;

        }}


        /* ================================
           RECOMMENDATIONS
        ================================= */

        .recommendation {{

            padding: 13px;

            margin: 10px 0;

            background-color: #d4edda;

            border-left:
                5px solid #28a745;

            border-radius: 6px;

        }}


        .no-recommendation {{

            padding: 13px;

            background-color: #e2e3e5;

            border-left:
                5px solid #6c757d;

            border-radius: 6px;

        }}


        /* ================================
           FOOTER
        ================================= */

        .footer {{

            margin-top: 40px;

            padding-top: 20px;

            border-top:
                1px solid #dddddd;

            text-align: center;

            color: #777;

            font-size: 14px;

        }}


        /* ================================
           RESPONSIVE
        ================================= */

        @media (max-width: 600px) {{

            body {{

                padding: 15px;

            }}


            .container {{

                padding: 20px;

            }}


            .header h1 {{

                font-size: 25px;

            }}


            .score {{

                font-size: 40px;

            }}

        }}

    </style>

</head>


<body>


<div class="container">


    <!-- ==============================
         HEADER
    =============================== -->

    <div class="header">

        <h1>
            📊 Data Profiler Report
        </h1>

        <p>
            Generated by Data Profiler
        </p>

    </div>


    <!-- ==============================
         HEALTH SCORE
    =============================== -->

    <h2>
        File Name:<span style="color: #008000;">{file_name}</span>.
    </h2>

    <h2>
        Dataset Health Score
    </h2>


    <div class="health">

        <div class="score">

            {health}/100

        </div>


        <div class="health-status">

            {health_status}

        </div>

    </div>


    <!-- ==============================
         DATASET SUMMARY
    =============================== -->

    <h2>
        Dataset Summary
    </h2>


    <table class="summary-table">

        <tr>

            <th>
                Metric
            </th>

            <th>
                Value
            </th>

        </tr>


        <tr>

            <td>
                Rows
            </td>

            <td>
                {rows}
            </td>

        </tr>


        <tr>

            <td>
                Columns
            </td>

            <td>
                {columns}
            </td>

        </tr>


        <tr>

            <td>
                Total Cells
            </td>

            <td>
                {total_cells}
            </td>

        </tr>


        <tr>

            <td>
                Missing Values
            </td>

            <td>
                {missing_values}
            </td>

        </tr>


        <tr>

            <td>
                Duplicate Rows
            </td>

            <td>
                {duplicate_rows}
            </td>

        </tr>


        <tr>

            <td>
                Duplicate Columns
            </td>

            <td>
                {duplicate_columns}
            </td>

        </tr>

    </table>


    <!-- ==============================
         PROBLEMS
    =============================== -->

    <h2>
        ⚠️ Problems Detected
    </h2>


    {problems_html}


    <!-- ==============================
         RECOMMENDATIONS
    =============================== -->

    <h2>
        💡 Recommendations
    </h2>


    {recommendations_html}


    <!-- ==============================
         FOOTER
    =============================== -->

    <div class="footer">

        Data Profiler

        <br>

        Generated automatically

    </div>


</div>


</body>

</html>
"""

        return html


    #GENERATE REPORT

    html_report = generate_html_report(
        df,
        health,
        problems,
        recommendations,
        file_name
    )

    #download button

    st.download_button(

        label="📥 Download HTML Report",

        data=html_report,

        file_name=(
            f"data_profiler_report_"
            f"{current_time}.html"
        ),

        mime="text/html",

    )