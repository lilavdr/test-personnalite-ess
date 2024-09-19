#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:21:49 2024

@author: lilavendrely
"""
import streamlit as st
import matplotlib.pyplot as plt

# Initialisation des variables de session
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'points' not in st.session_state:
    st.session_state.points = {i: 0 for i in range(1, 10)}

# Questions et options
questions = [
    {"question": "Ton point fort en cours :",
     "options": ["Les maths", "SES", "Activités manuelles et artistiques", "Sciences de la vie et de la terre", "Sport"]},
    {"question": "Un repas entre ami·e·s est organisé…",
     "options": ["C’est toi qui cuisine!! et attention à la première personne qui ose critiquer",
                 "… organisé de A à Z par toi évidemment, control freak va",
                 "Tu fais l’animation en racontant tes anecdotes improbable toute la soirée",
                 "Tu es ravi·e de pouvoir ramener tous tes jeux de société et partager tes nouveaux sons",
                 "C’est l’occasion d’avoir des super discussions deep dans la cuisine en petit comité"]},
    {"question": "Le duo de qualités qui te correspond :",
     "options": ["Créativité et originalité", "Ecoute et sens du dialogue", "Rigueur et organisation", 
                 "Capacité de synthèse et de rédaction", "Aisance à l’oral et capacité de persuasion"]},
    {"question": "Ton activité de rêve à Bordeaux :",
     "options": ["Dépenser tout ton argent en testant l’ensemble des ateliers de peinture sur céramique",
                 "Concert à la Rock School ou soirée à l'entrepôt, ça dépend de l’envie du jour",
                 "Combo dominical du seigneur (brocante à Saint Mich puis marché des Capu)",
                 "Verre au soleil (ouioui il y en a des fois) à Victoire",
                 "Manif et rassemblements politiques, tu connais les slogans sur Macron mieux que tes cours"]},
    {"question": "Ton film pref :",
     "options": ["Simone", "Le Loup de Wall Street", "Intouchable", "Mamma Mia", "Ratatouille"]},
    {"question": "Ta chaussure phare de 2024 :",
     "options": ["tes Birk", "Des runnings flambantes neuves (NIKE ZOOMX STREAKFLY pour préciser)",
                 "Une paire trouvée en brocante", "Spezial, Gazelle, Samba, la trend ne t’a pas échappée",
                 "Mocassins"]},
    {"question": "Ton animal totem",
     "options": ["Requin", "Araignée", "Chien", "Abeille", "Chat noir"]},
    {"question": "Ton arrêt de tram préféré :",
     "options": ["Montaigne Montesquieu", "Hôtel de ville", "CHU Pellegrin", "CAPC musée d’art contemporain", 
                 "Jardin botanique"]},
    {"question": "A quelle émission pourrais-tu participer ?",
     "options": ["Koh Lanta", "Top chef", "Qui veut gagner des millions", "La Star Academy", "Nus et culottés"]},
    {"question": "Ton application préférée :",
     "options": ["X (Twitter)", "Strava", "Tik Tok", "Duolingo", "Betclic"]},
]

points_mapping = {
    "Les maths": 1,
    "SES": [3, 5, 9],
    "Activités manuelles et artistiques": [2, 6],
    "Sciences de la vie et de la terre": [8, 7],
    "Sport": 4,
    "C’est toi qui cuisine!! et attention à la première personne qui ose critiquer": [2, 7],
    "… organisé de A à Z par toi évidemment, control freak va": 1,
    "Tu fais l’animation en racontant tes anecdotes improbable toute la soirée": 5,
    "Tu es ravi·e de pouvoir ramener tous tes jeux de société et partager tes nouveaux sons": [6, 3],
    "C’est l’occasion d’avoir des super discussions deep dans la cuisine en petit comité": [4, 8, 9],
    "Créativité et originalité": [2, 6, 7],
    "Ecoute et sens du dialogue": [8, 4],
    "Rigueur et organisation": 1,
    "Capacité de synthèse et de rédaction": [3, 5],
    "Aisance à l’oral et capacité de persuasion": [3, 9, 5],
    "Dépenser tout ton argent en testant l’ensemble des ateliers de peinture sur céramique": 2,
    "Concert à la Rock School ou soirée à l'entrepôt, ça dépend de l’envie du jour": 6,
    "Combo dominical du seigneur (brocante à Saint Mich puis marché des Capu)": [3, 7],
    "Verre au soleil (ouioui il y en a des fois) à Victoire": [1, 4, 5, 8],
    "Manif et rassemblements politiques, tu connais les slogans sur Macron mieux que tes cours": 9,
    "Simone": [3, 9],
    "Le Loup de Wall Street": 1,
    "Intouchable": [8, 4],
    "Mamma Mia": [2, 6],
    "Ratatouille": [5, 7],
    "tes Birk": 6,
    "Des runnings flambantes neuves (NIKE ZOOMX STREAKFLY pour préciser)": [4, 7],
    "Une paire trouvée en brocante": 2,
    "Spezial, Gazelle, Samba, la trend ne t’a pas échappée": [3, 5, 8],
    "Mocassins": 1,
    "Requin": 1,
    "Araignée": [2, 6],
    "Chien": [4, 5, 8],
    "Abeille": [3, 7],
    "Chat noir": 9,
    "Montaigne Montesquieu": [5, 9],
    "Hôtel de ville": [1, 3],
    "CHU Pellegrin": 8,
    "CAPC musée d’art contemporain": [2, 6],
    "Jardin botanique": [4, 7],
    "Koh Lanta": [2, 3, 4],
    "Top chef": 7,
    "Qui veut gagner des millions": 1,
    "La Star Academy": [5, 6],
    "Nus et culottés": [9, 8],
    "X (Twitter)": [9, 3],
    "Strava": [4, 8],
    "Tik Tok": [6, 7, 2],
    "Duolingo": 5,
    "Betclic": 1,
}

def next_question():
    st.session_state.current_question += 1

def previous_question():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1

def submit_answer(answer):
    st.session_state.answers.append(answer)
    if isinstance(points_mapping[answer], list):
        for point in points_mapping[answer]:
            st.session_state.points[point] += 1
    else:
        st.session_state.points[points_mapping[answer]] += 1
    next_question()

def show_results():
    st.title("Résultats")
    labels = ['Finance éthique + management ESS', 'Artisanat', 'Collectivité - Bordeaux Métropole',
              'Asso réinsertion sociale par le sport', 'Education', 'Arts, événementiel, fête, Tiers Lieu',
              'Alimentation durable', 'Médico-social', 'Association militante']
    sizes = [st.session_state.points[i] for i in range(1, 10)]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.pyplot(fig1)

# Configuration de la mise en page
st.set_page_config(page_title="Questionnaire de Personnalité ESS", layout="centered")

st.title("Questionnaire de personnalité ESS")

# Affichage des questions
if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    st.subheader(q["question"])
    
    for option in q["options"]:
        if st.button(option):
            submit_answer(option)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.current_question > 0:
            if st.button("Précédent"):
                previous_question()
    with col2:
        if st.button("Suivant"):
            next_question()
else:
    show_results()
    if st.button("Recommencer"):
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.points = {i: 0 for i in range(1, 10)}


