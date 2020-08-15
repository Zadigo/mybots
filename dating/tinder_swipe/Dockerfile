FROM python

COPY Pipfile .

RUN pip install --upgrade pip

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip3 install pipenv
RUN pipenv install --deploy --system

COPY . /bot

WORKDIR /bot

CMD [ "app.py" ]

ENTRYPOINT [ "python", "-m" ]