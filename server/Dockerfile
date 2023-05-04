FROM python:3.10

# Install dependencies
RUN pip install openai python-dotenv streamlit

# Copy the code
COPY src /app
WORKDIR /app

# Network port
EXPOSE 8080

# Run the app
ENTRYPOINT ["streamlit", "run", "streamlit_qa_generation.py", "--server.port=8080", "--server.address=0.0.0.0"]
