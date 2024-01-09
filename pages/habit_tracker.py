import streamlit as st
import habit_tools
from datetime import datetime

import calplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


st.write('# daily tracker')

# UPDATE
st.write(datetime.today().strftime('## %A %d %B %Y'))

habits          = habit_tools.get_all_habits()
checkbox_habits = habit_tools.get_checkbox_habits()

new_values = [0 for i in habits]
for i, habit in enumerate(checkbox_habits):
    new_values[i] = st.checkbox(habit)

update = st.button('update day')

if update:
    for i, habit in enumerate(checkbox_habits):
        habit_tools.update_habit(
            day = datetime.today().strftime('%Y-%m-%d'),
            habit = habit,
            value = new_values[i]
        )

# DISPLAY
st.write('# view')
plt.style.use('dark_background')
plt.rcParams['savefig.transparent'] = 'true'


view = st.button('view')
if view:
    for habit in checkbox_habits:
        st.write('### ' + habit)

        colour = habit_tools.get_colour(habit)

        days        = habit_tools.get_days()
        events      = pd.Series(
                        habit_tools.get_events(habit),
                        index = days
                    )

        fig, _ = calplot.calplot(
                    data        = events,
                    vmin        = 0,
                    vmax        = 1,
                    yearlabels  = True,
                    colorbar    = False,
                    cmap        = ListedColormap(["ivory", colour])
                )

        st.pyplot(fig)
