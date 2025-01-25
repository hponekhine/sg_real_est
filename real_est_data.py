#importing necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px

#reading file
df = pd.read_csv('HDDclean.csv')

#setting page configure and sidebar
st.set_page_config(page_title = 'Hpontthet:SG_Real Estate Data' , page_icon = ':bar_chart:', layout = 'wide')
st.sidebar.header('Please Filter Here')

#putting default and selction on sidebar for Flattypes
flat_type_op = st.sidebar.multiselect(
    'Select Flat Type', 
    options = df['flat_type'].unique(),
    default = df['flat_type'].unique() [:5]
)

#putting default and selction on sidebar for towns
town_op = st.sidebar.multiselect(
    'Select Town', 
    options = df['town'].unique(),
    default = df['town'].unique() [:5]
)

#putting default and selction on sidebar for years
year_op = st.sidebar.multiselect(
    'Select Year', 
    options = df['year'].unique(),
    default = df['year'].unique() [:5]
)

#adding main title 
st.title(':bar_chart: SINGAPORE:Real Estate Data')
st.markdown('##')

#giving names for total amount and no. of flat types
Total = df['resale_price'].sum()
Flat_types = df['flat_type'].nunique()

#adding subcolumns 
left_col , right_col = st.columns(2)
with left_col:
    st.subheader ('Total Sales')
    st.subheader (f"US $ {Total}")
with right_col:
    st.subheader ('Flat Types')
    st.subheader (f"{Flat_types}")

#creating new dataset with query
df_select = df.query('flat_type==@flat_type_op and town==@town_op and year ==@year_op')

#creating necessary filters for data visualization
df_wood_15 = ((df['year'] == 2015) & (df['town'] == 'WOODLANDS'))
df_yi_15 = ((df['year'] == 2015) & (df['town'] == 'YISHUN'))
df_qu_15 = ((df['year'] == 2015) & (df['town'] == 'QUEENSTOWN'))

#creating three columns
a , b , c = st.columns(3)

#bar graph with flat types and resale price
aa = df_select.groupby('flat_type') ['resale_price'].sum().sort_values()
fig_sp = px.bar(
    aa,
    x = aa.values,
    y = aa.index,
    title = "Sales by Flat Type"
    )
a.plotly_chart(fig_sp, use_container_width = True)

#making pie graph
fig_town = px.pie(
    df_select,
    values = 'resale_price',
    names = 'town',
    title = "Sales by Town"
)
b.plotly_chart(fig_town, use_container_width = True)

#making bar grpah with year and resale price
bb = df_select.groupby('year') ['resale_price'].sum().sort_values()
fig_year = px.bar(
    bb,
    x = bb.index,
    y = bb.values,
    title = "Sales by Year"
    )
c.plotly_chart(fig_year, use_container_width = True)


#adding two columns
d , e = st.columns(2)

#making line graph
line_fig = px.line(
    bb,
    x = bb.values,
    y = bb.index,
    title = 'Sales by Year'
)

d.plotly_chart(line_fig, use_container_width = True)

#creating histogram with resale price
hist_fig = px.histogram(
    df_select,
    x = 'resale_price',
    title = 'Resale Price'
)
e.plotly_chart(hist_fig, use_container_width = True)


#making three columns
x,y,z = st.columns(3)

#below 3 figures are comparing sqm and resale price between woodlands,yishun and queenstown
wood_fig = px.scatter(
    df[df_wood_15],
    x = 'floor_area_sqm',
    y = 'resale_price',
    title = 'Woodlands:Sales by Floor Area(sqm) in 2015'
)
x.plotly_chart(wood_fig, use_container_width = True)

yi_scat = px.scatter(
    df[df_yi_15],
    x = 'floor_area_sqm',
    y = 'resale_price',
    title = 'Yishun:Sales by Floor Area(sqm) in 2015'
)
y.plotly_chart(yi_scat, use_container_width = True)

qu_scat = px.scatter(
    df[df_qu_15],
    x = 'floor_area_sqm',
    y = 'resale_price',
    title = 'Queenstown:Sales by Floor Area(sqm) in 2015'
)
z.plotly_chart(qu_scat, use_container_width = True)

















