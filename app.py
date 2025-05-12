import streamlit as st
from database import get_clients, get_reservations, get_available_rooms, add_client, add_reservation

# Streamlit Page Title
st.title('Hotel Reservation System')

# Section for Viewing Clients
st.header('Clients List')
clients = get_clients()
if clients:
    for client in clients:
        st.write(f"ID: {client[0]}, Name: {client[1]}, Email: {client[4]}")
else:
    st.write("No clients found.")

# Section for Viewing Reservations
st.header('Reservations List')
reservations = get_reservations()
if reservations:
    for reservation in reservations:
        st.write(f"Reservation ID: {reservation[0]}, Client: {reservation[1]}, Hotel: {reservation[2]}")
else:
    st.write("No reservations found.")

# Section for Viewing Available Rooms
st.header('Available Rooms')
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if start_date and end_date:
    available_rooms = get_available_rooms(str(start_date), str(end_date))
    if available_rooms:
        for room in available_rooms:
            st.write(f"Room ID: {room[0]}, Floor: {room[2]}, Smoking: {room[3]}")
    else:
        st.write("No available rooms found for the selected dates.")

# Section for Adding a New Client
st.header('Add a New Client')
with st.form(key='add_client_form'):
    nom = st.text_input('Full Name')
    adresse = st.text_input('Address')
    ville = st.text_input('City')
    code_postal = st.text_input('Postal Code')
    email = st.text_input('Email')
    telephone = st.text_input('Telephone')

    submit_button = st.form_submit_button(label='Add Client')

    if submit_button:
        add_client(nom, adresse, ville, code_postal, email, telephone)
        st.success('Client added successfully!')

# Section for Adding a New Reservation
st.header('Add a New Reservation')
with st.form(key='add_reservation_form'):
    client_id = st.number_input('Client ID', min_value=1)
    date_arrivee = st.date_input('Arrival Date')
    date_depart = st.date_input('Departure Date')

    submit_button = st.form_submit_button(label='Add Reservation')

    if submit_button:
        add_reservation(client_id, str(date_arrivee), str(date_depart))
        st.success('Reservation added successfully!')

