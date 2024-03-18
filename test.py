import streamlit as st
from streamlit_chat import message

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right