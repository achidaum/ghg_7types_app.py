import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="GHG คืออะไร? - 7 ก๊าซเรือนกระจก",
    page_icon="🌍",
    layout="wide"
)

# ตกแต่ง CSS แบบจัดเต็ม (ใส่ Animation และ Gradient)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Kanit', sans-serif;
    }

    /* ตกแต่งส่วนหัวเรื่องให้มี Gradient และเงา */
    .header-container {
        background: linear-gradient(135deg, #1B5E20 0%, #43A047 100%);
        padding: 60px 20px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        animation: fadeIn 1.5s ease-in-out;
    }

    .main-title {
        color: #FFFFFF;
        font-size: 64px;
        font-weight: 800;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .sub-title {
        color: #E8F5E9;
        font-size: 30px;
        font-weight: 400;
        margin-top: 0px;
        opacity: 0.9;
    }

    /* Animation สำหรับการโหลดหน้าเว็บ */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* ตกแต่ง Card ให้ดูหรูหรา (Glassmorphism นิดๆ) */
    .ghg-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #E0E0E0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        margin-bottom: 20px;
        min-height: 200px;
    }

    .ghg-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 12px 25px rgba(46, 125, 50, 0.2);
        border-color: #2E7D32;
    }

    .ghg-card h4 {
        color: #2E7D32;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
    }

    .ghg-card p {
        font-size: 16px;
        color: #455A64;
        line-height: 1.6;
    }

    .source-tag {
        background: #E8F5E9;
        color: #2E7D32;
        padding: 5px 12px;
        border-radius: 50px;
        font-size: 14px;
        font-weight: 600;
        display: inline-block;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ส่วนหัวเรื่อง (โชว์แบบสวยงาม) ---
st.markdown("""
    <div class="header-container">
        <h1 class="main-title">GHG คืออะไร?</h1>
        <p class="sub-title">เจาะลึก 7 ก๊าซเรือนกระจก ตัวการทำโลกเดือด</p>
    </div>
    """, unsafe_allow_html=True)

# --- เนื้อหาอธิบายสั้นๆ ---
st.markdown("### 🌍 หัวใจสำคัญของปรากฏการณ์เรือนกระจก")
st.write("""
ก๊าซเรือนกระจก (**GHG**) เปรียบเสมือน **'ผ้าห่มของโลก'** ที่คอยดักจับรังสีความร้อน ไม่ให้หลุดออกไปนอกชั้นบรรยากาศ 
ซึ่งหากมีในปริมาณที่พอดีจะทำให้โลกอุ่นสบาย แต่กิจกรรมของมนุษย์กำลังทำให้ผ้าห่มนี้หนาขึ้นจนโลกเกิดภาวะวิกฤต
""")


st.write("---")

# --- ส่วนชนิดก๊าซ 7 ชนิด (Layout สวยๆ) ---
st.markdown("### 📊 ทำความรู้จัก 7 ตัวร้าย (อ้างอิง อบก. & พิธีสารเกียวโต)")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='ghg-card'>
        <h4>🌡️ 1. คาร์บอนไดออกไซด์ (CO<sub>2</sub>)</h4>
        <p>ตัวการหลักที่เกิดจากการใช้พลังงานฟอสซิล การคมนาคม และการทำลายพื้นที่ป่าไม้ทั่วโลก</p>
        <span class='source-tag'>ตัวการอันดับ 1</span>
    </div>
    <div class='ghg-card'>
        <h4>🐄 2. มีเทน (CH<sub>4</sub>)</h4>
        <p>กักความร้อนเก่งกว่า CO2 หลายเท่า เกิดจากการทำปศุสัตว์ นาข้าว และการเน่าเสียของขยะ</p>
        <span class='source-tag'>แรงกว่า CO2 28 เท่า</span>
    </div>
    <div class='ghg-card'>
        <h4>🚜 3. ไนตรัสออกไซด์ (N<sub>2</sub>O)</h4>
        <p>ผลพลอยได้จากการใช้ปุ๋ยเคมีในไร่นา และกระบวนการผลิตในโรงงานอุตสาหกรรมหนัก</p>
    </div>
    <div class='ghg-card'>
        <h4>❄️ 4. ไฮโดรฟลูออโรคาร์บอน (HFCs)</h4>
        <p>สารทำความเย็นที่เราใช้ในแอร์และตู้เย็นทุกบ้าน เป็นก๊าซสังเคราะห์ที่กักความร้อนได้สูงมาก</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='ghg-card'>
        <h4>🏗️ 5. เปอร์ฟลูออโรคาร์บอน (PFCs)</h4>
        <p>ก๊าซจากการถลุงอะลูมิเนียมและการผลิตสารกึ่งตัวนำในอุปกรณ์อิเล็กทรอนิกส์</p>
    </div>
    <div class='ghg-card'>
        <h4>⚡ 6. ซัลเฟอร์เฮกซะฟลูออไรด์ (SF<sub>6</sub>)</h4>
        <p>ก๊าซที่ร้ายแรงที่สุดในบรรดา 7 ชนิด ใช้เป็นฉนวนในอุปกรณ์ไฟฟ้าแรงสูง</p>
        <span class='source-tag'>ร้ายแรงที่สุด</span>
    </div>
    <div class='ghg-card'>
        <h4>📱 7. ไนโตรเจนไตรฟลูออไรด์ (NF<sub>3</sub>)</h4>
        <p>ตัวการน้องใหม่จากการผลิตจอ LCD และแผงโซลาร์เซลล์ ที่มีค่าศักยภาพโลกร้อนสูงมาก</p>
    </div>
    <div style='text-align: center; padding-top: 10px;'>
        <p style='color: #2E7D32; font-weight: 700; font-size: 20px;'>🌱 เริ่มต้นลด Carbon Footprint วันนี้ เพื่อโลกที่ยั่งยืน</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Dashboard by Streamlit | ข้อมูลอ้างอิง: องค์การบริหารจัดการก๊าซเรือนกระจก (TGO)")
