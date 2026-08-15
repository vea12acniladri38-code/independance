import streamlit as st

st.set_page_config(
    page_title="Independence Day 🇮🇳",
    page_icon="🇮🇳"
)

# Title
st.title(" Happy Independence Day ")

st.subheader("15 August 2026")
st.subheader("80 Years of indepandence : ")

st.write("")

# Indian Flag
st.markdown("""
<div style="text-align:center; font-size:100px;">
🟧
<br>
⬜
<br>
🟩
</div>
""", unsafe_allow_html=True)

# Message
st.success("""
 Today we celebrate the freedom of our great nation.

Let us remember and respect all the freedom fighters
who sacrificed their lives for India's independence.

**Jai Hind! **
""")

# NameS
name = st.text_input("Enter your name")

if st.button("Celebrate 🎉"):

    if name:
        st.balloons()

        st.write(
            f" Happy Independence Day, **{name}**! "
        )

        st.write(
            "Proud to be an Indian! ❤️🤍💚"
        )

    else:
        st.warning("Please enter your name.")

# Quote
st.subheader("💬 Patriotic Quote")

st.info(
    "One individual may die for an idea, "
    "but that idea will live forever."
)