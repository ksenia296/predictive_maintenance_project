import streamlit as st
from analysis_and_model import analysis_and_model_page
from presentation import presentation_page

# Словарь страниц с соответствующими функциями
pages = {
    "Анализ и модель": analysis_and_model_page,
    "Презентация": presentation_page
}

# Боковая панель с навигацией
st.sidebar.title("Навигация")
selection = st.sidebar.radio("Выберите страницу", tuple(pages.keys()))

# Выполняем выбранную страницу
pages[selection]()  # Вызываем функцию, соответствующую выбранной странице