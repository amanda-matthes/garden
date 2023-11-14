import streamlit as st
import log_tools

st.write('# log')

refresh = st.button('refresh')
if refresh:
    log_tools.display()
else:
    log_tools.display()

clear = st.button('clear')
if clear:
    log_tools.clear()
