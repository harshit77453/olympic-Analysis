import streamlit as st
import pandas as pd
import preprocessor, helper
bf = pd.read_csv('athlete_events.csv')
cf = pd.read_csv('noc_regions.csv')
bf = preprocessor.preprocess(bf,cf)



st.sidebar.title('Olympic Analysis')
st.sidebar.image("https://e1.365dm.com/23/02/1600x900/skysports-paris-olympics-rings_6052203.jpg",width = 300)
user_menu = st.sidebar.radio('Select an Option',('Medal Tally','Overall Analysis','Country-wise Analysis','Athelete-wise Analysis'))


if user_menu == 'Medal Tally':
    st.sidebar.title("Medal Tally")
    year,country = helper.country_year_list(bf)
    selected_year = st.sidebar.selectbox("Select Year",year)
    selected_country = st.sidebar.selectbox("Select Country",country)
    st.dataframe(bf)
    st.image("https://w7.pngwing.com/pngs/580/315/png-transparent-olympic-logo-olympic-olympics-olympic-game-olympic-rings-olympic-sign-3d-icon.png")

if user_menu == 'Country-wise Analysis':
    c_w_a = helper.medal_tally1(bf)
    st.dataframe(c_w_a)


if user_menu == 'Overall Analysis':
    st.dataframe(bf)
    c_w_a = helper.medal_tally1(bf)
    st.dataframe(c_w_a)