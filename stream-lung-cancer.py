import pickle
import streamlit as st


# membaca model
dataset_model = pickle.load(open('lung_cancer.sav', 'rb'))


#judul web
st.title('Prediksi Penyakit Kanker Paru Paru')

#membagi kolom
col1, col2, col3 = st.columns(3)


with col1 :
    GENDER = st.selectbox('Jenis Kelamin',('Laki-laki','Perempuan'))
    if GENDER == 'Perempuan':
        GENDER = 2
    if GENDER == 'Laki-laki':
        GENDER = 1
with col1 :
    AGE = st.number_input ('Input Nilai AGE')
with col1 :
    SMOKING = st.selectbox('Merokok ?',('Merokok','Tidak Merokok'))
    if SMOKING == 'Merokok':
        SMOKING = 2
    if SMOKING == 'Tidak Merokok':
        SMOKING = 1
with col1 :
    YELLOW_FINGERS = st.selectbox('Jari Kuning ?',('Ya','Tidak'))
    if YELLOW_FINGERS == 'Ya':
        YELLOW_FINGERS = 2
    if YELLOW_FINGERS == 'Tidak':
        YELLOW_FINGERS = 1
with col1 :
    ANXIETY = st.selectbox('Anxiety',('Ya','Tidak'))
    if ANXIETY == 'Ya':
        ANXIETY = 2
    if ANXIETY == 'Tidak':
        ANXIETY = 1
with col2 :
    PEER_PRESURE = st.selectbox('Peer Pressure ?',('Ya','Tidak'))
    if PEER_PRESURE == 'Ya':
        PEER_PRESURE = 2
    if PEER_PRESURE == 'Tidak':
        PEER_PRESURE = 1
with col2 :
    CHRONIC_DISEASE = st.selectbox('Memiliki Penyakit Kronis ?',('Ya','Tidak'))
    if CHRONIC_DISEASE == 'Ya':
        CHRONIC_DISEASE = 2
    if CHRONIC_DISEASE == 'Tidak':
        CHRONIC_DISEASE = 1
with col2 :
    FATIGUE = st.selectbox('Merasa Mudah Lelah ?',('Ya','Tidak'))
    if FATIGUE == 'Ya':
        FATIGUE = 2
    if FATIGUE == 'Tidak':
        FATIGUE = 1
with col2 :
    ALLERGY = st.selectbox('Memiliki Alergi ?',('Ya','Tidak'))
    if ALLERGY == 'Ya':
        ALLERGY = 2
    if ALLERGY == 'Tidak':
        ALLERGY = 1
with col2 :
    WHEEZING = st.selectbox('Merasa Wheezing ?',('Ya','Tidak'))
    if WHEEZING == 'Ya':
        WHEEZING = 2
    if WHEEZING == 'Tidak':
        WHEEZING = 1
with col3 :
    ALCOHOL_CONSUMING = st.selectbox('Mengonsumsi Alkohol ?',('Ya','Tidak'))
    if ALCOHOL_CONSUMING == 'Ya':
        ALCOHOL_CONSUMING = 2
    if ALCOHOL_CONSUMING == 'Tidak':
        ALCOHOL_CONSUMING = 1
with col3 :   
    COUGHING = st.selectbox('Batuk ?',('Ya','Tidak'))
    if COUGHING == 'Ya':
        COUGHING = 2
    if COUGHING == 'Tidak':
        COUGHING = 1
with col3 :
    SHORTNESS_OF_BREATH = st.selectbox('Sesak Nafas ?',('Ya','Tidak'))
    if SHORTNESS_OF_BREATH == 'Ya':
        SHORTNESS_OF_BREATH = 2
    if SHORTNESS_OF_BREATH == 'Tidak':
        SHORTNESS_OF_BREATH = 1
with col3 :   
    SWALLOWING_DIFFICULTY = st.selectbox('Kesulitan Menelan ?',('Ya','Tidak'))
    if SWALLOWING_DIFFICULTY == 'Ya':
        SWALLOWING_DIFFICULTY = 2
    if SWALLOWING_DIFFICULTY == 'Tidak':
        SWALLOWING_DIFFICULTY = 1
with col3 :
    CHEST_PAIN = st.selectbox('Sakit Dada ?',('Ya','Tidak'))
    if CHEST_PAIN == 'Ya':
        CHEST_PAIN = 2
    if CHEST_PAIN == 'Tidak':
        CHEST_PAIN = 1

#prediksi
lung_cancer_diagnosis = ""

#tombol prediksi
if st.button('Test prediksi kanker paru paru') :
    lung_cancer_prediction = dataset_model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])

    if(lung_cancer_prediction[0] == 1):
        lung_cancer_diagnosis = 'Pasien tidak terkena kanker paru paru'
    else :
        lung_cancer_diagnosis = 'Pasien terkena kanker paru paru'

st.success(lung_cancer_diagnosis)