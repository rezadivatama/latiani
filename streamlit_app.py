import streamlit as st

st.title("selamat datang di negeri wakanda")
st.write(
    "jalan jalan di Negeri Wakanda" 
) 
st.image("download.jpeg", width=200)
        


st.title("hala madrid")
st.header("madrid 15 ucl")
angka = st.number_input("15:",value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
    st.write (f"{angka} adalah bilangan ganjil")
    

