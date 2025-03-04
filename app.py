import streamlit as st

# Sayfa ayarlarını yapılandırın
st.set_page_config(page_title="Projelerim - Cem Kenan Aydın", layout="wide")

# Üst kısımda sol hizalanmış kişisel bilgiler
st.title("Cem Kenan Aydın")
st.markdown("""
**Home:** Defterdar Yokuşu No:45 D:3 Cihangir/Beyoğlu/Istanbul, 34433, Istanbul, Turkey
**Email:** [cemshot@gmail.com](mailto:cemshot@gmail.com)
**Phone:** (+90) 05327172790
**Website:** [GitHub](https://github.com/cemaydinn/)
**LinkedIn:** [Profile](https://www.linkedin.com/in/cem-aydin-26461518/)
""")

st.markdown("---")

# Özgeçmiş Özeti
st.subheader("ABOUT MYSELF")
st.write("""
I have a strong foundation in Data Science and Deep Learning, and I am passionate about advancing Artificial Intelligence. I earned my certificate from the Miuul Data Science Bootcamp in August 2024, which marked my commitment to mastering the latest AI technologies. After completing a 3‑month project as a Data Analyst in Canada, I am now working as an AI Engineer in the United States.

I am experienced in developing and fine‑tuning innovative models using techniques like convolutional neural networks, recurrent neural networks, and transformers for tasks such as classification, prediction, and decision‑making. I also have strong expertise in natural language processing, including text preprocessing, sentiment analysis, named entity recognition, and topic modeling. In addition, I apply generative AI methods (such as GANs and diffusion models) to create creative solutions and innovative content.

My technical skills include advanced customer segmentation through rule‑based classification, statistical modeling for customer lifetime value prediction (CLTV), dynamic RFM analysis, intelligent rating analysis for review ranking, and A/B testing. I work fluently with data analysis libraries like Pandas, NumPy, Matplotlib, and Seaborn, as well as machine learning tools such as Scikit‑Learn, Lifetimes, and Statsmodels.

Furthermore, I design, develop, and optimize large language models (LLMs) and AI solutions using TensorFlow, PyTorch, and Keras across various applications, including image recognition and time series forecasting. I am proficient with version control using Git, and have hands‑on experience with cloud platforms (AWS, Google Cloud, Azure) and big data tools like Apache Spark and Hadoop. My background also includes API development, containerization with Docker, and integration using modern deployment practices.

My analytical and innovative approach to problem‑solving, combined with a strong commitment to staying at the forefront of technological advancements, enables me to deliver effective, real‑world solutions in both independent and team settings.
""")

st.markdown("---")

# Projeler sözlüğü: her proje için tarih, açıklama ve GitHub linkleri
projects = {
    "Airplane Seat Reservation System with AI": {
        "date": "26/01/2025 – 28/01/2025",
        "description": "Havayolu koltuk rezervasyon sisteminde yapay zeka desteği ile geliştirilmiş proje.",
        "github": "https://github.com/cemaydinn/airplane-reservation.git"
    },
    "GenAI Voice to Draw": {
        "date": "09/01/2025 – 09/01/2025",
        "description": "Sesli komutları yaratıcı çizimlere dönüştüren generative AI tabanlı bir uygulama.",
        "github": "https://github.com/cemaydinn/GenAi_VoiceDraw.git"
    },
    "RNN WheatherForcast": {
        "date": "05/01/2025 – 05/01/2025",
        "description": "RNN kullanılarak geliştirilmiş hava durumu tahmin sistemi.",
        "github": "https://github.com/cemaydinn/WheatherForcast.git"
    },
    "Song Lyrics Semantic Similarity Analysis": {
        "date": "01/01/2025 – 01/01/2025",
        "description": "Şarkı sözlerinin anlamsal benzerlik analizine dayalı proje.",
        "github": "https://github.com/cemaydinn/songlyrics.git"
    },
    "Real-Time Object Detection": {
        "date": "02/01/2025 – 03/01/2025",
        "description": "Gerçek zamanlı nesne tespiti için geliştirilen sistem.",
        "github": "https://github.com/cemaydinn/yolo_project.git"
    },
    "Big Data Developer Technical Assessment Case": {
        "date": "23/12/2024 – 28/12/2024",
        "description": "Büyük veri geliştirme teknik değerlendirme vakası.",
        "github": "https://github.com/cemaydinn/CaseStudyBigData.git"
    },
    "OCR Document Processing": {
        "date": "15/11/2024 – 18/11/2024",
        "description": "OCR teknolojisiyle belge içerisindeki metinlerin işlenmesi projesi.",
        "github": "https://github.com/cemaydinn/ocr_processor.git"
    },
    "Checking The Overfitting Breast Cancer Classification model": {
        "date": "10/12/2024 – 12/12/2024",
        "description": "Meme kanseri sınıflandırma modelindeki aşırı uyum probleminin kontrolü üzerine proje.",
        "github": "https://github.com/cemaydinn/beastcancer"
    },
    "Customer Churn Classification": {
        "date": "12/11/2024 – 18/11/2024",
        "description": "Müşteri kaybını önceden tahmin etmek için sınıflandırma modeli geliştirme projesi.",
        "github": "https://github.com/cemaydinn/bankadvisory"
    },
    "Amazon - Rating Product & Sorting Reviews": {
        "date": "24/10/2024 – 02/11/2024",
        "description": "Amazon için ürün puanlaması ve yorum sıralaması analiz projesi.",
        "github": "https://github.com/cemaydinn/amazon"
    },
    "National Institutes of Diabetes-Digestive-Kidney Diseases in the US.": {
        "date": "15/10/2024 – 17/10/2024",
        "description": "ABD'deki diyabet, sindirim ve böbrek hastalıkları üzerine odaklanmış proje.",
        "github": "https://github.com/cemaydinn/diabetes.git"
    },
    "Telco Churn Prediction": {
        "date": "10/10/2024 – 13/10/2024",
        "description": "Telekomünikasyon sektöründe müşteri kaybı tahminine yönelik proje.",
        "github": "https://github.com/cemaydinn/telco"
    },
    "Spotify - Recommendation Systems": {
        "date": "20/09/2024 – 25/09/2024",
        "description": "Spotify için öneri sistemleri geliştirme projesi.",
        "github": "Link sağlanmadı"
    },
    "Armut.com Association Rule Based Recommender System": {
        "date": "11/09/2024 – 20/09/2024",
        "description": "Armut.com için birliktelik kuralına dayalı öneri sistemi.",
        "github": "https://github.com/cemaydinn/armutcomARL"
    },
    "Flo Shoes Customer Segmentation with Unsupervised Learning": {
        "date": "06/09/2024 – 10/09/2024",
        "description": "Flo Shoes müşterilerini denetimsiz öğrenme ile segmente eden proje.",
        "github": "https://github.com/cemaydinn/flo"
    }
}

# Sol kenar çubuğunda proje seçimi
st.sidebar.title("Projelerim")
project_names = list(projects.keys())
selected_project = st.sidebar.selectbox("Bir proje seçin", project_names)

# Seçilen projenin bilgilerini ana ekranda gösterin
project = projects[selected_project]
st.markdown("---")
st.header(selected_project)
st.write(f"**Tarih:** {project['date']}")
st.write(f"**Açıklama:** {project['description']}")

if project["github"]:
    st.markdown(f"**GitHub Link:** [Repo'ya Gitmek İçin Tıklayın]({project['github']})")
else:
    st.write("GitHub linki mevcut değil.")

st.markdown("---")
st.write("Projeler hakkında daha detaylı bilgi için GitHub deposunu inceleyebilirsiniz.")