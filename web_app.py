import streamlit as st
import functions

todos = functions.get_act()

def add_act():
    todo = st.session_state['new_act'] + "\n"
    todos.append(todo)
    functions.write_act(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_act(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_act, key='new_act')