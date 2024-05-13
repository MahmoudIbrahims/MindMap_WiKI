import streamlit as st
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_google_genai import ChatGoogleGenerativeAI
from IPython.display import Markdown
import textwrap

google_api_key = "AIzaSyDXeu-2fZXcfPcBETItnBKi86zyAwQzslI"

def to_markdown(text):
    text = text.replace('•','*')
    return Markdown(textwrap.indent(text, '>', predicate=lambda _: True))

# Streamlit App Title
st.title("MindMap Wiki")

st.markdown('<style>h1 {color:purple;}</style>', unsafe_allow_html=True)
# Center align the page
st.markdown('<style>body {text-align: center;}</style>', unsafe_allow_html=True)
# Search Input Box
search_query = st.text_input("Enter your search query:")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)

# The tools we'll give the Agent access to.
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# Initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Search Button
if st.button("Search"):
    # Wrap the search_query in a list as agent.run() expects a list of strings.
    results = agent.run([search_query])
    if results:
        # Display the result directly
        st.markdown((textwrap.indent(results, '>', predicate=lambda _: True)))
    else:
        st.error("Page not found. Please try another search query.")
