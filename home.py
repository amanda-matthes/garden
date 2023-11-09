import streamlit as st
from PIL import Image

timer_column, garden_column = st.columns(2, gap = 'large')

# SETTINGS

# TIMER
with timer_column:
    st.write('# timer')
    event_in_progress = False
    mode = st.selectbox('mode', ['countdown', 'stopwatch'], )

    if mode == 'countdown':
        st.write('countdown')
    else:
        st.write('stopwatch')

# GARDEN
with garden_column:
    st.write('# garden')
    if event_in_progress:
        st.write('focus on your work')
    else:
        st.image(Image.open('media/tree.png'))

st.write(f"streamlit version: {st.__version__}")