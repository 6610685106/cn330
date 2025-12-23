# Weather CLI Application

## Overview
Weather CLI Application เป็นโปรแกรมแบบ Command Line ที่พัฒนาด้วยภาษา Python  
โดยเชื่อมต่อกับ **OpenWeatherMap API** เพื่อแสดงข้อมูลสภาพอากาศแบบเรียลไทม์  
ผู้ใช้สามารถเรียกดูข้อมูลผ่านคำสั่ง CLI และสามารถรันโปรแกรมผ่าน Docker ได้

---

## Features
- `help` : แสดงคำสั่งทั้งหมดที่รองรับ
- `list` : แสดงประเภทข้อมูลสภาพอากาศที่สามารถเรียกดูได้
- `current` : แสดงสภาพอากาศปัจจุบันของเมืองที่ระบุ
- `forecast` : แสดงพยากรณ์อากาศล่วงหน้า 5 วัน

---

## Requirements
- Python 3.10+
- Docker & Docker Compose
- OpenWeatherMap API Key
- install requirements.txt

---

### 1. Clone Repository
```bash
git clone https://github.com/your-org/weather-cli.git
cd weather-cli
