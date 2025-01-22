import pandas as pd 
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

sales_data  = pd.read_excel("sales_report.xlsx")

st.set_page_config(page_title='Restaurant Sales Report', layout='wide', initial_sidebar_state='expanded', page_icon='📑')

st.sidebar.header("Filter Options")

selected_categories = st.sidebar.multiselect(
    'Select Categories:',
    options=sales_data['CATEGORY'].unique(),
    default=sales_data['CATEGORY'].unique()
)

selected_rating = st.sidebar.slider('Select Average Rating:', min_value=1, max_value=10, value=(1, 10))

filtered_data = sales_data[
    (sales_data['CATEGORY'].isin(selected_categories)) &
    (sales_data['AVG RATING'] >= selected_rating[0]) &
    (sales_data['AVG RATING'] <= selected_rating[1])
]

if st.checkbox('Show Raw Data'):
    st.dataframe(filtered_data)

st.title("Restaurant Sales Report")

total_profit = (filtered_data['PROFIT'].sum())
avg_rating = round((filtered_data['AVG RATING'].mean()),2)

col1,col2 = st.columns(2)

with col1 :
    st.markdown('### Total Profit:')
    st.subheader(f'{total_profit} $') 
with col2 :
    st.markdown('### Average Rating:')
    st.subheader(f'{avg_rating}')

    
st.markdown('---')

st.markdown('### Summary:')
st.write(f'The total profit for the selected categories is **{total_profit} $**. The average rating is **{avg_rating}**.')
    

category_profit = (filtered_data.groupby('CATEGORY')['PROFIT'].sum().reset_index())   

chart_col1,chart_col2 = st.columns(2)

with chart_col1:
    profit_bar_chart = px.bar(category_profit,
                   x='CATEGORY',y='PROFIT',
                   title='Profit by Category',
                   text_auto=True,
                   color_discrete_sequence=['#2c3e50'],
                   height=600,width=800)
    profit_bar_chart.update_xaxes(title_text = 'Profit')
    profit_bar_chart.update_yaxes(title_text = 'Category')
    profit_bar_chart.update_traces(textposition='outside')
    profit_bar_chart.update_layout(font=dict(family="Arial, sans-serif", size=14, color='white'),title_font=dict(size=24, color='white'))
    
    st.plotly_chart(profit_bar_chart, use_container_width=True)

with chart_col2:
    profit_pi_chart = go.Figure(data=[go.Pie(
    labels=category_profit['CATEGORY'],
    values=category_profit['PROFIT'],
    hole=0.3,
    marker_colors=['#2c3e50', '#34495e', '#7f8c8d', '#95a5a6', '#bdc3c7'],
    textinfo='percent+label',   
    textfont=dict(size=18, color='black'),  
    name='Profit Share by Category'
)])
    profit_pi_chart.update_layout(
    title_text='Profit Share by Category',
    title_font=dict(size=24, color='white'),
    annotations=[dict(text='Profit Share', font_size=20, xanchor='center', showarrow=False, font_color='white')],
    height=600,
    width=800,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    legend=dict(font=dict(color='white'))
)
    
    st.plotly_chart(profit_pi_chart, use_container_width=True)


if st.button('Export Filtered Data to Excel'):
    filtered_data.to_excel('filtered_data.xlsx', index=False)
    st.success('Data exported successfully!')

hide = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide, unsafe_allow_html=True)