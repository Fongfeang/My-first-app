import streamlit as st

st.title("คำนวณค่า BMI")
st.write("โปรแกรมคำนวณดัชนีมวลกาย")

weight = st.number_input(
    "น้ำหนัก (กิโลกรัม)",
    min_value=1.0,
    max_value=300.0,
    value=60.0
)

height = st.number_input(
    "ส่วนสูง (เซนติเมตร)",
    min_value=50.0,
    max_value=250.0,
    value=170.0
)

if st.button("คำนวณ BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.success(f"ค่า BMI ของคุณคือ {bmi:.2f}")

    if bmi < 18.5:
        st.info("คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
    elif bmi < 23:
        st.success("คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
    elif bmi < 25:
        st.warning("คุณมีน้ำหนักเกินเกณฑ์ (ท้วม)")
    elif bmi < 30:
        st.warning("คุณอยู่ในเกรณฑ์อ้วนระดับ 1 ควระวังเรื่องสุขภาพและออกกำลังกาย")
    else:
        st.error("คุณอยู่ในเกรณฑ์อ้วนระดับ 2 ควระวังเรื่องสุขภาพและออกกำลังกายมากๆ")

st.divider()
st.write("น.ส.กัญญาภัค บรรเรียนกิจ ม.4/9 เลขที่ 2")
