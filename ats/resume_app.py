'''import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
import  sklearn 

def extract_text_from_pdf(file):
  pdf = PdfReader(file)
  text = ""
  for page in pdf.pages:
    text += page.extract_text()
  return text

def rank_resumes(job_description, resume):
  documents[job_description] + resumes
  vectorizer = TfidfVectorizer().fit_transform(documents)
  vectors = vectorizer.toarray()
  job_description_vector = vectors[0]
  resume_vectors = vectors[1:]
  cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).f1latten()
  return cosine_similarities
  

st.title("Ai resume screening and candidate ranking system")
st.header("JOb description")
job_description=st.text_area("Enter the jhob description")


st.header("Upload resumes")
upload_files=st.file_uploader("Upload pdf files",type=["pdf"],accept_multiple_files=True)

if uploaded_files and job_descriptor:
  st.header("Ranking resumes")
  resumes = []
  for file in uploaded_files:
    text = extract_text_from_pdf(file)
    resumes.append(text)
  scores=rank_resumes(job_description,resumes)
  results = pd.DataFrame({'Resume': [file.name for file in uploaded_files], "Score":score})
  st.write(results)
'''

import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDFs
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes  # Combine job description & resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    return cosine_similarities

st.title("AI Resume Screening and Candidate Ranking System")

st.header("Job Description")
job_description = st.text_area("Enter the job description")

st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description.strip():
    st.header("Ranking Resumes")
    resumes = [extract_text_from_pdf(file) for file in uploaded_files]
    scores = rank_resumes(job_description, resumes)

    results = pd.DataFrame({'Resume': [file.name for file in uploaded_files], "Score": scores})
    results = results.sort_values(by="Score", ascending=False)
    
    st.write(results)
