import streamlit as st

st.header("Tutoriel d'utililisation")

st.subheader("Web Of Science")
with st.expander("Récupérer les articles de recherche dans Web Of Science :", expanded=False):
    st.write("Etape 1  - Aller sur le profile du chercheur.")
    st.write("Etape 2 - Cliquer sur le nombre de publications pour afficher tous les articles de recherche du chercheur.")
    st.image(r"img/Page chercheur WoS.png",width=1000)
    st.write("Etape 3 - Cliquer sur « Exporter », puis sélectionner « Excel ».")
    st.image(r"img/Page article de recherche Excel.png", width=1000)
    st.write("Etape 4 - Sélectionner les mêmes options que sur l’image ci-dessous, puis cliquer sur « Exporter ».")
    st.image(r"img/Excel export.png",width=500)
    st.subheader("Dans le cas où le chercheur à plus de 1000 articles de recherches dans Web Of Science")
    st.write("Sachez que l’outil d’export ne peut exporter que 999 articles à la fois.")
    st.write("Veuillez ne pas entrer '1000 to 2000' mais '1001 to 2000'.")
    # st.write("Dans le cas où vous avez plusieurs fichiers à télécharger, il faut les fusionner en un seul fichier.")
    st.write("Etape 5 - Une fois le fichier téléchargé, il faut le faire changer l'extension de xls à xlsx.")

st.divider()
st.subheader("Scopus")

with st.expander("Récupérer l'identifiant Scopus :", expanded=False):
    st.write("Etape 1 - Aller sur le profile Scopus du chercheur.")
    st.image(r"img/Scopus_id.png",width=1000)
    st.write("Etape 2 - Copier-Coller l'identifiant Scopus et l'entrer dans le bon champs.")

with st.expander("Récupérer article de recherche dans Scopus :", expanded=False):
    st.write("Etape 1 - Aller sur le profile Scopus du chercheur. Puis cliquer sur le bouton 'Export All'.")
    st.image(r"img/export scopus article.png",width=1000)
    st.write("Etape 2 - Sélectionner ensuite l'extension 'CSV'.")
    st.image(r"img/enregistrement csv scopus article.png",width=1000)
    st.write("Etape 3 - Puis cliquer sur le bouton 'Export' en bas à droite.")
    st.image(r"img/Export all Scopus.png",width=1000)

st.divider()
st.subheader("Orcid")

with st.expander("Récupérer l'URL orcID du chercheur :", expanded=False):
    st.write("Etape 1 - Aller sur le profile orcID du chercheur.")
    st.write("Etape 2 - Copier-Coller l'URL indiquer en-dessous du nom du chercheur. (Regarder l'image ci-dessous.)")
    st.image(r"img/Orcid.png", width=1000)
