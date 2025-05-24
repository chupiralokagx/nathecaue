import streamlit as st
from datetime import date

# 🔥 Fundo vermelho
page_bg_img = '''
<style>
body {
background-color: #FF0000;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# 💖 Título
st.title("💖 Para o Amor da Minha Vida 💖")

# 🎶 Música do SoundCloud
st.markdown("""
<iframe width="100%" height="166" scrolling="no" frameborder="no" 
allow="autoplay" 
src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/cozyatn/chezile-beanie-slowed-and-reverb&color=%23ff5500&inverse=false&auto_play=false&show_user=true">
</iframe>
""", unsafe_allow_html=True)

# 🗓️ Contagem de dias juntos
data_inicio = date(2022, 5, 24)  # Ajuste sua data
hoje = date.today()
dias = (hoje - data_inicio).days

st.subheader(f"Estamos juntos há 🌟 {dias} dias 🌟")
st.markdown("---")

# 📜 Mensagem de amor
st.header("Uma mensagem para você:")
st.write("""
Amor da minha vida,

Quero que saiba que cada momento ao seu lado é um presente que enche meu coração de alegria. 
Você transforma meus dias em felicidade, risos e amor. 
Que nossa história continue sendo escrita com carinho, cumplicidade e muito amor.

Te amo infinitamente! ❤️
""")

# 🎁 Surpresa
if st.button("Clique aqui para uma surpresa! 🎁"):
    st.balloons()
    st.success("Você é a pessoa mais incrível do mundo! 😍")

# 🖼️ Foto fixa no app
st.markdown("---")
st.subheader("📸 Uma lembrança especial:")

st.image("https://i.imgur.com/S8BRvay.jpg", 
         caption="Momentos que guardo no meu coração 💖", 
         use_column_width=True)