#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:51:41 2024

@author: lilavendrely
"""
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Progressbar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Définir le questionnaire de personnalité ESS
questionnaire = [
    {
        "question": "Ton point fort en cours :",
        "options": ["Les maths", "SES", "Activités manuelles et artistiques", "Sciences de la vie et de la terre", "Sport"]
    },
    {
        "question": "Un repas entre ami·e·s est organisé…",
        "options": ["C’est toi qui cuisine!! et attention à la première personne qui ose critiquer",
                    "… organisé de A à Z par toi évidemment, control freak va",
                    "Tu fais l’animation en racontant tes anecdotes improbables toute la soirée",
                    "Tu es ravi·e de pouvoir ramener tous tes jeux de société et partager tes nouveaux sons",
                    "C’est l’occasion d’avoir des super discussions deep dans la cuisine en petit comité"]
    },
    {
        "question": "Le duo de qualités qui te correspond :",
        "options": ["Créativité et originalité", "Ecoute et sens du dialogue", "Rigueur et organisation",
                    "Capacité de synthèse et de rédaction", "Aisance à l’oral et capacité de persuasion"]
    },
    {
        "question": "Ton activité de rêve à Bordeaux :",
        "options": ["Dépenser tout ton argent en testant l’ensemble des ateliers de peinture sur céramique",
                    "Concert à la Rock School ou soirée à l'entrepôt, ça dépend de l’envie du jour",
                    "Combo dominical du seigneur (brocante à Saint Mich puis marché des Capu)",
                    "Verre au soleil (ouioui il y en a des fois) à Victoire",
                    "Manif et rassemblements politiques, tu connais les slogans sur Macron mieux que tes cours"]
    },
    {
        "question": "Ton film préféré :",
        "options": ["Simone", "Le Loup de Wall Street", "Intouchable", "Mamma Mia", "Ratatouille"]
    },
    {
        "question": "Ta chaussure phare de 2024 :",
        "options": ["tes Birk", "Des runnings flambantes neuves (NIKE ZOOMX STREAKFLY pour préciser)",
                    "Une paire trouvée en brocante", "Spezial, Gazelle, Samba, la trend ne t’a pas échappée", "Mocassins"]
    },
    {
        "question": "Ton animal totem :",
        "options": ["Requin", "Araignée", "Chien", "Abeille", "Chat noir"]
    },
    {
        "question": "Ton arrêt de tram préféré :",
        "options": ["Montaigne Montesquieu", "Hôtel de ville", "CHU Pellegrin", "CAPC musée d’art contemporain", "Jardin botanique"]
    },
    {
        "question": "À quelle émission pourrais-tu participer ?",
        "options": ["Koh Lanta", "Top chef", "Qui veut gagner des millions", "La Star Academy", "Nus et culottés"]
    },
    {
        "question": "Ton application préférée :",
        "options": ["X (Twitter)", "Strava", "Tik Tok", "Duolingo", "Betclic"]
    }
]

# Mapping des réponses aux catégories
categories = {
    1: "Finance éthique + management ESS",
    2: "Artisanat",
    3: "Collectivité",
    4: "Asso réinsertion sociale par le sport",
    5: "Education",
    6: "Arts, événementiel, fête, Tiers Lieu",
    7: "Alimentation durable",
    8: "Médico-social",
    9: "Association militante"
}

class QuestionnaireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Questionnaire de Personnalité ESS")
        self.root.geometry("800x600")
        self.current_question = 0
        self.answers = []
        self.points = {i: 0 for i in range(1, 10)}
        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        self.question_frame = ttk.LabelFrame(self.root, text="Question")
        self.question_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        self.question_label = ttk.Label(self.question_frame, text="", wraplength=700, font=('Helvetica', 14))
        self.question_label.pack(anchor="w", padx=10, pady=5)

        self.var = tk.StringVar()
        self.options_frame = ttk.Frame(self.question_frame)
        self.options_frame.pack(anchor="w", padx=20, pady=5)

        self.next_button = ttk.Button(self.root, text="Suivant", command=self.next_question)
        self.next_button.pack(pady=20)

        self.progress = Progressbar(self.root, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress.pack(pady=5)

    def show_question(self):
        question = questionnaire[self.current_question]
        self.question_label.config(text=question["question"])

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for option in question["options"]:
            rb = ttk.Radiobutton(self.options_frame, text=option, variable=self.var, value=option)
            rb.pack(anchor="w", padx=20, pady=2)

        self.progress['value'] = (self.current_question / len(questionnaire)) * 100

    def next_question(self):
        answer = self.var.get()
        if not answer:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner une réponse.")
            return

        self.answers.append(answer)
        self.current_question += 1

        if self.current_question < len(questionnaire):
            self.show_question()
        else:
            self.calculate_results()
            self.show_results()

    def calculate_results(self):
        mapping = [
            ["Les maths", 1], ["SES", 3], ["Activités manuelles et artistiques", 2], ["Sciences de la vie et de la terre", 8], ["Sport", 4],
            ["C’est toi qui cuisine!! et attention à la première personne qui ose critiquer", 2], ["… organisé de A à Z par toi évidemment, control freak va", 1],
            ["Tu fais l’animation en racontant tes anecdotes improbables toute la soirée", 5], ["Tu es ravi·e de pouvoir ramener tous tes jeux de société et partager tes nouveaux sons", 6],
            ["C’est l’occasion d’avoir des super discussions deep dans la cuisine en petit comité", 4], ["Créativité et originalité", 2], ["Ecoute et sens du dialogue", 8],
            ["Rigueur et organisation", 1], ["Capacité de synthèse et de rédaction", 3], ["Aisance à l’oral et capacité de persuasion", 3], ["Dépenser tout ton argent en testant l’ensemble des ateliers de peinture sur céramique", 2],
            ["Concert à la Rock School ou soirée à l'entrepôt, ça dépend de l’envie du jour", 6], ["Combo dominical du seigneur (brocante à Saint Mich puis marché des Capu)", 3],
            ["Verre au soleil (ouioui il y en a des fois) à Victoire", 1], ["Manif et rassemblements politiques, tu connais les slogans sur Macron mieux que tes cours", 9], ["Simone", 3],
            ["Le Loup de Wall Street", 1], ["Intouchable", 8], ["Mamma Mia", 2], ["Ratatouille", 5], ["tes Birk", 6], ["Des runnings flambantes neuves (NIKE ZOOMX STREAKFLY pour préciser)", 4],
            ["Une paire trouvée en brocante", 2], ["Spezial, Gazelle, Samba, la trend ne t’a pas échappée", 3], ["Mocassins", 1], ["Requin", 1], ["Araignée", 2], ["Chien", 4], ["Abeille", 3], ["Chat noir", 9],
            ["Montaigne Montesquieu", 5], ["Hôtel de ville", 1], ["CHU Pellegrin", 8], ["CAPC musée d’art contemporain", 2], ["Jardin botanique", 4], ["Koh Lanta", 2], ["Top chef", 7],
            ["Qui veut gagner des millions", 1], ["La Star Academy", 5], ["Nus et culottés", 9], ["X (Twitter)", 9], ["Strava", 4], ["Tik Tok", 6], ["Duolingo", 5], ["Betclic", 1]
        ]

        for answer in self.answers:
            for map_answer, category in mapping:
                if answer == map_answer:
                    self.points[category] += 1

    def show_results(self):
        total_points = sum(self.points.values())
        percentages = {k: (v / total_points) * 100 for k, v in self.points.items()}

        labels = [categories[k] for k in self.points.keys()]
        sizes = [v for v in percentages.values()]

        # Graphique en secteurs
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(labels))))
        ax.axis('equal')
        plt.title("Résultats du questionnaire de personnalité ESS")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Masquer les éléments de l'interface utilisateur
        self.question_frame.pack_forget()
        self.next_button.pack_forget()
        self.progress.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuestionnaireApp(root)
    root.mainloop()




