## pyenv - poetry - fastapi - openai - docker

### setting environment

- pyenv
> brew install pyenv
> pyenv install --list
> pyenv install 3.11.2
> pyenv versions
> pyenv global 3.11.2

- pyenv-virtualenv
> brew install pyenv-virtualenv
> pyenv virtualenv 3.11.2 novelist
> pyenv versions
> pyenv local novelist

- poetry
> pip3 install poetry
> poetry init | poetry new novelist

- fastapi, openai
> poetry add fastapi
> poetry add "uvicorn[standard]"
> poetry add openai

- docker
> FROM python:3.11
> WORKDIR /novelist
> RUN pip install poetry
> 
> COPY pyproject.toml poetry.lock ./
> novelist novelist
> 
> RUN poetry install --no-root
> EXPOSE 8000
> ENTRYPOINT ['poetry', 'run', 'uvicorn', 'novelist.app:app', '--host', '0,0,0,0']
