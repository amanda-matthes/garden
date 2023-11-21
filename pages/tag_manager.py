import streamlit as st
import tag_tools

edit_column, add_column, view_column = st.columns([1, 1, 1], gap = 'large')

tags = tag_tools.get_all_tags()

with edit_column:
    st.write('# remove tags')

    tag = st.selectbox('select tag', tags)

    # REMOVE
    remove = st.button('remove ' + tag)
    if remove:
        tag_tools.remove_tag(tag)

    # # RENAME
    # new_name = st.text_input('new name')
    # rename = st.button('rename ' + tag + ' to ' + new_name)
    # if rename:
    #     tag_tools.rename_tag(tag, new_name)


with add_column:
    st.write('# add tags')
    new_tag = st.text_input('new tag')

    if len(new_tag) > 0:
        if new_tag in tags:
            st.write('this tag already exists')
        else:
            tag_tools.add_tag(new_tag)
            st.write('added tag for {}'.format(new_tag))

with view_column:
    st.write('# view tags')
    tags = tag_tools.get_all_tags()
    st.write(tags)