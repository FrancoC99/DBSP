import streamlit as st

# Título de la barra lateral y opciones de navegación
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home", "Total M/S", "Clusters", "Los mayores incrementos", "Gráficos"], index=0)

# Función para mostrar la sección seleccionada
def show_section(section):
    if section == "Home":
        st.markdown("<h1 style='text-align: center;'>Análisis de Cuota de Mercado (Nielsen)</h1>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style='text-align: center;'>
                <a href='https://mywebsite.com/' target='_blank'>
                    <img src='https://logos-world.net/wp-content/uploads/2020/04/Samsung-Logo.png' alt='My App' style='width:1500px;'>
                </a>
                <p style='text-align: center;'>A brief description of what my app does</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    elif section == "Total M/S":
        st.header("Total M/S Análisis")
        # Cambia 'df' y los nombres de columnas según tus datos
        state = st.selectbox('Select an option', df['column_name'].unique())
        category = st.selectbox('Select a category', df['category_name'].unique())
        option = st.radio('Choose an option', ['Option 1', 'Option 2', 'Option 3'], index=1)
        
        # Procesa la opción seleccionada
        if st.button('Go'):
            # Llama a la función de análisis con los datos seleccionados
            analyze_data(option, state, category)

    elif section == "Clusters":
        st.header("Clusters Análisis")
        selected_metric = st.selectbox('Select metric', ['Metric 1', 'Metric 2'])
        
        # Verifica columnas necesarias y valores no nulos
        if 'required_column' not in df.columns or df[['required_column']].isnull().any().any():
            st.error("Missing or null values in required columns.")
        else:
            # Realiza un análisis dependiendo de la métrica seleccionada
            if selected_metric == 'Metric 1':
                metric_column = 'metric_1_column'
                color_scale = 'Reds'
                color_label = 'Label for Metric 1'
            else:
                metric_column = 'metric_2_column'
                color_scale = 'Blues'
                color_label = 'Label for Metric 2'
            
            # Genera y muestra el gráfico
            fig = create_choropleth(df, metric_column, color_scale, color_label)
            st.plotly_chart(fig)

    elif section == "Section 3":
        st.header("Section 3 Analysis")
        selected_option1 = st.selectbox('Select an option', df['option_column'].unique())
        selected_option2 = st.selectbox('Select a second option', df['second_option_column'].unique())
        ranking_filter = st.radio('Select ranking filter', ['Best', 'Worst'])
        
        if st.button('Go'):
            # Filtra y muestra los datos según las opciones seleccionadas
            filtered_data = filter_data(df, selected_option1, selected_option2, ranking_filter)
            fig = create_scatter_plot(filtered_data)
            st.plotly_chart(fig)

            # Muestra tablas adicionales según el análisis
            top_items = get_top_items(filtered_data)
            st.subheader("Top Items")
            st.write(top_items)

    elif section == "Section 4":
        st.header("Section 4 Analysis")
        num_items = st.selectbox('Select number of items', [5, 10, 15, 20], index=1)
        selected_segment = st.selectbox('Select a segment', df['segment_column'].unique())
        
        if st.button('Analyze'):
            # Análisis para la sección 4
            top_items = df.sort_values(by='some_metric', ascending=False).head(num_items)
            fig1 = create_bar_chart(top_items, 'some_metric')
            st.plotly_chart(fig1)

            if selected_segment:
                filtered_data = df[df['segment_column'] == selected_segment]
                fig2 = create_bar_chart(filtered_data, 'another_metric')
                st.plotly_chart(fig2)

# Llama a la función para mostrar la sección seleccionada
show_section(section)
