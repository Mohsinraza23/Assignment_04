import streamlit as st
import string
import random
from graph import Graph, Vertex

# Apply custom CSS styling
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background: linear-gradient(to bottom right, #ffffff, #dfe9f3);
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        font-size: 16px;
        border-radius: 8px;
        margin-top: 10px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #555;
        padding-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>Markov Chain Text Generator 🧠🔀</h1>", unsafe_allow_html=True)

# Function to extract words from text
def extract_word(text):
    try:
        text = text.decode('utf-8')
    except UnicodeDecodeError:
        st.error("Unable to decode the text. Please ensure the file is in UTF-8 format. 📄🚫")
        return []
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words if words else []

# Function to build a graph
def build_graph(words):
    if not words:
        st.error("No words found in the text. 😔")
        return None

    graph = Graph()
    prev_vertex = None

    for word in words:
        word_vertex = graph.get_vertex(word)
        if prev_vertex:
            graph.add_edge(prev_vertex, word_vertex)
        prev_vertex = word_vertex

    graph.generate_probability_mapping()
    return graph

# Function to generate formatted text from the graph
def generate_text(graph, words):
    if not words or not graph:
        st.error("No words or graph available for text generation. 🛑")
        return ""

    formatted_text = "\n".join(words)
    return formatted_text

# Upload Section
uploaded_files = st.file_uploader("📂 Upload text file(s)", type=["txt"], accept_multiple_files=True)

all_words = []

for file in uploaded_files or []:
    all_words.extend(extract_word(file.read()))

if all_words:
    st.success(f"✅ Processed {len(uploaded_files)} file(s) successfully!")
    graph = build_graph(all_words)

    if st.button("✨ Generate Text"):
        st.subheader("✍️ Generated Text")
        st.markdown(generate_text(graph, all_words))
else:
    st.info("📥 Please upload at least one text file to proceed.")

# Stylish Footer
st.markdown("<hr class='footer'/>", unsafe_allow_html=True)
st.markdown("<div class='footer'>🔧 Built with 💖 by <strong>Mohsin Raza</strong></div>", unsafe_allow_html=True)
