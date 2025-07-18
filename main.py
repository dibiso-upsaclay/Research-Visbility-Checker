import streamlit as st
from os import path

from utilitaire import read_markdown_file

st.set_page_config("Research Visibility Checker", layout="wide")

st.markdown("""
<div style="text-align: center;">
    <h1>Bienvenue sur Research Visibility Checker !</h1>
</div>""", 
    unsafe_allow_html=True)

with st.expander("Présentation de l'application", expanded=False):
    st.markdown(read_markdown_file(r"md/presentation_app.md"), unsafe_allow_html=True)

st.divider()

def main():
    if "navigation" not in st.session_state:
        st.navigation([st.Page(path.relpath("pages/2_st_donnee.py"),title='Research Visibility Checker'), st.Page(path.relpath("pages/0_tutorial.py"),title='Tutoriel')]).run()
    else: 
        st.navigation([st.Page(path.relpath(f"pages/{st.session_state["navigation"]}"), title="Research Visibility Checker"), st.Page(path.relpath("pages/0_tutorial.py"),title='Tutoriel')]).run()

if __name__ == "__main__":
    main()
