
import streamlit as st

st.set_page_config(
    page_title="AI Student Success Advisor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Student Success Advisor")
st.write("Welcome to your Personalized Learning Dashboard!")

st.info("Your AI project website is ready for the next step.")

name = st.text_input("Enter Student Name")
study_hours = st.number_input(
    "Daily Study Hours", min_value=0.0, max_value=24.0, value=2.0
)
attendance = st.slider("Attendance (%)", 0, 100, 75)
score = st.slider("Test Score (%)", 0, 100, 60)

if st.button("Generate Study Plan"):
    st.subheader("Personalized Study Plan")
    st.write("Student:", name if name else "Student")
    st.write("Study Hours:", study_hours)
    st.write("Attendance:", f"{attendance}%")
    st.write("Test Score:", f"{score}%")

    if score < 50:
        st.warning("Revise difficult topics and practise questions daily.")
    else:
        st.success("Continue regular revision and practise advanced questions.")

    if attendance < 75:
        st.write("Suggestion: Focus on attending classes consistently.")
      
