import streamlit as st
import json
import pandas as pd

from datetime import datetime

log_file_name = 'data/log.json'

def _display_json():
    with open(log_file_name, 'r') as log_file:
        log = json.load(log_file)['events']
    st.write(log)

def _generate_data_frame():
    with open(log_file_name, 'r') as log_file:
        events = json.load(log_file)['events']

    times       = []
    durations   = []
    tags        = []

    for event in events:
        times.append(event['time'])
        durations.append(event['duration'])
        tags.append(event['tag'])

    data_frame = pd.DataFrame()
    data_frame['time']      = times
    data_frame['duration']  = durations
    data_frame['tag']       = tags

    return data_frame

def display():
    data_frame = _generate_data_frame()
    st.write(data_frame)

def clear():
    empty = {
        'events': []
    }
    with open(log_file_name, 'w') as log_file:
        json.dump(empty, log_file)

def add_event(timestamp, duration, tag):
    event = {
        'time'      : timestamp.strftime("%m/%d/%Y, %H:%M:%S"),
        'duration'  : duration,
        'tag'       : tag
    }
    with open(log_file_name) as log_file:
        input_data      = json.load(log_file)
        events          = input_data['events']

        if events is None:
            events = []

        events.append(event)
        output_data     = {
            'events': events
        }
        print(output_data)
    with open(log_file_name, 'w') as log_file:
        json.dump(output_data, log_file, indent = 4)