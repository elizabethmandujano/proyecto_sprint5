import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('/Users/elizabethmandujano/Desktop/proyecto_sprint5/proyecto_sprint5/vehicles_us.csv')

#desarrollo del cuadro de mandos de la app web
st.header('CARS SALE')

#histograma con boton
st.subheader('Information about the cars')
hist_button = st.button('Show odometer histogram')

if hist_button:
    st.write('Creating an histogram about the odometer of the cars on sale')
    fig_hist = px.histogram(car_data,
                        x='odometer',
                        title= 'Distance traveled on cars',
                        )
    st.plotly_chart(fig_hist, use_container_width=True)

#grafico de dispersión 
disp_button= st.button('Show the prices')

if disp_button:
    st.write('Creating scatter plot about the relation between prices and odometer')
    fig_scatter = px.scatter(car_data,
                            x='odometer',
                            y='price',
                            title='Price on cars related to the odometer',
                            color='condition'
                            )
    st.plotly_chart(fig_scatter, use_container_width=True)

#grafico con checkbox
box_graph= st.checkbox('Show condition of the cars')

if box_graph:
    st.write('Creating a graphic for the condition of the cars')
    fig_graph = px.histogram(car_data,
                             x='model_year',
                             y= 'condition',
                             title='Condition of cars through the years')
    st.scatter_chart(fig_graph, color='#FF0000', use_container_width=True)

#slider de rango de precios
## se analizó previamente cual era el precio maximo 
select_price= st.slider('Price', 1, 375000, 100000)
filtered_data= car_data[car_data['price'] == select_price]

st.subheader(f'Cars available for {select_price} dollars')
st.write(filtered_data)

