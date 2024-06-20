import streamlit as st
import json
import pandas as pd

from datetime import datetime

import calplot
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

import os

plt.style.use('dark_background')
plt.rcParams['savefig.transparent'] = 'true'

habits_file_name        = 'data/habits.json'
habit_tracker_file_name = 'data/habit_tracker.csv'
habit_plot_directory    = 'data/habit_plots'

def _get_habits(type):
    with open(habits_file_name, 'r') as file:
        habits = json.load(file)['habits']
    selected_habits = []
    for habit in habits:
        if habit['type'] == type:
            selected_habits.append(habit['name'])
    return selected_habits

def get_checkbox_habits():
    return _get_habits('checkbox')

def get_counter_habits():
    return _get_habits('counter')

def get_all_habits():
    all_habits = []
    for habit in get_checkbox_habits():
        all_habits.append(habit)
    for habit in get_counter_habits():
        all_habits.append(habit)
    return all_habits

def get_colour(habit_name):
    with open(habits_file_name, 'r') as file:
        habits = json.load(file)['habits']
    for habit in habits:
        if habit['name'] == habit_name:
            return habit['colour']

def _get_first_day():
    habit_log = pd.read_csv(habit_tracker_file_name)
    start_day   = habit_log.head(1)['date'].to_numpy()[0]
    return start_day

def _get_last_day():
    habit_log = pd.read_csv(habit_tracker_file_name)
    end_day     = habit_log.tail(1)['date'].to_numpy()[0]
    return end_day

def _get_index(day):
    day       = datetime.strptime(day, '%Y-%m-%d')
    first_day = datetime.strptime(_get_first_day(), '%Y-%m-%d')
    day_delta = (day-first_day).days
    return day_delta

def get_days():
    start_day   = _get_first_day()
    end_day     = _get_last_day()

    return pd.date_range(
                start       = start_day,
                end         = end_day,
                freq        ='D'
                )

def get_events(habit):
    habit_log = pd.read_csv(habit_tracker_file_name)
    events = habit_log[habit].to_numpy()
    return events

def update_habit(day, habit, value):
    habit_log   = pd.read_csv(habit_tracker_file_name)
    index       = _get_index(day)
    try:
        habit_log.at[index, habit] = int(value)
    except:
        print('something went wrong')
    habit_log.to_csv(habit_tracker_file_name, index = False)

    update_plot(habit)

def get_value(day, habit):
    habit_log   = pd.read_csv(habit_tracker_file_name)
    index       = _get_index(day)
    value       = habit_log.at[index, habit]
    return value


def remove_habit():
    #TODO implement
    return

def add_habit(name, type):
    #TODO implement
    # add to habits.json

    # add to habit_tracker.csv

    return

def update_plot(habit):
    colour = get_colour(habit)

    days        = get_days()
    events      = pd.Series(
                    get_events(habit),
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

    file_path = os.path.join(habit_plot_directory, habit + '.png')
    plt.savefig(file_path, dpi = 500)

def display_plot(habit):
    file_path = os.path.join(habit_plot_directory, habit + '.png')
    st.image(file_path, use_column_width=True)
