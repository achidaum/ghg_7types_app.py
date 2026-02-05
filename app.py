import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="GHG คืออะไร? - 7 ก๊าซเรือนกระจก",
    page_icon="🌍",
    layout="wide"
)

# ปรับแต่ง CSS สำหรับ Header และ Card (ตรวจสอบจุดปิดเรียบร้อย)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Kanit', sans-serif;
    }
    .main-title {
        color: #1B5E20;
        text-align: center;
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #455A64;
        text-align: center;
        font-size: 24px;
        font-weight: 400;
        margin-top: -10px;
        margin-bottom: 30px;
    }
    .ghg-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #2E7D32;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        min-height: 180px;
    }
    .ghg-card h4 {
        color: #2E7D32;
        margin-bottom: 10px;
        font-weight: 600;
    }
    .ghg-card p {
        font-size: 15px;
        color: #546E7A;
        line-height: 1.5;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ส่วนหัวข้อ ---
st.markdown("<h1 class='main-title'>GHG คืออะไร?</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>เจาะลึก 7 ก๊าซเรือนกระจก ตัวการทำโลกเดือด</p>", unsafe_allow_html=True)

st.write("---")

# --- ส่วนคำอธิบาย ---
st.subheader("🔍 ก๊าซเรือนกระจกคืออะไร?")
st.write("""
ก๊าซเรือนกระจก (Greenhouse Gases: GHG) คือก๊าซที่อยู่ในชั้นบรรยากาศ ทั้งที่เกิดขึ้นเองตามธรรมชาติ และที่เกิดจากกิจกรรมของมนุษย์ 
มีคุณสมบัติพิเศษในการดูดซับคลื่นรังสีความร้อนได้ดี และแผ่รังสีความร้อนกลับลงมาสู่พื้นผิวโลก 
ซึ่งเปรียบเสมือนกระจกของเรือนเพาะปลูกที่กักเก็บความร้อนไว้ภายใน ทำให้เกิดปรากฏการณ์เรือนกระจก (Greenhouse Effect)
""")


st.info("📌 ข้อมูลอ้างอิงตามพิธีสารเกียวโต (Kyoto Protocol) และมาตรฐานที่ อบก. ให้การรับรอง")

# --- ส่วนชนิดก๊าซ 7 ชนิด (2 คอลัมน์) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='ghg-card'>
        <h4>1. คาร์บอนไดออกไซด์ (CO<sub>2</sub>)</h4>
        <p><b>แหล่งที่มา:</b> การเผาไหม้เชื้อเพลิงฟอสซิล (ถ่านหิน, น้ำมัน), การคมนาคม และการตัดไม้ทำลายป่า</p>
    </div>
    <div class='ghg-card'>
        <h4>2. มีเทน (CH<sub>4</sub>)</h4>
        <p><b>แหล่งที่มา:</b> การปศุสัตว์ (วัว), นาข้าว, การฝังกลบขยะ และการรั่วไหลจากแหล่งก๊าซ</p>
    </div>
    <div class='ghg-card'>
        <h4>3. ไนตรัสออกไซด์ (N<sub>2</sub>O)</h4>
        <p><b>แหล่งที่มา:</b> การใช้ปุ๋ยเคมีในเกษตรกรรม และกระบวนการทางอุตสาหกรรม</p>
    </div>
    <div class='ghg-card'>
        <h4>4. ไฮโดรฟลูออโรคาร์บอน (HFCs)</h4>
        <p><b>แหล่งที่มา:</b> สารทำความเย็นในแอร์และตู้เย็น, อุตสาหกรรมผลิตโฟม</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='ghg-card'>
        <h4>5. เปอร์ฟลูออโรคาร์บอน (PFCs)</h4>
        <p><b>แหล่งที่มา:</b> การผลิตอะลูมิเนียม และอุตสาหกรรมอิเล็กทรอนิกส์</p>
    </div>
    <div class='ghg-card'>
        <h4>6. ซัลเฟอร์เฮกซะฟลูออไรด์ (SF<sub>6</sub>)</h4>
        <p><b>แหล่งที่มา:</b> อุปกรณ์ไฟฟ้าแรงสูง (ฉนวนไฟฟ้าในระบบส่งจ่ายไฟ)</p>
    </div>
    <div class='ghg-card'>
        <h4>7. ไนโตรเจนไตรฟลูออไรด์ (NF<sub>3</sub>)</h4>
        <p><b>แหล่งที่มา:</b> การผลิตจอ LCD, แผงโซลาร์เซลล์ และไมโครชิป</p>
    </div>
    <div style='text-align: center; padding: 10px; color: #2E7D32; font-weight: bold;'>
        🌍 มาร่วมกันลดก๊าซเรือนกระจกเพื่อโลกกันครับ
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.caption("พัฒนาด้วย Streamlit | อ้างอิงข้อมูลจาก องค์การบริหารจัดการก๊าซเรือนกระจก (TGO)")
