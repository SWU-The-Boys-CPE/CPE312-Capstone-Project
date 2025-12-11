# Script for Capstone Project Presentation
## Project: Bangkok Traffic Congestion Index Prediction
## Team: The Boys

---

### **Part 1: Introduction & Project Overview**
**Speaker: Nitipoom Potichai (Project Manager)**
**Slides: 1-6**

**(Slide 1: Title Slide)**
**Nitipoom:** สวัสดีครับอาจารย์และเพื่อนๆ ทุกคน พวกเราทีม **The Boys** วันนี้จะมานำเสนอ Capstone Project ในหัวข้อ **"Bangkok Traffic Congestion Index Prediction"** หรือการทำนายดัชนีรถติดในกรุงเทพมหานครครับ

**(Slide 2: Agenda)**
**Nitipoom:** สำหรับหัวข้อที่เราจะพูดถึงในวันนี้ (Agenda) จะเริ่มตั้งแต่ที่มาและความสำคัญของปัญหา เป้าหมายของโปรเจกต์ การจัดการข้อมูล การสร้างโมเดล ไปจนถึงผลลัพธ์และข้อเสนอแนะทางธุรกิจครับ

**(Slide 3: Introduction & Problem Statement)**
**Nitipoom:** เริ่มต้นที่ปัญหากันก่อนครับ อย่างที่เราทราบกันดีว่า "กรุงเทพฯ" ติดอันดับเมืองที่รถติดที่สุดในโลก ซึ่งสร้างความเสียหายทั้งทางเศรษฐกิจและคุณภาพชีวิต ปัญหาคือเราขาดเครื่องมือที่จะบอกเราล่วงหน้าว่า "วันนี้รถจะติดแค่ไหน" อย่างแม่นยำ
ดังนั้น **Opportunity** ของเราคือการใช้ข้อมูลในอดีต ทั้งข้อมูลจราจรและสภาพอากาศ มาสร้างโมเดลเพื่อทำนายค่า **Traffic Congestion Index (TCI)** เพื่อให้คนวางแผนการเดินทางได้ดีขึ้นครับ

**(Slide 4: Project Objectives)**
**Nitipoom:** เป้าหมายหลัก (Primary Objective) ของเราคือ สร้าง Machine Learning Model ที่ทำนายค่า TCI ได้แม่นยำ โดยมีค่า **$R^2$ มากกว่า 0.70** ครับ
ส่วนเป้าหมายรอง คือเราต้องการรู้ว่าปัจจัยอะไรบ้างที่ทำให้รถติด (เช่น ฝนตก หรือ วันศุกร์) และเปรียบเทียบประสิทธิภาพของโมเดลต่างๆ ครับ

**(Slide 5: Scope & Limitations)**
**Nitipoom:** ขอบเขตของงาน (Scope) เราโฟกัสที่พื้นที่กรุงเทพฯ และปริมณฑล ใช้ข้อมูลย้อนหลังตั้งแต่ปี 2019-2025 โดยทำนายเป็นรายวัน (Daily Aggregation) ครับ
ข้อจำกัด (Limitations) คือเรายังไม่มีข้อมูล Real-time รายชั่วโมง และโมเดลอาจจะไม่ครอบคลุมเหตุการณ์พิเศษ เช่น การชุมนุม หรืออุบัติเหตุใหญ่ๆ ครับ

**(Slide 6: Team Roles)**
**Nitipoom:** สมาชิกในทีมของเราประกอบด้วย
1. ผม **Nitipoom** เป็น Project Manager ดูแลภาพรวมครับ
2. **Veerkawin** เป็น Data Analyst ดูแลเรื่องข้อมูล
3. **Kamin** เป็น Data Scientist ดูแลเรื่องโมเดล
4. **Yossawee** ดูแลเรื่อง Visualization และผลลัพธ์
5. **Krittapas** เป็น Tech Lead ดูแลเรื่อง Deployment ครับ
ต่อไปขอส่งต่อให้คุณ Veerkawin พูดถึงเรื่องข้อมูลครับ

---

### **Part 2: Data Management & EDA**
**Speaker: Veerkawin Naknithichairat (Data Analyst)**
**Slides: 7-11**

**(Slide 7: Data Collection)**
**Veerkawin:** ขอบคุณครับ สำหรับข้อมูลที่เราใช้ (Data Collection) มาจาก 2 แหล่งหลักครับ
1. **Traffic Data:** จาก TomTom Traffic Index เก็บค่าความหนาแน่นจราจร
2. **Weather Data:** จาก OpenWeatherMap API เก็บค่าอุณหภูมิ ปริมาณฝน และความชื้นครับ

