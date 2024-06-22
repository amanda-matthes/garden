import streamlit as st
import json
import pandas as pd

log_file_name = 'data/log.json'

def _display_json():
    with open(log_file_name, 'r') as log_file:
        log = json.load(log_file)['events']
    st.write(log)

def get_json_string():
    with open(log_file_name, 'r') as log_file:
        log = json.load(log_file)
    return json.dumps(log, indent = 4)

def _generate_data_frame():
    with open(log_file_name, 'r') as log_file:
        events = json.load(log_file)['events']

    times       = []
    durations   = []
    tags        = []

    for event in reversed(events):
        times.append(event['time'])
        durations.append(event['duration'])
        tags.append(event['tag'])

    data_frame = pd.DataFrame()
    data_frame['time']      = times
    data_frame['duration']  = durations
    data_frame['tag']       = tags

    return data_frame

def get_csv():
    data_frame = _generate_data_frame()
    return data_frame.to_csv().encode('utf-8')

def display():
    data_frame = _generate_data_frame()
    data_frame['duration'] = data_frame['duration'].apply(lambda x: x//60)

    st.dataframe(
        data    = data_frame,
        width   = 500,
        column_config   = {
            'time'          : st.column_config.DatetimeColumn(
                format = 'DD MMM YYYY hh:mm a',
                width  = 150
            ),
            'duration'      : st.column_config.NumberColumn(
                format = '%i min',
                width = 70
            )
        }
    )

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
    with open(log_file_name, 'w') as log_file:
        json.dump(output_data, log_file, indent = 4)

def overwrite_log(new_log):
    with open(log_file_name, 'w') as log_file:
        json.dump(new_log, log_file, indent = 4)