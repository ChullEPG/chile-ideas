import streamlit as st
import random

# st.set_page_config(page_title="Chile Ideas", page_icon=":chile:", layout="wide")

# ideas = []

# def add_idea(idea):
#     ideas.append(idea)
#     st.write("Idea added: ", idea)


# def generate_idea():
#     if ideas:
#         st.write("Random idea: ", random.choice(ideas))
#     else:
#         st.write("No ideas to generate. Add some ideas first.")

# new_idea = st.text_input("Enter new idea")

# if st.button("Add Idea"):
#     add_idea(new_idea)

# if st.button("Generate Idea"):
#     generate_idea()

# st.write("List of ideas: ", ideas)


st.set_page_config(page_title="Chile Ideas", page_icon=":chile:", layout="wide")

@st.cache
def get_ideas():
    return []

ideas = get_ideas()

def add_idea(idea):
    ideas.append(idea)
    st.write(idea)

def generate_idea():
    if ideas:
        st.write(random.choice(ideas))
    else:
        st.write("No ideas to generate. Add some ideas first.")

new_idea = st.text_input("Enter new idea")

if st.button("Add Idea"):
    add_idea(new_idea)

if st.button("Generate Idea"):
    generate_idea()

st.write("List of ideas: ", ideas)
