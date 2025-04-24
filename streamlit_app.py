import streamlit as st
import requests

st.set_page_config(page_title="Text Similarity Checker", layout='centered')

st.title("Text Similarity App")
st.markdown("Enter two sentences to check how similar they are using a semantic similarity model.")

# Input fields
text1 = st.text_area("Text 1", height=150)
text2 = st.text_area("Text 2", height=150)

# Button to trigger similarity check
if st.button("Check Similarity"):
    if text1.strip() == "" or text2.strip() == "":
        st.warning("Please fill in both text boxes.")
    else:
        payload = {
            "text1": text1,
            "text2": text2
        }

        try:
            response = requests.post("https://text-similarity-api-5pv5.onrender.com/", json=payload)
            if response.status_code == 200:
                result = response.json()
                score = result['similarity score']

                # Interpretation logic for normalized score
                if score >= 0.8:
                    st.success(f"Similarity Score: **{score}** — The texts are **highly similar**")
                elif score >= 0.5:
                    st.info(f"Similarity Score: **{score}** — The texts are **somewhat related**")
                elif score >= 0.3:
                    st.warning(f"Similarity Score: **{score}** — The texts have **low similarity**")
                else:
                    st.error(f"Similarity Score: **{score}** — The texts are **not similar**")


            else:
                st.error("Something went wrong. Please try again.")

        except Exception as e:
            st.error(f"Error: {e}")
st.markdown("---")
st.caption("Note: A normalized similarity score close to 1.0 means strong semantic similarity. Scores below 0.3 generally indicate little to no semantic overlap.")
