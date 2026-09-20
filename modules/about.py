
import streamlit as st


def about():

    # ============================================================
    # CUSTOM CSS + GRAPHICAL BACKGROUND
    # ============================================================

    st.html("""
    <style>

    /* =========================================================
       HERO
    ========================================================= */

    .dp-hero {
        position: relative;
        overflow: hidden;

        padding: 55px 30px;
        margin: 10px 0 30px 0;

        text-align: center;

        border-radius: 28px;

        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.11),
                rgba(255,255,255,0.035)
            );

        border: 1px solid rgba(255,255,255,0.16);

        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);

        box-shadow:
            0 20px 60px rgba(0,0,0,0.18);

        animation: heroIn 1s ease;
    }


    /* Animated glow */

    .dp-hero::before {
        content: "";

        position: absolute;

        width: 220px;
        height: 220px;

        border-radius: 50%;

        top: -100px;
        left: -70px;

        background: #ff6ec4;

        filter: blur(80px);

        opacity: 0.20;

        animation: glowMove 7s ease-in-out infinite;
    }


    .dp-hero::after {
        content: "";

        position: absolute;

        width: 250px;
        height: 250px;

        border-radius: 50%;

        bottom: -130px;
        right: -80px;

        background: #4facfe;

        filter: blur(80px);

        opacity: 0.20;

        animation: glowMove2 8s ease-in-out infinite;
    }


    .dp-title {

        position: relative;
        z-index: 2;

        font-size: clamp(40px, 6vw, 65px);

        font-weight: 900;

        letter-spacing: 3px;

        background:
            linear-gradient(
                90deg,
                #ff6ec4,
                #7873f5,
                #4facfe,
                #00f2fe,
                #ff6ec4
            );

        background-size: 400% 400%;

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        animation:
            gradientFlow 6s ease infinite;
    }


    .dp-subtitle {

        position: relative;
        z-index: 2;

        margin-top: 8px;

        font-size: 20px;

        font-weight: 650;

        opacity: 0.9;
    }


    .dp-description {

        position: relative;
        z-index: 2;

        max-width: 850px;

        margin: 15px auto 0;

        font-size: 15px;

        line-height: 1.8;

        opacity: 0.68;
    }


    /* =========================================================
       SECTION TITLE
    ========================================================= */

    .dp-section {

        text-align: center;

        font-size: 28px;

        font-weight: 800;

        margin: 45px 0 25px;
    }


    .dp-section-line {

        width: 70px;
        height: 3px;

        margin: -15px auto 25px;

        border-radius: 20px;

        background:
            linear-gradient(
                90deg,
                #ff6ec4,
                #7873f5,
                #4facfe
            );

        animation: linePulse 2s ease-in-out infinite;
    }


    /* =========================================================
       METRIC CARDS
    ========================================================= */

    .dp-metric {

        padding: 22px 10px;

        text-align: center;

        border-radius: 20px;

        background:
            rgba(255,255,255,0.065);

        border:
            1px solid rgba(255,255,255,0.13);

        backdrop-filter:
            blur(14px);

        transition:
            all 0.35s ease;
    }


    .dp-metric:hover {

        transform:
            translateY(-10px)
            scale(1.04);

        border-color:
            rgba(255,255,255,0.38);

        box-shadow:
            0 18px 40px rgba(0,0,0,0.22);
    }


    .dp-number {

        font-size: 34px;

        font-weight: 900;

        background:
            linear-gradient(
                90deg,
                #ff6ec4,
                #4facfe
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    .dp-label {

        font-size: 13px;

        opacity: 0.62;
    }


    /* =========================================================
       FEATURE CARDS
    ========================================================= */

    .dp-feature {

        min-height: 165px;

        padding: 24px;

        border-radius: 21px;

        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.09),
                rgba(255,255,255,0.035)
            );

        border:
            1px solid rgba(255,255,255,0.13);

        backdrop-filter:
            blur(14px);

        transition:
            all 0.35s ease;

        animation:
            cardIn 0.7s ease;
    }


    .dp-feature:hover {

        transform:
            translateY(-10px);

        border-color:
            rgba(255,255,255,0.38);

        box-shadow:
            0 18px 42px rgba(0,0,0,0.22);
    }


    .dp-feature-icon {

        font-size: 32px;

        margin-bottom: 10px;

        transition:
            transform 0.4s ease;
    }


    .dp-feature:hover .dp-feature-icon {

        transform:
            scale(1.25)
            rotate(8deg);
    }


    .dp-feature-title {

        font-size: 17px;

        font-weight: 750;
    }


    .dp-feature-text {

        margin-top: 7px;

        font-size: 13px;

        line-height: 1.55;

        opacity: 0.63;
    }


    /* =========================================================
       WORKFLOW
    ========================================================= */

    .dp-workflow-box {

        padding: 30px 20px;

        border-radius: 25px;

        background:
            rgba(255,255,255,0.055);

        border:
            1px solid rgba(255,255,255,0.13);

        backdrop-filter:
            blur(15px);
    }


    .dp-step {

        text-align: center;

        padding: 18px 8px;

        border-radius: 18px;

        background:
            rgba(255,255,255,0.075);

        border:
            1px solid rgba(255,255,255,0.12);

        transition:
            all 0.35s ease;
    }


    .dp-step:hover {

        transform:
            translateY(-8px)
            scale(1.04);

        background:
            rgba(255,255,255,0.15);

        box-shadow:
            0 12px 30px rgba(0,0,0,0.20);
    }


    .dp-step-icon {

        font-size: 30px;

        margin-bottom: 6px;
    }


    .dp-step-number {

        font-size: 10px;

        opacity: 0.45;
    }


    .dp-step-name {

        font-size: 13px;

        font-weight: 700;
    }


    .dp-arrow {

        text-align: center;

        padding-top: 35px;

        font-size: 22px;

        animation:
            arrowMove 1.5s ease-in-out infinite;
    }


    /* =========================================================
       SVG GRAPHIC
    ========================================================= */

    .dp-graphic {

        padding: 25px;

        border-radius: 25px;

        background:
            rgba(255,255,255,0.055);

        border:
            1px solid rgba(255,255,255,0.12);

        text-align: center;
    }


    .dp-graphic svg {

        width: 100%;

        max-width: 650px;

        height: auto;
    }


    .bar {

        transform-origin: bottom;

        animation:
            barAnimation 2s ease-in-out infinite alternate;
    }


    .bar2 {
        animation-delay: 0.2s;
    }

    .bar3 {
        animation-delay: 0.4s;
    }

    .bar4 {
        animation-delay: 0.6s;
    }

    .bar5 {
        animation-delay: 0.8s;
    }


    /* =========================================================
       TECHNOLOGIES
    ========================================================= */

    .dp-tech {

        text-align: center;

        padding: 23px 10px;

        border-radius: 20px;

        background:
            rgba(255,255,255,0.065);

        border:
            1px solid rgba(255,255,255,0.13);

        transition:
            all 0.35s ease;
    }


    .dp-tech:hover {

        transform:
            translateY(-8px)
            scale(1.04);

        background:
            rgba(255,255,255,0.12);

        box-shadow:
            0 12px 30px rgba(0,0,0,0.20);
    }


    .dp-tech-icon {

        font-size: 32px;
    }


    .dp-tech-name {

        margin-top: 8px;

        font-weight: 700;
    }


    /* =========================================================
       DEVELOPER
    ========================================================= */

    .dp-developer {

        text-align: center;

        padding: 35px;

        border-radius: 25px;

        background:
            linear-gradient(
                135deg,
                rgba(255,110,196,0.09),
                rgba(79,172,254,0.09)
            );

        border:
            1px solid rgba(255,255,255,0.15);

        transition:
            all 0.35s ease;
    }


    .dp-developer:hover {

        transform:
            translateY(-8px);

        box-shadow:
            0 20px 50px rgba(0,0,0,0.22);
    }


    .dp-avatar {

        width: 75px;
        height: 75px;

        margin: auto;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 50%;

        font-size: 32px;

        background:
            linear-gradient(
                135deg,
                #ff6ec4,
                #4facfe
            );

        animation:
            avatarPulse 2.5s ease-in-out infinite;
    }


    .dp-name {

        margin-top: 15px;

        font-size: 25px;

        font-weight: 850;
    }


    .dp-role {

        margin-top: 5px;

        font-size: 14px;

        opacity: 0.62;
    }


    /* =========================================================
       ANIMATIONS
    ========================================================= */

    @keyframes heroIn {

        from {
            opacity: 0;
            transform: translateY(30px) scale(0.97);
        }

        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }


    @keyframes gradientFlow {

        0% {
            background-position: 0% 50%;
        }

        50% {
            background-position: 100% 50%;
        }

        100% {
            background-position: 0% 50%;
        }
    }


    @keyframes glowMove {

        0%, 100% {
            transform: translate(0,0);
        }

        50% {
            transform: translate(120px,70px);
        }
    }


    @keyframes glowMove2 {

        0%, 100% {
            transform: translate(0,0);
        }

        50% {
            transform: translate(-120px,-70px);
        }
    }


    @keyframes linePulse {

        0%,100% {
            width: 55px;
        }

        50% {
            width: 100px;
        }
    }


    @keyframes arrowMove {

        0%,100% {
            transform: translateX(0);
            opacity: 0.35;
        }

        50% {
            transform: translateX(5px);
            opacity: 1;
        }
    }


    @keyframes cardIn {

        from {
            opacity: 0;
            transform: translateY(20px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }


    @keyframes avatarPulse {

        0%,100% {
            box-shadow:
                0 0 0 0 rgba(79,172,254,0.3);
        }

        50% {
            box-shadow:
                0 0 0 13px rgba(79,172,254,0);
        }
    }


    @keyframes barAnimation {

        from {
            transform: scaleY(0.65);
        }

        to {
            transform: scaleY(1);
        }
    }

    </style>
    """)


    # ============================================================
    # HERO
    # ============================================================

    st.html("""
    <div class="dp-hero">

        <div class="dp-title">
            DATA PROFILER
        </div>

        <div class="dp-subtitle">
            Understand Your Data Before You Analyze It
        </div>

        <div class="dp-description">
            An interactive application for exploring dataset structure,
            discovering data-quality issues, understanding statistical
            characteristics and generating meaningful profiling insights.
        </div>

    </div>
    """)


    # ============================================================
    # QUICK STATS
    # ============================================================

    cols = st.columns(4)

    metrics = [
        ("09+", "Profiling Features"),
        ("07", "Core Steps"),
        ("05", "Technologies"),
        ("01", "Unified Workflow")
    ]

    for col, (number, label) in zip(cols, metrics):

        with col:

            st.html(f"""
            <div class="dp-metric">

                <div class="dp-number">
                    {number}
                </div>

                <div class="dp-label">
                    {label}
                </div>

            </div>
            """)


    # ============================================================
    # FEATURES
    # ============================================================

    st.markdown(
        '<div class="dp-section">What Can You Do?</div>'
        '<div class="dp-section-line"></div>',
        unsafe_allow_html=True
    )


    features = [
        (
            "📋",
            "Dataset Overview",
            "Explore rows, columns, memory usage and dataset structure."
        ),

        (
            "🔎",
            "Column Profiling",
            "Inspect data types, unique values and column information."
        ),

        (
            "⚠️",
            "Missing Values",
            "Identify missing values and understand their distribution."
        ),

        (
            "♻️",
            "Duplicate Detection",
            "Find duplicate rows and duplicate columns."
        ),

        (
            "📊",
            "Statistical Analysis",
            "Explore descriptive statistics and numerical characteristics."
        ),

        (
            "📈",
            "Visualization",
            "Discover patterns and relationships through charts."
        ),

        (
            "🧹",
            "Data Cleaning",
            "Identify and fix common data-quality problems."
        ),

        (
            "❤️",
            "Health Score",
            "Understand the overall quality of your dataset."
        ),

        (
            "📥",
            "Export",
            "Download your cleaned dataset for further analysis."
        )
    ]


    for i in range(0, len(features), 3):

        cols = st.columns(3)

        for j, col in enumerate(cols):

            if i + j >= len(features):
                continue

            icon, title, description = features[i + j]

            with col:

                st.html(f"""
                <div class="dp-feature">

                    <div class="dp-feature-icon">
                        {icon}
                    </div>

                    <div class="dp-feature-title">
                        {title}
                    </div>

                    <div class="dp-feature-text">
                        {description}
                    </div>

                </div>
                """)


    # ============================================================
    # WORKFLOW
    # ============================================================

    st.markdown(
        '<div class="dp-section">Profiling Workflow</div>'
        '<div class="dp-section-line"></div>',
        unsafe_allow_html=True
    )


    workflow = [
        ("📂", "Upload"),
        ("🔎", "Profile"),
        ("📋", "Summary"),
        ("🧹", "Clean"),
        ("📊", "Analyze"),
        ("📈", "Visualize"),
        ("❤️", "Report")
    ]


    st.html("""
    <div class="dp-workflow-box">
        <div style="
            text-align:center;
            font-size:14px;
            opacity:0.65;
            margin-bottom:20px;
        ">
            From raw dataset to complete data-quality insights
        </div>
    </div>
    """)


    # Use native Streamlit columns for reliable layout

    workflow_cols = st.columns(13)

    for i, (icon, name) in enumerate(workflow):

        with workflow_cols[i * 2]:

            st.html(f"""
            <div class="dp-step">

                <div class="dp-step-icon">
                    {icon}
                </div>

                <div class="dp-step-number">
                    STEP {i + 1}
                </div>

                <div class="dp-step-name">
                    {name}
                </div>

            </div>
            """)

        if i < len(workflow) - 1:

            with workflow_cols[i * 2 + 1]:

                st.html("""
                <div class="dp-arrow">
                    ➜
                </div>
                """)


    # ============================================================
    # GRAPHICAL DATA PROFILING ILLUSTRATION
    # ============================================================

    st.markdown(
        '<div class="dp-section">Data Profiling at a Glance</div>'
        '<div class="dp-section-line"></div>',
        unsafe_allow_html=True
    )


    st.html("""
    <div class="dp-graphic">

        <svg
            viewBox="0 0 700 300"
            xmlns="http://www.w3.org/2000/svg"
        >

            <!-- Grid -->

            <line
                x1="80" y1="240"
                x2="650" y2="240"
                stroke="rgba(255,255,255,0.2)"
                stroke-width="2"
            />

            <line
                x1="80" y1="60"
                x2="80" y2="240"
                stroke="rgba(255,255,255,0.2)"
                stroke-width="2"
            />


            <!-- Bars -->

            <rect
                class="bar"
                x="130"
                y="125"
                width="55"
                height="115"
                rx="10"
                fill="#ff6ec4"
            />

            <rect
                class="bar bar2"
                x="225"
                y="95"
                width="55"
                height="145"
                rx="10"
                fill="#7873f5"
            />

            <rect
                class="bar bar3"
                x="320"
                y="145"
                width="55"
                height="95"
                rx="10"
                fill="#4facfe"
            />

            <rect
                class="bar bar4"
                x="415"
                y="80"
                width="55"
                height="160"
                rx="10"
                fill="#00c9ff"
            />

            <rect
                class="bar bar5"
                x="510"
                y="110"
                width="55"
                height="130"
                rx="10"
                fill="#00f2fe"
            />


            <!-- Labels -->

            <text
                x="157"
                y="270"
                fill="white"
                opacity="0.6"
                text-anchor="middle"
                font-size="13"
            >
                Missing
            </text>

            <text
                x="252"
                y="270"
                fill="white"
                opacity="0.6"
                text-anchor="middle"
                font-size="13"
            >
                Unique
            </text>

            <text
                x="347"
                y="270"
                fill="white"
                opacity="0.6"
                text-anchor="middle"
                font-size="13"
            >
                Duplicate
            </text>

            <text
                x="442"
                y="270"
                fill="white"
                opacity="0.6"
                text-anchor="middle"
                font-size="13"
            >
                Numeric
            </text>

            <text
                x="537"
                y="270"
                fill="white"
                opacity="0.6"
                text-anchor="middle"
                font-size="13"
            >
                Quality
            </text>

        </svg>

    </div>
    """)


    # ============================================================
    # INTERACTIVE INFORMATION
    # ============================================================

    st.markdown(
        '<div class="dp-section">Explore the Project</div>'
        '<div class="dp-section-line"></div>',
        unsafe_allow_html=True
    )


    tab1, tab2, tab3 = st.tabs([
        "🎯 Project Goal",
        "💡 Why Profiling?",
        "🚀 Future Scope"
    ])


    with tab1:

        st.markdown("""
        ### 🎯 Project Goal

        Data Profiler is designed to make the first stage of data analysis
        faster and easier.

        Instead of manually inspecting every column, the application
        provides important dataset information in one interactive
        environment.
        """)


    with tab2:

        st.markdown("""
        ### 💡 Why Data Profiling?

        Data profiling helps identify the characteristics and quality
        of a dataset before deeper analysis or machine learning.

        It helps answer questions such as:

        - How large is the dataset?
        - What data types are present?
        - Are there missing values?
        - Are there duplicate records?
        - How unique are the values?
        - What does the numerical data look like?
        """)


    with tab3:

        st.markdown("""
        ### 🚀 Future Scope

        Possible future improvements include:

        - Automated anomaly detection
        - ML-readiness score
        - PDF report generation
        """)


    # ============================================================
    # TECHNOLOGIES
    # ============================================================

    st.markdown(
        '<div class="dp-section">Built With</div>'
        '<div class="dp-section-line"></div>',
        unsafe_allow_html=True
    )


    technologies = [
        ("🐍", "Python"),
        ("⚡", "Streamlit"),
        ("🐼", "Pandas"),
        ("🔢", "NumPy"),
        ("📊", "Matplotlib"),
        ("📈","Seaborn")
    ]


    cols = st.columns(6)

    for col, (icon, name) in zip(cols, technologies):

        with col:

            st.html(f"""
            <div class="dp-tech">

                <div class="dp-tech-icon">
                    {icon}
                </div>

                <div class="dp-tech-name">
                    {name}
                </div>

            </div>
            """)


    # ============================================================
    # DEVELOPER
    # ============================================================

    st.markdown(
        '<div class="dp-section">Developer</div>'
        '<div class="dp-section-line"></div>',
        unsafe_allow_html=True
    )


    st.html("""
    <div class="dp-developer">

        <div class="dp-avatar">
            👨‍💻
        </div>

        <div class="dp-name">
            Sandesh Bonde
        </div>

        <div class="dp-role">
            B.Sc. Computer Science • MCA
        </div>

        <div class="dp-role">
            Python • Data Science • Data Profiling
        </div>

    </div>
    """)


    # ============================================================
    # FOOTER
    # ============================================================

    st.html("""
    <div style="
        text-align:center;
        margin:35px 0 10px;
        padding:18px;
        opacity:0.5;
        font-size:12px;
    ">
        ✦ DATA PROFILER • EXPLORE • UNDERSTAND • IMPROVE ✦
    </div>
    """)
