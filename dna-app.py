import altair as alt
from PIL import Image
import pandas as pd
import streamlit as st
#from sympy import sequence

image = Image.open('dna-logo.jpeg')
st.image(image, use_column_width=True)

st.write('''
# DNA nucleotide Count Web App

This app counts the nucleotide composition of query DNA

''')

st.header('Enter DNA sequence')
sequence_input=">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area('Sequence input',sequence_input, height=250)
sequence=sequence.splitlines()   # divide line to list elements 
sequence=sequence[1:]   # skip first elemnt '>DNA Query 2'
sequence=''.join(sequence)    # Concatinates lists to string

st.write('''
***
''')
st.header('Input (DNA Query) ')

st.header('Output (DNA Nucleotide Count)')

st.subheader('1. Print dictionary')

def DNA_nucleotide_count(seq):
    d=dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())
st.subheader('2. Print text')
st.write('There are '+str(X['A'])+' adenine (A)')
st.write('There are '+str(X['T'])+' thymine (T)')
st.write('There are '+str(X['G'])+'  guanine (guanine)')
st.write('There are '+str(X['C'])+' cytosine (cytosine)')



st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df=df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns = {'index':'nucleotide'})
st.write(df)
#-------------------------
st.subheader('4. Display bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y= 'count'

)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)

