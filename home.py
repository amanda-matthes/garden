import streamlit as st
from PIL import Image

from datetime import datetime

import json
import session_tools
import tag_tools
import log_tools

from random import randrange

# SETTINGS
st.set_page_config(layout = 'wide')

timer_column, garden_column, log_column = st.columns([1, 1, 1], gap = 'large')

# TIMER
with timer_column:
    st.write('# timer')

    # PICK TAG
    tags            = tag_tools.get_all_tags()
    selected_tag    = st.selectbox('select tag', tags)

    # TIMER STATUS
    status = st.empty()

    current_start_time = session_tools.get_start_time_string()
    if current_start_time != '1900-01-01_00:00:00':
        status.text('timer started at ' + current_start_time)
    else:
        status.text('no timer running')

    # CONTROL BUTTONS
    start_button    = st.button('start')
    end_button      = st.button('end')
    if start_button:
        start_time = datetime.now()
        session_tools.update_start_time(datetime.strftime(start_time, '%Y-%m-%d_%H:%M:%S'))
        session_tools.update_end_time('1900-01-01_00:00:00')
        status.text('timer started at ' + datetime.strftime(start_time, '%Y-%m-%d_%H:%M:%S'))
    if end_button:
        if session_tools.get_start_time_string() != '1900-01-01_00:00:00':
            end_time = datetime.now()
            session_tools.update_end_time(datetime.strftime(end_time, '%Y-%m-%d_%H:%M:%S'))


    # RESULT
    elapsed_seconds = session_tools.get_elapsed_seconds()

    if elapsed_seconds is not None:

        hours, remainder = divmod(int(elapsed_seconds), 3600)
        minutes, seconds = divmod(remainder, 60)

        st.text('start          ' + session_tools.get_start_time_string())
        st.text('end            ' + session_tools.get_end_time_string())
        st.text('total          {:02}:{:02}:{:02}'.format(hours, minutes, seconds))


        # SAVE TO LOG
        current_time = datetime.now()

        save = st.button('save')
        if save:
            log_tools.add_event(
                timestamp   = current_time,
                duration    = elapsed_seconds,
                tag         = selected_tag
            )
            st.write('saved')
            session_tools.clear()
    else:
        messages = [
            'get some work done',
            'aim for the door, not for the stars',
            'it does not have to be good - it just has to be done',
            'you can do this',
            'you are doing so well',
            'be nice to yourself',
            'trust the process',
            'you are making progress',
            'go and get it',
            'you are doing all the right things',
            'it is not too late',
        ]
        if selected_tag == 'break':
            st.write('make a tea')
        else:
            message = messages[randrange(len(messages))]
            st.write(message)


# GARDEN
with garden_column:
    st.write('# garden')
    st.image(Image.open('media/tree.png'))


# LOG
with log_column:
    st.write('# log')

    ## UPLOAD
    uploaded_log = st.file_uploader(
        label       = 'upload log',
        type        = 'json'
    )

    if uploaded_log is not None:
        new_log = json.load(uploaded_log)
        log_tools.overwrite_log(new_log)


    # VIEW
    log_tools.display()


    # DOWNLOAD AS JSON
    file_name = datetime.today().strftime('%Y-%m-%d_%H-%M')
    json_string = log_tools.get_json_string()

    st.download_button(
        label       = 'download log as json',
        file_name   = file_name + '_log.json',
        mime        = 'application/json',
        data        =  json_string
    )


st.sidebar.write(f"streamlit version: {st.__version__}")