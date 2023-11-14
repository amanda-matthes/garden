import streamlit as st
import pandas as pd

## this should be a json

current_session_file_name = 'data/session.csv'

def display():
    current_session = pd.read_csv(current_session_file_name)
    st.write(current_session)

def clear():
    current_session                 = pd.DataFrame()

    current_session['start_time']   = [0]
    current_session['end_time']     = [0]

    current_session.to_csv(current_session_file_name, index = False)

def _update(name, value):
    current_session             = pd.read_csv(current_session_file_name)
    current_session[name]       = [value]
    current_session.to_csv(current_session_file_name, index = False)

def _get(name):
    current_session             = pd.read_csv(current_session_file_name)
    return(current_session[name][0])

def update_start_time(start_time):
    _update('start_time', start_time)

def update_end_time(end_time):
    _update('end_time', end_time)

def get_start_time():
    return _get('start_time')

def get_end_time():
    return _get('end_time')

def get_elapsed_seconds():
    start_time = get_start_time()
    end_time   = get_end_time()
    if start_time < end_time:
        return((end_time - start_time))
    else:
        return None