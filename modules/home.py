import streamlit as st

def show_home():
    st.title("CSV Data Profiler 📊")
    st.write(
        ":green[Discover. Clean. Analyze. Visualize. Your data journey starts here.]"
        )

    st.markdown("### Description :memo:")  
    st.write(
        '''Data Profiler is a portfolio-quality data analysis application 
        developed entirely from scratch using Python. 
        It empowers users to upload CSV datasets, 
        assess data quality, explore statistical insights, 
        clean and transform data, create interactive visualizations, 
        and generate comprehensive reports. 
        The project emphasizes clean architecture, modular development, 
        and hands-on implementation without using automated profiling libraries, 
        showcasing strong Python programming and data analysis skills.'''
        )

    st.markdown("### Built With:")

    st.code(
        "Python | Pandas | NumPy | Matplotlib | Streamlit"
        )

    if st.button("Explore :rocket:",type="primary"):
        st.session_state.explore=True
        st.rerun()
        
         
