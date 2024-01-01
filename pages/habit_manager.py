import streamlit as st
import habit_tools

st.write('# ! in progress')
edit_column, add_column, view_column = st.columns([1, 1, 1], gap = 'large')


habits = habit_tools.get_all_habits()

with edit_column:
    st.write('# remove habits')

    habit = st.selectbox('select habit', habits)

    remove = st.button('remove "' + habit + '"')
    if remove:
        habit_tools.remove_habit(habit)


with add_column:
    st.write('# add habit')
    new_habit   = st.text_input('new habit')
    type        = st.selectbox('type', ['checkbox', 'counter'])

    if len(new_habit) > 0:
        if new_habit in habits:
            st.write('this habit already exists')
        else:
            habit_tools.add_habit(new_habit)
            st.write('added {}'.format(new_habit))

with view_column:
    st.write('# view habits')
    st.write(habits)