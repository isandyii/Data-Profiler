# import streamlit as st

# def show_home():
#     st.title("Data Profiler 📊")
#     st.write(
#         ":green[Discover. Clean. Analyze. Visualize. Your data journey starts here.]"
#         )

#     st.markdown("### Description :memo:")  
#     st.write(
#         '''Data Profiler is a portfolio-quality data analysis application 
#         developed entirely from scratch using Python. 
#         It empowers users to upload CSV or Excel datasets, 
#         assess data quality, explore statistical insights, 
#         clean and transform data, create interactive visualizations, 
#         and generate comprehensive reports. 
#         The project emphasizes clean architecture, modular development, 
#         and hands-on implementation without using automated profiling libraries, 
#         showcasing strong Python programming and data analysis skills.'''
#         )

#     st.markdown("### Built With:")

#     st.code(
#         "Python | Pandas | NumPy | Matplotlib | Streamlit"
#         )

#     if st.button("Explore :rocket:",type="primary"):
#         st.session_state.explore=True
#         st.rerun()import streamlit as st


import streamlit as st
import base64


def show_home():

    # =========================================================
    # LOGO
    # =========================================================

    with open("assets/image1.png", "rb") as image_file:
        logo = base64.b64encode(image_file.read()).decode()


    # =========================================================
    # CUSTOM CSS
    # =========================================================

    st.html("""
    <style>
     /* =========================================================
    WHAT'S NEW
    ========================================================= */

    .home-new {

        min-height: 180px;

        padding: 27px 24px;

        margin-bottom: 20px;

        border-radius: 22px;

        background:
            rgba(255,255,255,0.62);

        backdrop-filter: blur(14px);

        border:
            1px solid rgba(255,255,255,0.7);

        box-shadow:
            0 12px 35px rgba(60,60,120,0.08);

        position: relative;

        overflow: hidden;

        transition:
            transform 0.35s ease,
            box-shadow 0.35s ease;
    }


    .home-new::before {

        content: "";

        position: absolute;

        top: 0;
        left: 0;

        width: 100%;
        height: 4px;

        background:
            linear-gradient(
                90deg,
                #ff6ec4,
                #7873f5,
                #4facfe,
                #00f2fe
            );

        background-size: 300% 300%;

        animation:
            gradientFlow 5s ease infinite;
    }


    .home-new:hover {

        transform:
            translateY(-7px);

        box-shadow:
            0 22px 45px rgba(60,60,120,0.14);
    }


    .home-new-icon {

        font-size: 25px;

        margin-bottom: 14px;
    }


    .home-new-title {

        font-size: 18px;

        font-weight: 800;

        color: #292c36;

        margin-bottom: 8px;
    }


    .home-new-text {

        font-size: 14px;

        line-height: 1.6;

        color: #747986;
    }
    

    /* =========================================================
       MAIN CONTAINER
    ========================================================= */

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* =========================================================
       HERO
    ========================================================= */

    .home-hero {

        position: relative;

        overflow: hidden;

        padding: 55px 35px;

        margin: 10px 0 35px 0;

        text-align: left;

        border-radius: 28px;

        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.11),
                rgba(255,255,255,0.035)
            );

        border:
            1px solid rgba(255,255,255,0.16);

        backdrop-filter:
            blur(18px);

        -webkit-backdrop-filter:
            blur(18px);

        box-shadow:
            0 20px 60px rgba(0,0,0,0.18);

        animation:
            heroIn 1s ease;
    }


    /* =========================================================
       HERO GLOW
    ========================================================= */

    .home-hero::before {

        content: "";

        position: absolute;

        width: 230px;
        height: 230px;

        border-radius: 50%;

        top: -100px;
        left: -80px;

        background: #ff6ec4;

        filter: blur(80px);

        opacity: 0.20;

        animation:
            glowMove 7s ease-in-out infinite;
    }


    .home-hero::after {

        content: "";

        position: absolute;

        width: 260px;
        height: 260px;

        border-radius: 50%;

        bottom: -140px;
        right: -90px;

        background: #4facfe;

        filter: blur(80px);

        opacity: 0.20;

        animation:
            glowMove2 8s ease-in-out infinite;
    }


    /* =========================================================
       BRAND
    ========================================================= */

    .home-brand {

        position: relative;

        z-index: 2;

        display: flex;

        align-items: center;

        justify-content: flex-start;

        gap: 18px;

        margin-bottom: 28px;
    }


    .home-logo {

        width: 78px;
        height: 78px;

        object-fit: contain;

        border-radius: 18px;

        animation:
            logoFloat 4s ease-in-out infinite;

        transition:
            transform 0.3s ease;
    }


    .home-logo:hover {

        transform:
            scale(1.08);
    }


    .home-brand-name {

        font-size: clamp(30px, 5vw, 60px);

        font-weight: 900;

        letter-spacing: -2px;

        line-height: 1;

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


    /* =========================================================
       BADGE
    ========================================================= */

    .home-badge {

        position: relative;

        z-index: 2;

        display: inline-block;

        padding: 8px 15px;

        border-radius: 50px;

        background:
            rgba(255,255,255,0.07);

        border:
            1px solid rgba(255,255,255,0.16);

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 1.5px;

        opacity: 0.75;

        margin-bottom: 18px;
    }


    /* =========================================================
       HERO HEADING
    ========================================================= */

    .home-heading {

        position: relative;

        z-index: 2;

        max-width: 850px;

        font-size: clamp(38px, 6vw, 30px);

        font-weight: 900;

        line-height: 1.08;

        letter-spacing: -2px;

        background:
            linear-gradient(
                90deg,
                #ff6ec4,
                #7873f5,
                #4facfe,
                #00f2fe
            );

        background-size: 300% 300%;

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;

        animation:
            gradientFlow 7s ease infinite;
    }


    /* =========================================================
       HERO DESCRIPTION
    ========================================================= */

    .home-description {

        position: relative;

        z-index: 2;

        max-width: 760px;

        margin-top: 20px;

        font-size: 16px;

        line-height: 1.8;

        opacity: 0.68;
    }


    /* =========================================================
       NOTE
    ========================================================= */

    .home-note {

        margin-top: 16px;

        font-size: 12px;

        opacity: 0.48;

        text-align: left;
    }


    /* =========================================================
       SECTION
    ========================================================= */

    .home-section {

        text-align: left;

        font-size: 28px;

        font-weight: 850;

        margin: 55px 0 10px;
    }


    .home-section-label {

        text-align: left;

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 2px;

        text-transform: uppercase;

        opacity: 0.55;

        margin-bottom: 8px;
    }


    .home-section-line {

        width: 70px;

        height: 3px;

        margin: 0 0 28px 0;

        border-radius: 20px;

        background:
            linear-gradient(
                90deg,
                #ff6ec4,
                #7873f5,
                #4facfe
            );

        animation:
            linePulse 2s ease-in-out infinite;
    }


    /* =========================================================
       FEATURE CARD
    ========================================================= */

    .home-feature {

        min-height: 190px;

        padding: 26px;

        border-radius: 22px;

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

        -webkit-backdrop-filter:
            blur(14px);

        transition:
            all 0.35s ease;

        animation:
            cardIn 0.7s ease;
    }


    .home-feature:hover {

        transform:
            translateY(-9px);

        border-color:
            rgba(255,255,255,0.38);

        box-shadow:
            0 18px 42px rgba(0,0,0,0.22);
    }


    .home-feature-number {

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 1px;

        opacity: 0.45;

        margin-bottom: 15px;
    }


    .home-feature-icon {

        font-size: 32px;

        margin-bottom: 10px;

        transition:
            transform 0.4s ease;
    }


    .home-feature:hover
    .home-feature-icon {

        transform:
            scale(1.2)
            rotate(7deg);
    }


    .home-feature-title {

        font-size: 18px;

        font-weight: 800;

        margin-bottom: 8px;
    }


    .home-feature-text {

        font-size: 13px;

        line-height: 1.6;

        opacity: 0.62;
    }


    /* =========================================================
       STATISTICS
    ========================================================= */

    .home-stats {

        display: grid;

        grid-template-columns:
            repeat(4, 1fr);

        gap: 15px;

        margin-top: 35px;
    }


    .home-stat {

        padding: 24px 15px;

        border-radius: 20px;

        text-align: left;

        background:
            rgba(255,255,255,0.065);

        border:
            1px solid rgba(255,255,255,0.13);

        backdrop-filter:
            blur(14px);

        transition:
            all 0.35s ease;
    }


    .home-stat:hover {

        transform:
            translateY(-8px)
            scale(1.03);

        border-color:
            rgba(255,255,255,0.38);

        box-shadow:
            0 18px 40px rgba(0,0,0,0.20);
    }


    .home-stat-number {

        font-size: 30px;

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


    .home-stat-label {

        margin-top: 4px;

        font-size: 12px;

        opacity: 0.58;
    }


    /* =========================================================
       WORKFLOW
    ========================================================= */

    .home-workflow {

        display: grid;

        grid-template-columns:
            repeat(4, 1fr);

        gap: 15px;
    }


    .home-step {

        padding: 25px;

        border-radius: 21px;

        background:
            rgba(255,255,255,0.065);

        border:
            1px solid rgba(255,255,255,0.13);

        backdrop-filter:
            blur(14px);

        transition:
            all 0.35s ease;
    }


    .home-step:hover {

        transform:
            translateY(-8px);

        background:
            rgba(255,255,255,0.12);

        border-color:
            rgba(255,255,255,0.38);

        box-shadow:
            0 15px 35px rgba(0,0,0,0.20);
    }


    .home-step-number {

        font-size: 11px;

        font-weight: 800;

        opacity: 0.45;

        margin-bottom: 14px;
    }


    .home-step-icon {

        font-size: 28px;

        margin-bottom: 8px;
    }


    .home-step-title {

        font-size: 16px;

        font-weight: 800;

        margin-bottom: 7px;
    }


    .home-step-text {

        font-size: 13px;

        line-height: 1.55;

        opacity: 0.62;
    }


    /* =========================================================
       TECHNOLOGIES
    ========================================================= */

    .home-tech-container {

        display: flex;

        justify-content: flex-start;

        flex-wrap: wrap;

        gap: 10px;
    }


    .home-tech {

        padding: 10px 17px;

        border-radius: 50px;

        background:
            rgba(255,255,255,0.065);

        border:
            1px solid rgba(255,255,255,0.14);

        font-size: 13px;

        opacity: 0.75;

        transition:
            all 0.3s ease;
    }


    .home-tech:hover {

        transform:
            translateY(-4px);

        opacity: 1;

        border-color:
            rgba(255,255,255,0.40);

        background:
            rgba(255,255,255,0.12);
    }


    /* =========================================================
       CTA
    ========================================================= */

    .home-cta {

        position: relative;

        overflow: hidden;

        margin-top: 65px;

        padding: 45px 30px;

        text-align: left;

        border-radius: 25px;

        background:
            linear-gradient(
                135deg,
                rgba(255,110,196,0.09),
                rgba(79,172,254,0.09)
            );

        border:
            1px solid rgba(255,255,255,0.15);

        backdrop-filter:
            blur(15px);

        transition:
            all 0.35s ease;
    }


    .home-cta:hover {

        transform:
            translateY(-5px);

        box-shadow:
            0 20px 50px rgba(0,0,0,0.20);
    }


    .home-cta-title {

        font-size: 32px;

        font-weight: 900;

        margin-bottom: 10px;
    }


    .home-cta-text {

        font-size: 15px;

        opacity: 0.62;

        margin-bottom: 22px;
    }


    /* =========================================================
       FOOTER
    ========================================================= */

    .home-footer {

        text-align: left;

        margin-top: 60px;

        padding-top: 22px;

        border-top:
            1px solid rgba(255,255,255,0.12);

        font-size: 11px;

        opacity: 0.45;
    }


    /* =========================================================
       ANIMATIONS
    ========================================================= */

    @keyframes heroIn {

        from {

            opacity: 0;

            transform:
                translateY(30px)
                scale(0.97);
        }

        to {

            opacity: 1;

            transform:
                translateY(0)
                scale(1);
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

        0%,100% {
            transform:
                translate(0,0);
        }

        50% {
            transform:
                translate(120px,70px);
        }
    }


    @keyframes glowMove2 {

        0%,100% {
            transform:
                translate(0,0);
        }

        50% {
            transform:
                translate(-120px,-70px);
        }
    }


    @keyframes logoFloat {

        0%,100% {
            transform:
                translateY(0);
        }

        50% {
            transform:
                translateY(-7px);
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


    @keyframes cardIn {

        from {

            opacity: 0;

            transform:
                translateY(20px);
        }

        to {

            opacity: 1;

            transform:
                translateY(0);
        }
    }


    /* =========================================================
       TABLET
    ========================================================= */

    @media(max-width: 800px) {

        .home-hero {

            padding:
                45px 25px;
        }


        .home-brand {

            gap: 13px;
        }


        .home-logo {

            width: 62px;
            height: 62px;
        }


        .home-brand-name {

            font-size: 55px;
        }


        .home-heading {

            font-size: 30px;
        }


        .home-stats {

            grid-template-columns:
                repeat(2, 1fr);
        }


        .home-workflow {

            grid-template-columns:
                repeat(2, 1fr);
        }
    }


    /* =========================================================
       MOBILE
    ========================================================= */

    @media(max-width: 600px) {

        .block-container {

            padding-left: 1rem;
            padding-right: 1rem;

            padding-top: 1rem;
        }


        .home-hero {

            padding:
                32px 20px;

            margin-top: 5px;

            border-radius: 22px;
        }


        .home-brand {

            gap: 10px;

            margin-bottom: 22px;
        }


        .home-logo {

            width: 48px;
            height: 48px;

            border-radius: 12px;
        }


        .home-brand-name {

            font-size: 27px;

            letter-spacing:
                -1px;
        }


        .home-badge {

            font-size: 9px;

            padding:
                7px 11px;

            letter-spacing:
                1px;
        }


        .home-heading {

            font-size: 35px;

            letter-spacing:
                -1.2px;

            line-height:
                1.12;
        }


        .home-description {

            font-size: 14px;

            line-height:
                1.7;
        }


        .home-note {

            font-size: 11px;
        }


        .home-section {

            font-size: 24px;

            margin-top: 42px;
        }


        .home-feature {

            min-height: auto;

            padding: 22px;

            border-radius: 19px;
        }


        .home-feature-icon {

            font-size: 28px;
        }


        .home-feature-title {

            font-size: 17px;
        }


        .home-feature-text {

            font-size: 13px;
        }


        .home-stats {

            grid-template-columns:
                1fr 1fr;

            gap: 10px;
        }


        .home-stat {

            padding:
                19px 14px;

            border-radius: 17px;
        }


        .home-stat-number {

            font-size: 25px;
        }


        .home-stat-label {

            font-size: 11px;
        }


        .home-workflow {

            grid-template-columns:
                1fr;

            gap: 12px;
        }


        .home-step {

            padding: 21px;

            border-radius: 18px;
        }


        .home-tech-container {

            gap: 8px;
        }


        .home-tech {

            padding:
                8px 13px;

            font-size: 12px;
        }


        .home-cta {

            margin-top: 45px;

            padding:
                30px 20px;

            border-radius: 21px;
        }


        .home-cta-title {

            font-size: 25px;
        }


        .home-cta-text {

            font-size: 14px;

            line-height:
                1.6;
        }


        .home-footer {

            margin-top: 45px;

            font-size: 10px;
        }
    }


    /* =========================================================
       VERY SMALL PHONES
    ========================================================= */

    @media(max-width: 380px) {

        .home-brand-name {

            font-size: 23px;
        }


        .home-logo {

            width: 42px;
            height: 42px;
        }


        .home-heading {

            font-size: 31px;
        }


        .home-stats {

            grid-template-columns:
                1fr;
        }
    }

    </style>
    """)


    # =========================================================
    # HERO
    # =========================================================

    st.html(f"""
    <div class="home-hero">

        <div class="home-brand">


            <div class="home-brand-name">
                Data Profiler
            </div>
            
            <img
                class="home-logo"
                src="data:image/png;base64,{logo}"
            >

        </div>


        <div class="home-badge">
            DATA INTELLIGENCE WORKSPACE
        </div>


        <div class="home-heading">
            Turn Raw Data Into
            Meaningful Insights
        </div>


        <div class="home-description">
            Explore, clean, analyze and visualize your datasets
            through one powerful and intuitive data profiling workspace.
        </div>

    </div>
    """)


    # =========================================================
    # LAUNCH BUTTON
    # =========================================================

    if st.button(
        "Launch Data Profiler  →",
        type="primary",
        width="stretch"
    ):

        st.session_state.explore = True

        st.rerun()


    st.html("""
    <div class="home-note">
        ✦ No setup complexity • Upload your CSV or Excel • Start analyzing
    </div>
    """)


    # =========================================================
    # FEATURES
    # =========================================================

    st.html("""
    <div class="home-section-label">
        Powerful Workspace
    </div>

    <div class="home-section">
        Everything You Need For Better Data
    </div>

    <div class="home-section-line"></div>
    """)


    features = [

        (
            "01",
            "🔎",
            "Explore",
            "Understand dataset structure, columns, data types, "
            "missing values and unique values before making changes."
        ),

        (
            "02",
            "✨",
            "Clean",
            "Detect duplicates, handle missing values, rename "
            "columns and transform your dataset with confidence."
        ),

        (
            "03",
            "📊",
            "Analyze",
            "Generate statistics, visualize distributions and "
            "discover patterns hidden inside your data."
        )
    ]


    for i in range(0, len(features), 3):

        cols = st.columns(3)

        for j, col in enumerate(cols):

            if i + j >= len(features):
                continue

            number, icon, title, text = features[i + j]

            with col:

                st.html(f"""
                <div class="home-feature">

                    <div class="home-feature-number">
                        {number}
                    </div>

                    <div class="home-feature-icon">
                        {icon}
                    </div>

                    <div class="home-feature-title">
                        {title}
                    </div>

                    <div class="home-feature-text">
                        {text}
                    </div>

                </div>
                """)


    # =========================================================
    # STATS
    # =========================================================

    st.html("""
    <div class="home-stats">

        <div class="home-stat">

            <div class="home-stat-number">
                CSV + XLSX
            </div>

            <div class="home-stat-label">
                Dataset Support
            </div>

        </div>


        <div class="home-stat">

            <div class="home-stat-number">
                100%
            </div>

            <div class="home-stat-label">
                Interactive
            </div>

        </div>


        <div class="home-stat">

            <div class="home-stat-number">
                ∞
            </div>

            <div class="home-stat-label">
                Data Possibilities
            </div>

        </div>


        <div class="home-stat">

            <div class="home-stat-number">
                1
            </div>

            <div class="home-stat-label">
                Unified Workspace
            </div>

        </div>

    </div>
    """)


    # =========================================================
    # WORKFLOW
    # =========================================================

    st.html("""
    <div class="home-section-label">
        Simple Workflow
    </div>

    <div class="home-section">
        From Dataset To Insight
    </div>

    <div class="home-section-line"></div>
    """)


    steps = [

        (
            "01",
            "📂",
            "Upload",
            "Import your dataset into the workspace."
        ),

        (
            "02",
            "🔎",
            "Inspect",
            "Understand structure and identify data issues."
        ),

        (
            "03",
            "🧹",
            "Transform",
            "Clean and prepare your data for analysis."
        ),

        (
            "04",
            "📈",
            "Discover",
            "Visualize patterns and generate insights."
        )
    ]


    for i in range(0, len(steps), 4):

        cols = st.columns(4)

        for j, col in enumerate(cols):

            if i + j >= len(steps):
                continue

            number, icon, title, text = steps[i + j]

            with col:

                st.html(f"""
                <div class="home-step">

                    <div class="home-step-number">
                        STEP {number}
                    </div>

                    <div class="home-step-icon">
                        {icon}
                    </div>

                    <div class="home-step-title">
                        {title}
                    </div>

                    <div class="home-step-text">
                        {text}
                    </div>

                </div>
                """)


    # =========================================================
    # WHAT'S NEW
    # =========================================================
    
    st.html("""
    <div class="home-section-label">
        Latest Update
    </div>
    
    <div class="home-section">
        ✨ What's New
    </div>
    
    <div class="home-section-line"></div>
    """)
    
    
    new_features = [
    
        (
            "🆕",
            "CSV + Excel Support",
            "You can now upload and work with both CSV "
            "and Excel files."
        ),
    
        (
            "🆕",
            "Aggregation-Based Missing Values",
            "Handle missing values using aggregation functions "
            "such as mean, median and other suitable methods."
        ),
    
        (
            "🆕",
            "Seaborn Integration",
            "Seaborn has been added for richer statistical "
            "data visualization."
        ),
    
        (
            "🆕",
            "Specific Value Editing",
            "Edit individual cells directly inside the dataset "
            "and apply your changes."
        ),
    
        (
            "🆕",
            "New UI",
            "A redesigned interactive interface provides a cleaner "
            "and more engaging data analysis experience."
        )
    ]
    
    
    for i in range(0, len(new_features), 3):
    
        cols = st.columns(3)
    
        for j, col in enumerate(cols):
        
            if i + j >= len(new_features):
                continue
            
            icon, title, text = new_features[i + j]
    
            with col:
            
                st.html(f"""
                <div class="home-new">
    
                    <div class="home-new-icon">
                        {icon}
                    </div>
    
                    <div class="home-new-title">
                        {title}
                    </div>
    
                    <div class="home-new-text">
                        {text}
                    </div>
    
                </div>
                """)
    
    # =========================================================
    # TECHNOLOGIES
    # =========================================================

    st.html("""
    <div class="home-section-label">
        Technology
    </div>

    <div class="home-section">
        Built With Modern Tools
    </div>

    <div class="home-section-line"></div>


    <div class="home-tech-container">

        <div class="home-tech">🐍 Python</div>

        <div class="home-tech">🐼 Pandas</div>

        <div class="home-tech">🔢 NumPy</div>

        <div class="home-tech">📊 Matplotlib</div>

        <div class="home-tech">⚡ Streamlit</div>

        <div class="home-tech">📈 Seaborn</div>

    </div>
    """)


    # =========================================================
    # CTA
    # =========================================================

    st.html("""
    <div class="home-cta">

        <div class="home-cta-title">
            Ready to understand your data?
        </div>

        <div class="home-cta-text">
            Upload your dataset and start exploring,
            cleaning and analyzing your data.
        </div>

    </div>
    """)


    if st.button(
        "Start Analyzing  →",
        type="primary",
        width="stretch"
    ):

        st.session_state.explore = True

        st.rerun()


    # =========================================================
    # FOOTER
    # =========================================================

    st.html("""
    <div class="home-footer">
        ✦ DATA PROFILER • EXPLORE • UNDERSTAND • IMPROVE ✦
    </div>
    """)


