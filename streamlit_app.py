import streamlit as st
import datetime, random

st.title("Bitnova AI – Asistente de Ahorro en BTC")
today = datetime.datetime.now().strftime("%A, %d %B %Y")
btc_price = round(random.uniform(25000, 40000), 2)

st.write(f"**Hoy es:** {today}")
st.write(f"**Precio estimado de BTC:** ${btc_price}")

preferred_day = "Friday"
amount = 0.05

if today.split(",")[0] == preferred_day:
    st.info(f"💡 Hoy es tu día habitual de ahorro. Podrías ahorrar ${amount} en BTC.")
elif btc_price < 28000:
    st.warning(f"📉 BTC está bajo: ¡una buena oportunidad para ahorrar ${amount}!")
else:
    st.success("🙂 Hoy no hay recomendación fuerte. Mantente pendiente de otros días.")
