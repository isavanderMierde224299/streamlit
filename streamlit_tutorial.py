import streamlit as st
import time
import numpy as np
import pandas as pd
import altair as alt

st.write("Hello, let's learn how to build a Streamlit app together")
st.title("This is the app title")
st.header("This is the markdown")
st.markdown("This is the header")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.checkbox('Yes')
st.button('Click')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)
st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')
st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):
    time.sleep(10)
st.success("You did it!")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))
st.sidebar.title("This is a sidebar")
st.sidebar.button("Click here")
st.sidebar.radio("Pick your gender", ['Male', 'Female'])

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)

df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
c = alt.Chart(df).mark_circle().encode(
    x='x',
    y='y',
    size='z',
    color='z',
    tooltip=['x', 'y', 'z']
)
st.altair_chart(c, use_container_width=True)

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)

if __name__ == '__main__':
    st.run()


