import streamlit as st
import string
from graph import Graph, Vertex

# Page config
st.set_page_config(page_title="Markov Chain Generator", page_icon="🧠", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        color: #3b3b98;
        text-align: center;
        margin-top: 30px;
    }
    .footer {
        text-align: center;
        font-size: 16px;
        color: #777;
        margin-top: 50px;
    }
    .stButton>button {
        background-color: #3b3b98;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to extract words
def extract_word(text):
    try:
        text = text.decode('utf-8')
    except UnicodeDecodeError:
        st.error("❌ Unable to decode text. Ensure file is UTF-8.")
        return []
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words if words else []

# Function to build a graph
def build_graph(words):
    if not words:
        st.error("😔 No words found in uploaded text.")
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

# Function to generate text
def generate_text(graph, words, length=100):
    if not words or not graph:
        st.error("🛑 Graph or words not available.")
        return ""
    current_word = words[0]
    result = [current_word]
    for _ in range(length - 1):
        current_vertex = graph.get_vertex(current_word)
        next_word = current_vertex.next_word() if current_vertex else None
        if not next_word:
            break
        result.append(next_word)
        current_word = next_word
    return " ".join(result)

# Main UI
st.markdown("<h1 class='title'>🧠 Markov Chain Text Generator</h1>", unsafe_allow_html=True)
uploaded_files = st.file_uploader("📂 Upload .txt file(s)", type=["txt"], accept_multiple_files=True)

all_words = []

for file in uploaded_files or []:
    all_words.extend(extract_word(file.read()))

if all_words:
    st.success(f"✅ Processed {len(uploaded_files)} file(s) successfully!")
    graph = build_graph(all_words)

    if st.button("✨ Generate Text"):
        st.subheader("📜 Generated Text")
        st.write(generate_text(graph, all_words, length=150))
else:
    st.info("📥 Please upload a `.txt` file to begin.")

# Footer
st.markdown("<div class='footer'>🔧 Built with ❤️ by <strong>Mohsin Raza</strong></div>", unsafe_allow_html=True)
