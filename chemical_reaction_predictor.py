import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw, rdChemReactions, rdDepictor
import matplotlib.pyplot as plt
import numpy as np

# Reaction prediction function using SMARTS patterns
def apply_reaction(reactants_smiles, reaction_smarts):
    try:
        reaction = rdChemReactions.ReactionFromSmarts(reaction_smarts)
        reactants = [Chem.MolFromSmiles(smi.strip()) for smi in reactants_smiles.split('+')]

        expected_reactants = reaction.GetNumReactantTemplates()
        actual_reactants = len(reactants)

        if actual_reactants != expected_reactants:
            st.error(f"Reactants provided ({actual_reactants}) do not match expected ({expected_reactants}).")
            return None

        products = reaction.RunReactants(tuple(reactants))
        if not products:
            st.error("No products found. Please check your inputs.")
            return None

        unique_products = set()
        for product_set in products:
            for product in product_set:
                smi = Chem.MolToSmiles(product)
                unique_products.add(smi)

        return list(unique_products)

    except Exception as e:
        st.error(f"Error predicting reaction: {e}")
        return None

# Function to visualize reaction mechanism
def draw_reaction_mechanism(reaction_smarts):
    try:
        reaction = rdChemReactions.ReactionFromSmarts(reaction_smarts)
        img = Draw.ReactionToImage(reaction, subImgSize=(400, 200))
        return img
    except Exception as e:
        st.error(f"Error generating mechanism diagram: {e}")
        return None

# Expanded SMARTS Patterns
reaction_smarts_dict = {
    "Bromination": "[cH:1].[Br][Br]>>[c:1][Br]",
    "Chlorination": "[cH:1].[Cl][Cl]>>[c:1][Cl]",
    "Iodination": "[cH:1].[I][I]>>[c:1][I]",
    "Fluorination": "[cH:1].[F][F]>>[c:1][F]",
    "Hydrogenation": "[C:1]=[C:2].[H][H]>>[C:1]-[C:2]",
    "Nitration": "[cH:1].[O-][N+](=O)O>>[c:1][N+](=O)[O-]",
    "Esterification": "[C:1](=O)O.[O:2][C:3]>>[C:1](=O)[O:2][C:3]",
    "Hydrolysis": "[C:1](=O)[O:2][C:3]>>[C:1](=O)O.[C:3][OH]",
    "Aldol Condensation": "[C:1]=O.[CH3][C:2]=O>>[C:1]=C-[C:2]=O",
    "Decarboxylation": "[C:1](=O)[OH]>>[C:1][H]",
    "Amide Formation": "[C:1](=O)O[C:2][H].[NH2][C:3]>>[C:1](=O)[N][C:3]",
    "Epoxidation": "[C:1]=[C:2].[O][O]>>[C:1]1[O][C:2]1",
    "Cannizzaro Reaction": "[C:1]=O.[C:2]=O>>[C:1][OH].[C:2][O-]",
    "Friedel-Crafts Acylation": "[cH:1].[C:2](=O)Cl>>[c:1][C:2](=O)",
    "Diels-Alder Reaction": "C=CC=C.C=C>>C1=CCCCC1",
    "Claisen Condensation": "[C:1](=O)O[C:2].[C:3](=O)O[C:4]>>[C:1](=O)C[C:3](=O)[C:4]",
    "Michael Addition": "[C:1]=[C:2]-[C:3]=O.[C:4]-[H]>>[C:1]([C:4])[C:2]-[C:3]=O",
    "Wittig Reaction": "[C:1]=O.[C:2]=P[CH3]3>>[C:1]=[C:2]",
    "Perkin Reaction": "[C:1](=O)O[C:2].[C:3]=O>>[C:1]=[C:3]"
}

# Streamlit UI
st.title("SMARTS-based Chemical Reaction Predictor")
st.write("Predict reaction products using SMARTS reaction rules and visualize the reaction mechanism.")

# Reaction prediction input
reactants_smiles = st.text_input("Enter Reactants (SMILES, separated by '+')", "c1ccccc1 + BrBr")
reaction_type = st.selectbox("Select Reaction Type", list(reaction_smarts_dict.keys()))

if st.button("Predict Reaction Products"):
    reaction_smarts = reaction_smarts_dict[reaction_type]
    products = apply_reaction(reactants_smiles, reaction_smarts)

    if products:
        st.subheader("Predicted Products")
        for smi in products:
            mol = Chem.MolFromSmiles(smi)
            if mol:
                img = Draw.MolToImage(mol, size=(300, 300))
                st.image(img, caption=smi)
            else:
                st.error(f"Invalid SMILES generated: {smi}")
        
        # Generate and display reaction mechanism
        mechanism_img = draw_reaction_mechanism(reaction_smarts)
        if mechanism_img:
            st.subheader("Reaction Mechanism Visualization")
            st.image(mechanism_img, caption="Reaction Mechanism")
