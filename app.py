import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to interact with GPT-3 API for question answering
def ask_gpt3(question):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Question: {question}\nAnswer:",
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.markdown(
        """
        <footer style="position: fixed; bottom: 0; right: 0; background-color: #f0f0f0; padding: 20px 10py;">
            Developed by Ram Kumar Pandey
        </footer>
        
        """,
        unsafe_allow_html=True
    )
    st.title("Question-Answer Bot")
    st.markdown("Ask me anything!")
    user_question = st.text_input("Question:", "")
    if st.button("Generate Answer"):
        with st.spinner("Thinking..."):
            # Get response from GPT-3
            response = ask_gpt3(user_question)
            st.text_area("Answer:", value=response, height=200, max_chars=None, key=None)



if __name__ == "__main__":
    main()
