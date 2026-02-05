import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="7 ก๊าซเรือนกระจก ตัวการโลกร้อน",
    page_icon="🌍",
    layout="wide"
)

# ปรับแต่ง CSS ให้ฟอนต์อ่านง่ายขึ้น
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Kanit', sans-serif;
    }
    .main-title {
        color: #2E7D32;
        text-align: center;
        font-weight: 600;
    }
    .highlight-card {
        background-color: #f0f7f4;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #2E7D32;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ส่วนหัวข้อ ---
st.markdown("<h1 class='main-title'>🌍 7 ก๊าซเรือนกระจกที่โลกต้องจำ!</h1>", unsafe_allow_html=True)
st.write("---")

# --- อธิบายปรากฏการณ์ ---
st.markdown("""
### **ทำไมโลกถึงร้อน? 🌡️**
ก๊าซเรือนกระจก (**Greenhouse Gases: GHG**) มีทั้งที่เกิดขึ้นเองตามธรรมชาติและจากกิจกรรมของมนุษย์ 
มีคุณสมบัติพิเศษในการ **ดูดซับคลื่นรังสีความร้อน** และแผ่รังสีกลับลงมาสู่พื้นผิวโลก 
ซึ่งเปรียบเสมือนกระจกของเรือนเพาะปลูกที่กักเก็บความร้อนไว้ภายใน ทำให้เกิด **ปรากฏการณ์เรือนกระจก (Greenhouse Effect)** อันเป็นสาเหตุหลักของภาวะโลกร้อนในปัจจุบัน
""")



st.info("💡 ข้อมูลอ้างอิงตาม **พิธีสารเกียวโต (Kyoto Protocol)** และมาตรฐานที่ **อบก.** ให้การรับรอง")

# --- ส่วน Card 7 ชนิด (ใช้ Column เพื่อความสวยงาม) ---
st.subheader("📊 เจาะลึก 7 ก๊าซตัวการหลัก")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='highlight-card'>
        <h4>1. คาร์บอนไดออกไซด์ ($CO_2$)</h4>
        <p><b>ที่มา:</b> การเผาไหม้เชื้อเพลิงฟอสซิล (รถยนต์, โรงไฟฟ้า), การตัดไม้ทำลายป่า</p>
    </div>
    <div class='highlight-card'>
        <h4>2. มีเทน ($CH_4$)</h4>
        <p><b>ที่มา:</b> การปศุสัตว์ (การเคี้ยวเอื้องของสัตว์), นาข้าว, การฝังกลบขยะมูลฝอย</p>
    </div>
    <div class='highlight-card'>
        <h4>3. ไนตรัสออกไซด์ ($N_2O$)</h4>
        <p><b>ที่มา:</b> การใช้ปุ๋ยเคมีในเกษตรกรรม, กระบวนการทางอุตสาหกรรม</p>
    </div>
    <div class='highlight-card'>
        <h4>4. ไฮโดรฟลูออโรคาร์บอน (HFCs)</h4>
        <p><b>ที่มา:</b> สารทำความเย็นในแอร์และตู้เย็น, อุตสาหกรรมโฟม</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='highlight-card'>
        <h4>5. เปอร์ฟลูออโรคาร์บอน (PFCs)</h4>
        <p><b>ที่มา:</b> การผลิตอะลูมิเนียม, การผลิตสารกึ่งตัวนำ (Electronics)</p>
    </div>
    <div class='highlight-card'>
        <h4>6. ซัลเฟอร์เฮกซะฟลูออไรด์ ($SF_6$)</h4>
        <p><b>ที่มา:</b> อุปกรณ์ไฟฟ้าแรงสูง (ใช้เป็นฉนวนไฟฟ้าใน Switchgear)</p>
    </div>
    <div class='highlight-card'>
        <h4>7. ไนโตรเจนไตรฟลูออไรด์ ($NF_3$)</h4>
        <p><b>ที่มา:</b> การผลิตจอ LCD และแผงโซลาร์เซลล์</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.caption("จัดทำเพื่อเผยแพร่ความรู้ด้านสิ่งแวดล้อม | อ้างอิงข้อมูลจาก องค์การบริหารจัดการก๊าซเรือนกระจก (องค์การมหาชน)")
