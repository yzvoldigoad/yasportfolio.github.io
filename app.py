import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl(
    "https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json")
video_file_setboy = open('images/setboy.mp4', 'rb')
video_file_waifu = open('images/hehe.mp4', 'rb')
# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hallo, Gue Ilyass :wave:")
    st.title("Seorang Pelajar SMK GALILEO dari Indonesia")
    st.write("Gue orangnya suka cari tau atau bisa dibilang orangnya itu suka ngulik dan yang paling gue suka yaitu tentang pemrograman, dan bahasa pmerograman yang sekarang gue pelajari adalah Python.")
    st.write(
        "[TONTON TUTORIAL CARA MEMBUAT WEBSITE TANPA HARUS NGODING >](https://youtu.be/8PtnLp_DHhc)")

# ---- APA YANG GUE LAKUIN ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
with left_column:
    st.header("APA YANG GUE LAKUIN?")
    st.write("##")
    st.write(
        """
            Apasih waktu yang gue habisin buat sehari-hari?
            - Yang pasti gue lakuin dalam keseharian gue yaitu beribadah, ya ini udah pasti yagesya, tapi jujur sih gue masih sering ninggalin 5 waktu nya :sweat_smile:
            - SEKOLAH yap ini juga udah pasti gue lakuin terkecuali kalo lagi sakit, izin atau libur wkwkwk
            - Maen game nah ini udah pasti ga ketinggalan kalo maen game, soalnya kalo seharian belom maen game itu rasanya kaya kurang aja gitu HAHAHAHH
            - NONTON ANIMEEKKKKKK SAMA DENGERIN PLAYLIST LAGU FAVORIT GUAA :heart_eyes: DENGERIN PLAYLIST SAMA NONTON ANIMEK ITU BISA BIKIN MOOD GUE BAGUS BANGETTTT, APALAGI DENGER PLAYLIST ITU SETIAP BERANGKAT SEKOLAH, PULANG, MAU TIDUR, BELAJAR, BAHKAN PAS MANDI AKWOAKWOAKOWKA
            
            SEBENERNYA MASIH BANYAK CUMAN GUE MALAS NGETIKNYA AH KEBANYAKAN, JADI GUE KASI TAU YANG EMANG SELALU GUE LAKUIN AJA WKWKWK
            """
    )
    st.write("[YouTube Channel >](https://www.youtube.com/c/Ilyassamz15)")
    st.write("[TikTok >](https://tiktok.com/@kidskids1515)")
    st.write("[Instagram >](https://instagram.com/yasszyzz)")

with right_column:
    st_lottie(lottie_coding, height=550, key="coding")

# ---- GUE ----
with st.container():
    st.write("---")
    st.header("INI GUE")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.video(video_file_waifu)
    with text_column:
        st.subheader("FOTO BERSAMA WAIFU")
        st.write(
            """
            - INI FOTO WAKTU LAGI ADA EVENT DI CCM CITYCON YANG SEDANG HUNTING WAIFU YANG WANGY WANGY CUYYYYHH
            - NAH GUE KESINI NYA BARENG 2 ANAK SI REHAN WIBU AMA SI ARYA NGAWI :boy:
            - NAH NANTI SABTU ITU ADA EVENT LAGI DI BLOK M SQUAREEEE, TAPI JADWALNYA BENTROK SAMA PTS :sob: :sob: :sob:
            - SEDIH BANGET GA KETEMU ANIMEK, KALO MAU KETEMU HARUS NUNGGU 2 BULAN LAGI :sob: :sob: :sob:
            - PELISSSSSSS AKU PENGEN KETEMU ANIMEK HARI SABTU :cry: :cry:
            """
        )
        clicked = st.button("KLIK DISINI")
        st.write(clicked)
        if clicked:
            st.write(
                "[LIKE VT NYA CUY :point_up: :sweat_smile:](https://vt.tiktok.com/ZSRuma8Mw)")
with st.container():
    st.write("---")
    st.header("INI PLAYLIST GUE")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.video(video_file_setboy)
    with text_column:
        st.subheader("MENGSAD DULU")
        st.write(
            """
            DARI SEKIAN BANYAKNYA PLAYLIST LAGU GUE
            
            NAH INI ITU YANG PALING GUE SUKA POKONYA 10000000%
            
            HEHEHEHEH
            """
        )
        clicked = st.button("KLIK DISINII")
        st.write(clicked)
        if clicked:
            st.write(
                "[YANG MAU LINK PLAYLIST NYA](https://www.youtube.com/watch?v=OSR7qSZ6hzg&list=PLluqqQxNB4uU9gPz8wVEOnrRty8C_JqaN)")
with st.container():
    st.write("---")
    st.header("PENILAIAN WEBSITE GUE")
    st.write("##")
number = st.slider("KASIH NILAI WEBSITE GUE", 0, 100)
st.write("INI NILAI YANG GUE KASIH KE LU YAS", number)
clicked = st.button("KLIK INI KALO KALIAN NGASIH NILAI DIBAWAH 50")
st.write(clicked)
if clicked:
    st.write("KAMPRET PELIT AMAT NGASIH NILAI")

clicked = st.button("KLIK INI KALO KALIAN NGASIH NILAI 100")
st.write(clicked)
if clicked:
    st.write("TERIMAKASI TERIMAKASI TERIMAKASI")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("HUBUNGI GUE :e-mail:")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/yzvoldigoad27@gmail.com" method="POST">
        <inout type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="NAMA LU" required>
        <input type="email" name="email" placeholder="EMAIL LU" required>
        <textarea name="message" placeholder="ISI PESAN LU DISINI" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
