# app.py
import streamlit as st
from database import (
    obtenir_clients,
    obtenir_reservations,
    obtenir_chambres_disponibles,
    ajouter_client,
    ajouter_reservation,
    obtenir_types_chambres
)
from datetime import date

st.set_page_config(page_title="Système de Réservation d'Hôtel", layout="wide")
st.title("🏨 Système de Réservation d'Hôtel")

# Section Clients
st.header("👤 Clients")
clients = obtenir_clients()
if clients:
    st.dataframe(
        [{"ID": c[0], "Nom complet": c[6], "Email": c[4], "Téléphone": c[5]} for c in clients],
        use_container_width=True
    )
else:
    st.info("Aucun client trouvé.")

# Section Réservations
st.header("📅 Réservations")
reservations = obtenir_reservations()
if reservations:
    st.dataframe(
        [
            {
                "ID": r[0], "Client": r[1], "Email": r[2],
                "Arrivée": r[3], "Départ": r[4],
                "Ville": r[5], "Pays": r[6]
            } for r in reservations
        ],
        use_container_width=True
    )
else:
    st.info("Aucune réservation trouvée.")

# Section Chambres disponibles
st.header("🚪 Chambres Disponibles")
col1, col2 = st.columns(2)
with col1:
    date_debut = st.date_input("Date d'arrivée", value=date.today())
with col2:
    date_fin = st.date_input("Date de départ", value=date.today())

if date_debut <= date_fin:
    chambres = obtenir_chambres_disponibles(str(date_debut), str(date_fin))
    if chambres:
        st.subheader("Chambres libres")
        st.dataframe([
            {
                "ID": ch[0], "Numéro": ch[1], "Étage": ch[2], "Fumeurs": "Oui" if ch[3] else "Non",
                "Ville": ch[4], "Type": ch[5], "Tarif (€)": f"{ch[6]:.2f}"
            } for ch in chambres
        ], use_container_width=True)
    else:
        st.warning("Aucune chambre disponible pour ces dates.")
else:
    st.error("La date d'arrivée doit être avant la date de départ.")

# Formulaire pour ajouter un client
st.header("➕ Ajouter un client")
with st.form("form_client"):
    col1, col2, col3 = st.columns(3)
    with col1:
        nom = st.text_input("Nom complet")
        email = st.text_input("Email")
    with col2:
        adresse = st.text_input("Adresse")
        ville = st.text_input("Ville")
    with col3:
        code_postal = st.text_input("Code Postal")
        telephone = st.text_input("Téléphone")

    if st.form_submit_button("Ajouter le client"):
        if nom and email:
            ajouter_client(nom, adresse, ville, code_postal, email, telephone)
            st.success("Client ajouté avec succès !")
        else:
            st.error("Nom et Email sont obligatoires.")

# Formulaire pour ajouter une réservation
st.header("📝 Ajouter une réservation")
with st.form("form_reservation"):
    id_client = st.number_input("ID du client", min_value=1, step=1)
    date_arrivee = st.date_input("Date d'arrivée (réservation)", value=date.today())
    date_depart = st.date_input("Date de départ (réservation)", value=date.today())
    types = obtenir_types_chambres()
    type_options = {f"{t[1]} - {t[2]:.2f} €": t[0] for t in types}
    type_selection = st.selectbox("Type de chambre", list(type_options.keys()))

    if st.form_submit_button("Ajouter la réservation"):
        if date_arrivee <= date_depart:
            ajouter_reservation(id_client, str(date_arrivee), str(date_depart), type_options[type_selection])
            st.success("Réservation ajoutée avec succès !")
        else:
            st.error("La date d'arrivée doit être avant la date de départ.")

