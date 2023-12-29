import streamlit as st
st.set_page_config(page_title='cats')
st.markdown("## Types of Cats")
col1,col2=st.columns(2)
with col1:
  st.subheader("Persian cat")
  st.image("/054d7111.jpg",caption="Persian cat",width=300,use_column_width=True)
  st.write("Persian cats are cute")
with col2:
  st.subheader("White cat")
  st.image("./1013332-white-cats-wallpaper-1920x1200-for-meizu.jpg,caption="White cat",width=300,use_column_width=True)
  st.write("White cats are cute")