**(Slide 8: Data Overview)**
**Veerkawin:** ภาพรวมของข้อมูล (Data Overview) เรามีข้อมูลจราจรดิบ 1,682 วัน และข้อมูลอากาศ 365 วัน เมื่อนำมา Clean และ Merge กันแล้ว เราเหลือข้อมูลที่สมบูรณ์พร้อมใช้ประมาณ 351 ตัวอย่าง (Samples) โดยมี Features ทั้งหมด 33 ตัวครับ ตัวแปรตาม (Target) ของเราคือ `congestion_index` ครับ

**(Slide 9: Data Cleaning & Preprocessing)**
**Veerkawin:** ขั้นตอนการเตรียมข้อมูล (Cleaning)
1. เราจัดการ Missing Values ด้วยการ Interpolation ในจุดเล็กน้อย และตัดข้อมูลที่ Target หายไปทิ้ง
2. กำจัด Outliers ในข้อมูลปริมาณรถด้วยวิธี IQR
3. แปลง Data Type ให้ถูกต้อง และ Merge ข้อมูลทั้งสองแหล่งเข้าด้วยกันด้วย `date` ครับ

**(Slide 10: EDA - Traffic)**
**Veerkawin:** จากการวิเคราะห์ข้อมูลจราจร (EDA Traffic) เราพบ Pattern ที่น่าสนใจครับ
- **รายสัปดาห์:** รถจะติดสูงสุดในวันศุกร์ และโล่งที่สุดในวันอาทิตย์ (ตามกราฟ)
- **รายฤดูกาล:** ช่วงเปิดเทอมและหน้าแล้ง (Nov-Feb) รถจะติดกว่าปกติครับ
- การกระจายตัวของข้อมูลเป็นแบบ Normal Distribution ซึ่งดีต่อการทำ Regression ครับ

**(Slide 11: EDA - Weather)**
**Veerkawin:** ส่วนความสัมพันธ์กับสภาพอากาศ (EDA Weather)
- **อุณหภูมิ (Temp):** มี Correlation สูงมากกับรถติด คือ "ยิ่งร้อน รถยิ่งติด" อาจเพราะคนหนีร้อนมาใช้รถส่วนตัวหรือเปิดแอร์
- **ฝน (Rainfall):** มีผลกระทบปานกลาง คือทำให้รถชะลอตัว
ต่อไปคุณ Kamin จะมาเล่าเรื่องการสร้างโมเดลครับ

---

### **Part 3: Model Development**
**Speaker: Kamin Surakhajorn (Data Scientist)**
**Slides: 12-15**

**(Slide 12: Feature Engineering)**
**Kamin:** ครับ ในส่วนของ Feature Engineering เราสร้างตัวแปรใหม่ๆ เพื่อเพิ่มประสิทธิภาพโมเดลครับ
1. **Rolling Statistics:** ค่าเฉลี่ยย้อนหลัง 7 วัน และ 14 วัน เพื่อจับ Trend ระยะสั้น
2. **Lag Features:** ค่ารถติดของเมื่อวาน (Lag 1) และสัปดาห์ที่แล้ว (Lag 7) เพื่อดู Pattern เดิม
3. **Temporal Features:** แปลงวันและเดือนเป็นค่า Sin/Cos เพื่อให้โมเดลเข้าใจความเป็นวัฏจักร (Cyclical) ครับ

**(Slide 13: Model Selection Strategy)**
**Kamin:** กลยุทธ์การเลือกโมเดล เราทดลอง 3 โมเดลครับ
1. **Linear Regression:** เป็น Baseline ที่เข้าใจง่าย
2. **XGBoost:** เก่งเรื่องข้อมูลที่มีความซับซ้อน
3. **Random Forest:** เก่งเรื่องลด Overfitting และบอกความสำคัญของตัวแปรได้
โดยเราตั้งเกณฑ์ไว้ว่า $R^2$ ต้องมากกว่า 0.70 ครับ

**(Slide 14: Model Results - Linear Regression)**
**Kamin:** ผลลัพธ์โมเดลแรก **Linear Regression**
- ทำได้ดีเกินคาดครับ ได้ค่า **$R^2$ = 0.7742**
- RMSE อยู่ที่ 2.06
- แสดงว่าความสัมพันธ์ของข้อมูลส่วนใหญ่เป็นเส้นตรง (Linear) ครับ

**(Slide 15: Model Results - XGBoost)**
**Kamin:** โมเดลที่สอง **XGBoost**
- ได้ค่า **$R^2$ = 0.7359** ซึ่งน้อยกว่า Linear นิดหน่อย
- และเริ่มเห็นสัญญาณของ Overfitting เล็กน้อยครับ
ต่อไปคุณ Yossawee จะมาเฉลยโมเดลที่ดีที่สุดของเราครับ

---

### **Part 4: Results & Insights**
**Speaker: Yossawee Pimratkasem (Visualization)**
**Slides: 16-19**

