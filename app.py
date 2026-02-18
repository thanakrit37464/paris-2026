from flask import Flask, render_template, request

app = Flask(__name__)

db_content = {
    "th": {
        "nav_home": "หน้าแรก",
        "nav_places": "สถานที่แนะนำ",
        "hero_title": "ปารีส 2026",
        "hero_sub": "สัมผัสความล้ำสมัยในเมืองแห่งศิลปะ",
        "lang_btn": "English",
        "lang_val": "en",
        "destinations": [
            {
                "name": "หอไอเฟล (Eiffel Tower)", 
                "desc": "สัญลักษณ์ระดับโลกที่ปีนี้มาพร้อมสวนสีเขียวรอบด้าน", 
                "long_desc": "ในปี 2026 หอไอเฟลกลายเป็นศูนย์กลางของ 'ปอดแห่งปารีส' ด้วยการขยายพื้นที่สวนสาธารณะโดยรอบให้กลายเป็นป่าในเมือง มีการติดตั้งระบบผลิตไฟฟ้าจากแรงสั่นสะเทือนของการเดินเท้าของนักท่องเที่ยว เพื่อใช้ส่องสว่างตัวหอในยามค่ำคืน",
                "img": "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?q=80&w=1000"
            },
            {
                "name": "พิพิธภัณฑ์ลูฟร์", 
                "desc": "ชมงานศิลปะระดับโลกผ่านระบบ AR สุดล้ำ", 
                "long_desc": "ลูฟร์โฉมใหม่ใช้เทคโนโลยีโฮโลแกรมและ AR (Augmented Reality) ทำให้นักท่องเที่ยวสามารถเห็นภาพประวัติศาสตร์ในอดีตซ้อนทับกับโบราณวัตถุจริง รวมถึงการเปิดโซนจัดแสดงงานศิลปะดิจิทัลที่ใหญ่ที่สุดในยุโรป",
                "img": "https://upload.wikimedia.org/wikipedia/commons/6/66/Louvre_Museum_Wikimedia_Commons.jpg"
            },
            {
                "name": "แม่น้ำแซน (Seine River)", 
                "desc": "ล่องเรือไฟฟ้าชมวิวเมืองปารีสโฉมใหม่", 
                "long_desc": "แม่น้ำแซนได้รับการฟื้นฟูจนสามารถลงว่ายน้ำได้อีกครั้ง พร้อมบริการเรือแท็กซี่ไฟฟ้าไร้คนขับที่พาคุณชมทัศนียภาพสองฝั่งน้ำอย่างเงียบสงบและเป็นมิตรต่อสิ่งแวดล้อม 100%",
                "img": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?q=80&w=1000"
            }
        ]
    },
    "en": {
        "nav_home": "Home",
        "nav_places": "Destinations",
        "hero_title": "Paris 2026",
        "hero_sub": "Experience the future of the city of arts",
        "lang_btn": "ภาษาไทย",
        "lang_val": "th",
        "destinations": [
            {
                "name": "Eiffel Tower", 
                "desc": "The global icon, now surrounded by eco-friendly parks.", 
                "long_desc": "By 2026, the Eiffel Tower sits at the heart of a vast urban forest. Innovative flooring converts visitors' footsteps into electricity to power its night-time light shows, making it more sustainable than ever.",
                "img": "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?q=80&w=1000"
            },
            {
                "name": "Louvre Museum", 
                "desc": "Explore world-class art with cutting-edge AR technology.", 
                "long_desc": "The Louvre integrates holographic guides and AR, allowing visitors to see the historical context of masterpieces. A new digital art wing showcases the fusion of traditional painting and AI creativity.",
                "img": "https://upload.wikimedia.org/wikipedia/commons/6/66/Louvre_Museum_Wikimedia_Commons.jpg"
            },
            {
                "name": "Seine River", 
                "desc": "Cruise the river on new electric boats with panoramic views.", 
                "long_desc": "The Seine is now swimmable and features autonomous electric water taxis. These zero-emission vessels offer a quiet, futuristic way to see the city's iconic architecture along the riverbanks.",
                "img": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?q=80&w=1000"
            }
        ]
    }
}

@app.route('/')
def home():
    lang = request.args.get('lang', 'th')
    data = db_content.get(lang, db_content['th'])
    return render_template('index.html', content=data, current_lang=lang)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)