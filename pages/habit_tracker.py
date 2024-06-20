import streamlit as st
import habit_tools
from datetime import datetime


st.write('# daily tracker')

st.write(datetime.today().strftime('## %A %d %B %Y'))

left_column, right_column = st.columns([1, 2])


# UPDATE
with left_column:
    habits          = habit_tools.get_all_habits()
    checkbox_habits = habit_tools.get_checkbox_habits()

    new_values = [0 for i in habits]
    for i, habit in enumerate(checkbox_habits):
        new_values[i] = st.checkbox(
                            label = habit,
                            value = habit_tools.get_value(
                                        datetime.today().strftime('%Y-%m-%d'),
                                        habit
                                    )
                        )

    update = st.button('update day')

    if update:
        for i, habit in enumerate(checkbox_habits):
            habit_tools.update_habit(
                day = datetime.today().strftime('%Y-%m-%d'),
                habit = habit,
                value = new_values[i]
            )

# DISPLAY
with right_column:
    for habit in checkbox_habits:
        st.write(habit)
        habit_tools.display_plot(habit)
