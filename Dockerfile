FROM python
WORKDIR /app
COPY . .
RUN pip install flask
CMD python main.py
