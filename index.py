import streamlit as st
import time

with st.empty():
    for seconds in range(20):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write(":material/check: voce perdeu 20 segundos da sua vida!")
st.button("Rerun")