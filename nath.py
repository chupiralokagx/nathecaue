import streamlit as st
from datetime import date
import random
import time

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

# 🎶 Música do SoundCloud com autoplay
st.markdown("""
<iframe width="100%" height="166" scrolling="no" frameborder="no" 
allow="autoplay" 
src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/cozyatn/chezile-beanie-slowed-and-reverb&auto_play=true">
</iframe>
""", unsafe_allow_html=True)

# 🗓️ Contagem de dias juntos
data_inicio = date(2022, 5, 24)  # Ajuste sua data
hoje = date.today()
dias = (hoje - data_inicio).days

st.markdown("---")
st.subheader("🌟 Quanto tempo já vivemos essa linda história? 🌟")

# 🎯 Contagem animada
contador = st.empty()
for i in range(0, dias + 1, max(1, dias // 100)):  # Incremento proporcional
    contador.subheader(f"💖 Estamos juntos há {i} dias! 💖")
    time.sleep(0.02)
contador.subheader(f"💖 Estamos juntos há {dias} dias! 💖")  # Garantir valor final

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

# 🎁 Botão surpresa com corações animados
if st.button("Clique aqui para uma surpresa! 🎁"):
    st.success("Você é a pessoa mais incrível do mundo! 😍")
    
    # 💖 Corações animados
    for _ in range(20):
        hearts = "".join(["❤️" for _ in range(random.randint(5, 15))])
        st.markdown(f"<h3 style='text-align: center;'>{hearts}</h3>", unsafe_allow_html=True)
        time.sleep(0.1)

# 🖼️ Botão para revelar a foto
st.markdown("---")
st.subheader("📸 Quer ver uma lembrança especial?")

if st.button("Clique aqui para revelar nossa foto! 📸"):
    st.image(
        "https://i.imgur.com/S8BRvay.jpg", 
        caption="Momentos que guardo no meu coração 💖", 
        use_container_width=True
    )
