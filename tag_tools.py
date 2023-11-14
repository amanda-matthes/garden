import streamlit as st
import json

tags_file_name = 'data/tags.json'

def get_all_tags():
    with open(tags_file_name, 'r') as tag_file:
        tags = json.load(tag_file)
    return tags


def add_tag(tag):
    tags = get_all_tags()
    tags.append(tag)
    with open(tags_file_name, 'w') as tag_file:
        json.dump(tags, tag_file)