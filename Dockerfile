FROM python:3.11-slim

WORKDIR /app

COPY app.py .

# Flask install karna
RUN pip install flask

# Container run karte hi app.py chalu ho
CMD ["python", "app.py"]
