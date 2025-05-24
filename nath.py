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
h1, h2, h3, h4, h5, h6, p {
text-align: center;
color: white;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# 💖 Título
st.title("💖 Para o Amor da Minha Vida 💖")

# 🎶 Música com autoplay
st.markdown("""
<div style="text-align: center;">
<iframe width="100%" height="166" scrolling="no" frameborder="no" 
allow="autoplay" 
src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/cozyatn/chezile-beanie-slowed-and-reverb&auto_play=true">
</iframe>
</div>
""", unsafe_allow_html=True)

# 🗓️ Contagem de dias juntos
data_inicio = date(2021, 5, 19)  # DATA ATUALIZADA
hoje = date.today()
dias = (hoje - data_inicio).days

st.markdown("---")
st.subheader("🌟 Quanto tempo já vivemos essa linda história? 🌟")

# 🎯 Contagem animada
contador = st.empty()
for i in range(0, dias + 1, max(1, dias // 100)):
    contador.subheader(f"💖 Estamos juntos há {i} dias! 💖")
    time.sleep(0.02)
contador.subheader(f"💖 Estamos juntos há {dias} dias! 💖")

st.markdown("---")

# 📜 Mensagem de amor
st.header("💌 Uma mensagem para você:")
st.markdown("""
<p style='font-size: 20px;'>
Amor da minha vida,<br><br>

Quero que saiba que cada momento ao seu lado é um presente que enche meu coração de alegria. <br>
Você transforma meus dias em felicidade, risos e amor. <br>
Que nossa história continue sendo escrita com carinho, cumplicidade e muito amor.<br><br>

<b>Te amo infinitamente! ❤️</b>
</p>
""", unsafe_allow_html=True)

# 🎁 Botão surpresa com corações animados
if st.button("Clique aqui para uma surpresa! 🎁"):
    st.success("Você é a pessoa mais incrível do mundo! 😍")
    
    for _ in range(20):
        hearts = "".join(["❤️" for _ in range(random.randint(5, 15))])
        st.markdown(f"<h3>{hearts}</h3>", unsafe_allow_html=True)
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

# 🎇 Botão final com mensagem de encerramento
st.markdown("---")
st.subheader("✨ Um último recado...")

if st.button("Clique aqui para o GRANDE FINAL! 🎇"):
    st.success("Prepare-se para sorrir... 😍")
    st.markdown("""
    <h2>💖✨</h2>
    <h3>Quero que você nunca se esqueça:</h3>
    <p style='font-size: 22px;'>
    Você é o amor da minha vida, minha melhor companhia, minha inspiração diária. <br><br>
    Que possamos continuar construindo memórias lindas, vivendo cada dia com amor, carinho e cumplicidade. <br><br>
    Você é a pessoa mais especial que Deus colocou na minha vida. <br><br>
    <b>TE AMO INFINITAMENTE! ❤️🥰</b>
    </p>
    """, unsafe_allow_html=True)
    st.balloons()
