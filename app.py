import streamlit as st
import json

# Cargar la base de datos
with open("bal.json", "r", encoding="utf-8") as f:
    data = json.load(f)

st.set_page_config(page_title="Manual de BAL", page_icon="🦠", layout="centered")

st.title("📖 Manual de Bacterias Ácido Lácticas (BAL)")
st.write("Busca información de bacterias ácido lácticas de importancia industrial y alimentaria.")

# Caja de búsqueda
query = st.text_input("🔍 Escribe el nombre de la bacteria:")

if query:
    encontrado = next((b for b in data if query.lower() in b["nombre"].lower()), None)
    if encontrado:
        st.subheader(encontrado["nombre"])
        st.markdown(f"**Morfología:** {encontrado['morfologia']}")
        st.markdown(f"**Metabolismo:** {encontrado['metabolismo']}")
        st.markdown(f"**Hábitat:** {encontrado['habitat']}")
        st.markdown(f"**Importancia:** {encontrado['importancia']}")
        st.image(encontrado["imagen"], width=250, caption=f"Micrografía de {encontrado['nombre']}")
    else:
        st.warning("⚠️ No se encontró la bacteria.")
