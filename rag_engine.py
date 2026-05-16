from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter

with open("data/farmer.txt", "r", encoding="utf-8") as f:
    text = f.read()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
docs = splitter.split_text(text)

embeddings = HuggingFaceEmbeddings()
db = FAISS.from_texts(docs, embeddings)

def get_context(query):
    results = db.similarity_search(query, k=3)
    return " ".join([r.page_content for r in results])