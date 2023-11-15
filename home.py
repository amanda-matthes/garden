import streamlit as st
from PIL import Image

import time
from datetime import datetime

import session_tools
import tag_tools
import log_tools

# SETTINGS
st.set_page_config(layout = 'wide')

timer_column, data_column, garden_column = st.columns([1, 1, 1], gap = 'large')


# TIMER
with timer_column:
    st.write('# timer')

    # SELECT MODE
    mode = st.selectbox('mode', ['stopwatch', 'countdown'], )
    if mode == 'countdown':
        st.write('countdown')

        st.write('todo')
    else:
        st.write('stopwatch')

        # CONTROL BUTTONS
        start_button = st.button('start')
        end_button  = st.button('end')
        if start_button:
            start_time = datetime.now()
            session_tools.update_start_time(datetime.strftime(start_time, '%Y-%m-%d_%H:%M:%S'))
            session_tools.update_end_time('1900-01-01_00:00:00')

        if end_button:
            end_time = datetime.now()
            session_tools.update_end_time(datetime.strftime(end_time, '%Y-%m-%d_%H:%M:%S'))

        # TIMER
        if start_button:
            with st.empty():
                done = False
                while not done:
                    current_time = datetime.now()
                    elapsed_time = (current_time - start_time).total_seconds()
                    hours, remainder = divmod(int(elapsed_time), 3600)
                    minutes, seconds = divmod(remainder, 60)

                    st.write('# {:02}:{:02}:{:02}'.format(hours, minutes, seconds))

                    if end_button:
                        done == True

                    time.sleep(1)


# DATA
with data_column:
    st.write('# data')

    elapsed_seconds = session_tools.get_elapsed_seconds()

    if elapsed_seconds is not None:
        session_tools.display()

        hours, remainder = divmod(int(elapsed_seconds), 3600)
        minutes, seconds = divmod(remainder, 60)

        st.write('total time was {:02}:{:02}:{:02}'.format(hours, minutes, seconds))

        # PICK TAG
        tags            = tag_tools.get_all_tags()
        selected_tag    = st.selectbox('select tag', tags)

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
        st.write('get some work done')


# GARDEN
with garden_column:
    st.write('# garden')
    st.image(Image.open('media/tree.png'))
    log_tools.display()


st.sidebar.write(f"streamlit version: {st.__version__}")