# app.py (version améliorée en français avec plus de fonctionnalités)

import streamlit as st
from database import (
    obtenir_clients,
    obtenir_reservations,
    obtenir_chambres_disponibles,
    ajouter_client,
    ajouter_reservation,
    obtenir_villes_hotels,
    obtenir_types_chambres
)

st.set_page_config(page_title="Système de Réservation d'Hôtel", layout="wide")
st.title("Système de Réservation d'Hôtel 🏨")

# Section Clients
st.header("👤 Liste des Clients")
clients = obtenir_clients()
if clients:
    st.table([{"ID": c[0], "Nom complet": c[6], "Email": c[4], "Téléphone": c[5]} for c in clients])
else:
    st.info("Aucun client trouvé.")

# Section Réservations
st.header("📅 Réservations")
reservations = obtenir_reservations()
if reservations:
    st.table([
        {
            "ID": r[0], "Client": r[1], "Email": r[2],
            "Arrivée": r[3], "Départ": r[4],
            "Ville": r[5], "Pays": r[6]
        } for r in reservations
    ])
else:
    st.info("Aucune réservation trouvée.")

# Section Chambres disponibles
st.header("🚪 Chambres Disponibles")
col1, col2 = st.columns(2)
with col1:
    date_debut = st.date_input("Date d'arrivée")
with col2:
    date_fin = st.date_input("Date de départ")

if date_debut and date_fin:
    chambres = obtenir_chambres_disponibles(str(date_debut), str(date_fin))
    if chambres:
        st.subheader("Chambres libres")
        st.table([
            {
                "ID": ch[0], "Numéro": ch[1], "Étage": ch[2], "Fumeurs": "Oui" if ch[3] else "Non",
                "Ville": ch[4], "Type": ch[5], "Tarif": f"{ch[6]:.2f} €"
            } for ch in chambres
        ])
    else:
        st.warning("Aucune chambre disponible pour ces dates.")

# Formulaire pour ajouter un client
st.header("➕ Ajouter un nouveau client")
with st.form(key="form_client"):
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
    submit_client = st.form_submit_button("Ajouter le client")
    if submit_client:
        if nom and email:
            ajouter_client(nom, adresse, ville, code_postal, email, telephone)
            st.success("Client ajouté avec succès !")
        else:
            st.error("Veuillez remplir au minimum le nom et l'email.")

# Formulaire pour ajouter une réservation
st.header("📝 Ajouter une réservation")
with st.form(key="form_reservation"):
    id_client = st.number_input("ID du client", min_value=1, step=1)
    date_arrivee = st.date_input("Date d'arrivée")
    date_depart = st.date_input("Date de départ")
    types = obtenir_types_chambres()
    type_options = {f"{t[1]} - {t[2]:.2f} €": t[0] for t in types}
    type_selection = st.selectbox("Type de chambre", list(type_options.keys()))

    submit_resa = st.form_submit_button("Ajouter la réservation")
    if submit_resa:
        ajouter_reservation(id_client, str(date_arrivee), str(date_depart), type_options[type_selection])
        st.success("Réservation ajoutée avec succès !")
