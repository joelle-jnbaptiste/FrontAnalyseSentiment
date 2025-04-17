import streamlit as st
import requests

st.title("Test de sentiment")

# État pour stocker les infos entre les actions utilisateur
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None
if "user_text" not in st.session_state:
    st.session_state.user_text = ""

# Champ de saisie
user_input = st.text_area("Entrez un message :", height=150)

if st.button("Analyser le sentiment"):
    if user_input.strip() == "":
        st.warning("Veuillez entrer un message.")
    else:
        try:
            
            response = requests.post(
                "https://web-api-sentiment.graysky-45e01b24.francecentral.azurecontainerapps.io/predict", 
                json={"text": user_input},
                verify=False
            )

            if response.status_code == 200:
                result = response.json()
                st.session_state.user_text = user_input
                st.session_state.prediction_result = result.get("prediction", 0)

                sentiment = "✅ Sentiment positif" if st.session_state.prediction_result == 1 else "❌ Sentiment négatif"
                st.subheader(sentiment)
            else:
                st.error(f"Erreur de l'API : {response.status_code}")

        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")
            
# Si on a une prédiction, on propose le feedback
if st.session_state.prediction_result is not None:
    feedback = st.radio("Cette prédiction vous semble-t-elle correcte ?", ["Oui", "Non"])
    send_feedback = st.button("Envoyer le feedback")

    if send_feedback:
        feedback_correct = feedback == "Oui"

        try:
            response = requests.post(
                "https://web-api-sentiment.graysky-45e01b24.francecentral.azurecontainerapps.io/feedback",
                json={
                    "texte": st.session_state.user_text,
                    "prediction": st.session_state.prediction_result,
                    "feedback_correct": feedback_correct
                },
                verify=False
            )

            if response.status_code == 200:
                message = response.json().get("message", "Feedback envoyé.")
                st.success(message)
            else:
                st.error(f"Erreur lors de l’envoi du feedback : {response.status_code}")

        except Exception as e:
            st.error(f"Une erreur est survenue pendant l’envoi du feedback : {e}")