**(Slide 16: Model Results - Random Forest)**
**Yossawee:** ขอบคุณครับ และพระเอกของเราในวันนี้คือ **Random Forest** ครับ
- หลังจากเราทำ Hyperparameter Tuning แล้ว ค่า **$R^2$ พุ่งไปถึง 0.9645** ครับ!
- RMSE ลดเหลือแค่ 0.81 ซึ่งต่ำมาก
- ถือว่าผ่านเกณฑ์ที่เราตั้งไว้แบบขาดลอยครับ (Significantly Exceeds)

**(Slide 17: Model Comparison)**
**Yossawee:** เมื่อเปรียบเทียบทั้ง 3 โมเดล (ตาราง)
- **อันดับ 1:** Random Forest (แม่นยำที่สุด)
- **อันดับ 2:** Linear Regression
- **อันดับ 3:** XGBoost
สรุปคือ Random Forest เหมาะที่สุดสำหรับการนำไปใช้งานจริงที่ต้องการความแม่นยำสูงครับ

**(Slide 18: Feature Importance)**
**Yossawee:** แล้วอะไรทำให้รถติด? (Feature Importance)
- อันดับ 1 คือ **อุณหภูมิ (Temp Avg)** ครับ มีความสำคัญถึง **46.9%**
- รองลงมาคือ **Rolling Mean 7 วัน** (19.2%)
- จะเห็นว่า "สภาพอากาศ" มีผลมากกว่า "ประวัติรถติดในอดีต" เสียอีกครับ

**(Slide 19: Key Insights)**
**Yossawee:** Insight ที่เราได้คือ
1. **Weather Dominance:** สภาพอากาศมีผลต่อการทำนายเกิน 50%
2. **Temperature Impact:** อากาศร้อน = รถติด (Correlation ชัดเจน)
3. **History Repeats:** การดูเทรนด์ย้อนหลัง 7 วัน แม่นยำกว่าดูแค่เมื่อวาน (Lag) ครับ
ต่อไปคุณ Krittapas จะมาสรุปและเสนอแนะแนวทางครับ

---

### **Part 5: Conclusion & Future Work**
**Speaker: Krittapas Imtour (Tech Lead)**
**Slides: 20-24**

**(Slide 20: Hypothesis Validation)**
**Krittapas:** ครับ มาตรวจสอบสมมติฐานกัน (Hypothesis Validation)
- **H1:** $R^2 > 0.70$ -> **ผ่าน** (ได้ 0.96)
- **H2:** Complex Model ดีกว่า Simple -> **ผ่าน** (RF ชนะ Linear)
- **H3:** อากาศมีผลมาก -> **ผ่าน** (สำคัญ 55%)
- **H4:** Lag Feature สำคัญที่สุด -> **ไม่ผ่าน** (เพราะอากาศสำคัญกว่า)

**(Slide 21: Business Recommendations)**
**Krittapas:** ข้อเสนอแนะ (Recommendations)
- **ภาครัฐ:** ควรเพิ่มพื้นที่สีเขียวเพื่อลดอุณหภูมิเมือง ซึ่งจะช่วยลดรถติดทางอ้อมได้ และปรับไฟจราจรตามพยากรณ์อากาศ
- **คนเดินทาง:** ให้วางแผนล่วงหน้าโดยดูเทรนด์ 7 วัน และถ้าวันไหนอากาศร้อนจัด ให้เผื่อเวลาเดินทางเพิ่มครับ

**(Slide 22: Deployment Strategy)**
**Krittapas:** แผนการนำไปใช้ (Deployment)
- เราจะดึงข้อมูลรายวันจาก API -> เข้า Pipeline เพื่อ Clean และสร้าง Feature -> ให้ Random Forest ทำนาย -> แสดงผลบน Dashboard
- และต้องมีการ Retrain โมเดลทุกเดือนเพื่อให้ทันต่อการเปลี่ยนแปลงของเมืองครับ

**(Slide 23: Challenges)**
**Krittapas:** ความท้าทายที่เจอ
- ข้อมูลเราเป็นรายวัน (Daily) ทำให้บอกละเอียดเป็นรายชั่วโมงไม่ได้
- ตอนแรกโมเดล Overfit แต่เราแก้ด้วยการจูน Hyperparameter จนได้ผลลัพธ์ที่ดีครับ

**(Slide 24: Future Work & Conclusion)**
**Krittapas:** ในอนาคต เราอยากทำนายแบบ Real-time รายชั่วโมง และเจาะจงรายเขตครับ
**บทสรุป:** โปรเจกต์นี้พิสูจน์แล้วว่า เราสามารถทำนายรถติดได้แม่นยำถึง 96% และค้นพบว่า "อุณหภูมิ" คือตัวแปรสำคัญที่ถูกมองข้ามครับ

พวกเราทีม **The Boys** ขอจบการนำเสนอเพียงเท่านี้ครับ ขอบคุณครับ!
(Q&A Session)
