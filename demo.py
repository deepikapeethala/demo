import streamlit as st
st.set_page_config(page_title = 'cats')
st.markdown("Types of Cats")

col1,col2=st.columns(2)
with col1:
  st.write("Persian Cat")
  st.subheader("/054d7111.jpg",caption="Persian Cat",width=300,use_column_width=True)
  st.write("Persian cat are cute")
with col2:
  st.write("white Cat")
  st.subheader("./1013332-white-cats-wallpaper-1920x1200-for-meizu.jpg",caption="White Cat",width=300,use_column_width=True)
  st.write("white cat are cute")




