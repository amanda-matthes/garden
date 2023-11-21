import streamlit as st
import log_tools
import json
from datetime import datetime


st.write('# log')

## VIEW
log_container = st.empty()

with log_container.container():
    log_tools.display()

clear = st.button('clear')
if clear:
    log_tools.clear()
    with log_container.container():
        log_tools.display()

## UPLOAD
uploaded_log = st.file_uploader(
    label       = 'upload log',
    type        = 'json'
)

if uploaded_log is not None:
    new_log = json.load(uploaded_log)
    log_tools.overwrite_log(new_log)

    with log_container.container():
        log_tools.display()


# DOWNLOAD OPTIONS
file_name = datetime.today().strftime('%Y-%m-%d_%H-%M')

# DOWNLOAD AS JSON
json_string = log_tools.get_json_string()

st.download_button(
    label       = 'download log as json',
    file_name   = file_name + '_log.json',
    mime        = 'application/json',
    data        =  json_string
)

# download = st.button('download csv')
# if download: # prevents generating the csv all the time

#     # DOWNLOAD AS CSV
#     # csv = log_tools.get_csv()

#     # st.download_button(
#     #     label       = "download log as csv",
#     #     file_name   = file_name + '_log.csv',
#     #     mime        = 'text/csv',
#     #     data        = csv
#     # )
