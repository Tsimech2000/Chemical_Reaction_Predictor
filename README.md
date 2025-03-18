# Chemical Reaction Predictor

## 🚀 Overview
The **Chemical Reaction Predictor** is a **Streamlit-powered web application** that predicts chemical reaction products using **SMARTS-based reaction rules**. It also provides **mechanistic visualizations** to illustrate reaction pathways.

## 🔬 Features
- Predicts reaction products based on predefined **SMARTS reaction rules**.
- Supports a wide variety of **organic reactions**.
- Provides a **reaction mechanism visualization**.
- **User-friendly Streamlit UI** for easy interaction.

## 🧪 Supported Reactions
- **Bromination, Chlorination, Iodination, Fluorination**
- **Hydrogenation, Nitration, Esterification, Hydrolysis**
- **Aldol Condensation, Decarboxylation, Amide Formation**
- **Epoxidation, Cannizzaro Reaction, Friedel-Crafts Acylation**
- **Diels-Alder Reaction, Claisen Condensation, Michael Addition**
- **Wittig Reaction, Perkin Reaction**

## 🛠️ Installation & Running the App
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Tsimech2000/chemical-reaction-predictor.git
cd chemical-reaction-predictor
```

### 2️⃣ Install Dependencies
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run chemical_reaction_predictor.py
```

## 🌍 Deploy on Streamlit Cloud
1. Push your repository to **GitHub**.
2. Visit [Streamlit Cloud](https://share.streamlit.io/).
3. Click **New App**, select your repository, and deploy!

## 🧑‍🔬 Example Input & Output
### **Example 1: Benzene Bromination**
- **Input (SMILES):** `c1ccccc1 + BrBr`
- **Predicted Product:** **Bromobenzene** (`c1ccc(cc1)Br`)
- **Mechanism Visualization:** Displays the reaction path.

## 🤝 Contributing
Want to add more reactions or improve the UI? Feel free to **fork the repo and contribute**!

---

💡 **Created for chemists, researchers, and students!** 🔬

