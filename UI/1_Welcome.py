import streamlit as st

from scripts.output import Output
from scripts.message_generator import generate_messages


st.set_page_config(
    layout="wide",
    page_title="Error Recrator",
    page_icon="🥸",
)

st.write("Hello, world!")
status_container = st.status("Runnin...",
                             expanded=True)

Output().configure(lambda m: status_container.write(m))
generate_messages()
