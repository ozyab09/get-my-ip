FROM python:3.10

WORKDIR /app

COPY . .

RUN pip3.10 install -r requirements.txt

CMD python3.10 main.py

# docker build -t ozyab/get-my-ip . && docker push ozyab/get-my-ip