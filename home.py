import streamlit as st
from PIL import Image

import time
from datetime import datetime

import session_tools
import tag_tools
import log_tools

# SETTINGS
st.set_page_config(layout = 'wide')

timer_column, data_column, garden_column = st.columns([1, 2, 1], gap = 'large')


# TIMER
with timer_column:
    st.write('# timer')
    mode = st.selectbox('mode', ['stopwatch', 'countdown'], )

    if mode == 'countdown':
        st.write('countdown')

        st.write('todo')
    else:
        st.write('stopwatch')

        start_button = st.button('start')
        if start_button:
            # start_time = time.time()
            start_time = datetime.strftime(datetime.now(), '%Y-%m-%d_%H:%M:%S')
            session_tools.update_start_time(start_time)
            session_tools.update_end_time('1900-01-01_00:00:00')

        end_button  = st.button('end')
        if end_button:
            # end_time = time.time()
            end_time = datetime.strftime(datetime.now(), '%Y-%m-%d_%H:%M:%S')
            session_tools.update_end_time(end_time)


            # st.write('elapsed time: {}'.format(end_time - start_time))

            # st.sidebar.write('starting timer')

            # with st.empty():
            #     done = False
            #     while not done:
            #         current_time = time.time()
            #         elapsed_time = current_time - start_time
            #         hours, remainder = divmod(int(elapsed_time), 3600)
            #         minutes, seconds = divmod(remainder, 60)

            #         st.write('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))

            #         if end_button:
            #             st.sidebar.write('stopping timer')
            #             st.write('whooo')
            #             # st.session_state['timing'] = False
            #             time.sleep(5)
            #             done == True

            #         time.sleep(1)
            #     st.write('blob')

            # st.write(start_time)
            # st.write('DONE')
            # st.button('something')


# DATA
with data_column:
    st.write('# data')

    # CURRENT SESSION
    refresh = st.button('refresh')
    if refresh:
        session_tools.display()
    else:
        session_tools.display()

    clear = st.button('clear')
    if clear:
        session_tools.clear()

    elapsed_seconds = session_tools.get_elapsed_seconds()

    if elapsed_seconds is not None:
        hours, remainder = divmod(int(elapsed_seconds), 3600)
        minutes, seconds = divmod(remainder, 60)

        st.write('# {:02}:{:02}:{:02}'.format(hours, minutes, seconds))

    # PICK TAG
    tags            = tag_tools.get_all_tags()
    selected_tag    = st.selectbox('select tag', tags)


    # SAVE TO LOG
    current_time = datetime.now()

    st.write(current_time)

    save = st.button('save')
    if save:
        log_tools.add_event(
            timestamp   = current_time,
            duration    = elapsed_seconds,
            tag         = selected_tag
        )
        st.write('saved')




# GARDEN
with garden_column:
    st.write('# garden')
    st.image(Image.open('media/tree.png'))
    log_tools.display()


st.sidebar.write(f"streamlit version: {st.__version__}")