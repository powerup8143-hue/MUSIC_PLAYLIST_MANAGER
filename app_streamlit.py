# app_streamlit.py
import streamlit as st
import subprocess
import shlex

st.set_page_config(page_title="C Playlist (Streamlit)", layout="centered")

st.title("C Playlist — Streamlit UI")
st.write("This UI calls the compiled C program `./playlist`. Make sure you compiled it (run `./compile.sh`).")

cmd = st.radio("Command", ["list", "add", "remove"])

if cmd == "add":
    name = st.text_input("Song name")
    if st.button("Add"):
        # Use quotes to preserve spaces
        proc = subprocess.run(["./playlist", "add", name], capture_output=True, text=True)
        st.text(proc.stdout)
elif cmd == "remove":
    idx = st.number_input("Index to remove", min_value=1, step=1)
    if st.button("Remove"):
        proc = subprocess.run(["./playlist", "remove", str(int(idx))], capture_output=True, text=True)
        st.text(proc.stdout)
else:
    if st.button("Show playlist"):
        proc = subprocess.run(["./playlist", "list"], capture_output=True, text=True)
        st.text(proc.stdout)
