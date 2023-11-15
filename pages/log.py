import streamlit as st
import log_tools

from datetime import datetime

st.write('# log')

refresh = st.button('refresh')
if refresh:
    log_tools.display()
else:
    log_tools.display()

clear = st.button('clear')
if clear:
    log_tools.clear()


# DOWNLOAD OPTIONS
download = st.button('download')

if download: # prevents generating the csv all the time

    file_name = datetime.today().strftime('%Y-%m-%d_%H-%M')

    # DOWNLOAD AS JSON
    json_string = log_tools.get_json_string()
    st.json(json_string, expanded=True)

    st.download_button(
        label       = 'download log as json',
        file_name   = file_name + '_log.json',
        mime        = 'application/json',
        data        =  json_string
    )

    # DOWNLOAD AS CSV
    csv = log_tools.get_csv()

    st.download_button(
        label       = "download log as csv",
        file_name   = file_name + '_log.csv',
        mime        = 'text/csv',
        data        = csv
    )
