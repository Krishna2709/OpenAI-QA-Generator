import openai
import os
import streamlit as st

from dotenv import load_dotenv

load_dotenv()
openai.organization = "org-Vv4q4dSusXu3Eu4FMIJ1USHb"
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_qa(prompt: str) -> str:
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content":prompt}
        ],
        max_tokens=500,
        temperature=0.2,
    )

    responses = completion.choices[0].message

    return responses


hide_menu = """
<style>
#MainMenu {visibility: hidden;}
</style>
"""

footer="""<style>
footer {visibility: hidden;}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
}

</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" crossorigin="anonymous">
<div class="footer">
<p> 
    Developed with ❤️ by Krishna Kankipati &nbsp; &nbsp;
    <a href="https://www.linkedin.com/in/krishnacse/" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
        &nbsp;&nbsp;
    <a href="https://github.com/Krishna2709" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
</p>
</div>
"""

def main():
    st.set_page_config(page_title="Q&A Generator", 
                       page_icon=None, layout="centered", 
                       initial_sidebar_state="auto")
    
    st.title("Questions and Answers Generator")
    st.subheader("Enter a passage and the number of questions you want to generate.")

    st.markdown(hide_menu, unsafe_allow_html=True)
    st.markdown(footer, unsafe_allow_html=True)

    passage = st.text_area("Enter passage: ","")
    num_questions = st.number_input("Enter number of questions: ", value=3)

    if st.button("Generate Questions"):
        if passage:
            prompt = f"""
            Given the passage: '{passage}' \
            Create {num_questions} questions related to the passage along with their answers.
            The questions and answers generate should be from the passage itself.
            The questions and answers should be grammatically correct.
            The questions and answers should be in English.
            The questions and answers should be in complete sentences.
            The questions and answers should be in the form of a question and answer pair. Use the following format: \
            
            1. Question: <question> \
               Answer: <answer> \
            
            2. Question: <question> \
               Answer: <answer> \
               
            ...

            N. Question: <question> \
                Answer: <answer> \
            """
            response = generate_qa(prompt)
            st.write("Generated Questions and Answers:")
            st.write(response['content'])
        else:
            st.warning("Please enter a passage.")

if __name__ == "__main__":
    main()