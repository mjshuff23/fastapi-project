# fastapi-project

A project where I am hoping to create a basic skeleton utilizing: FastAPI, Next.JS, Terraform, S3, RDS, SQS, SNS, Lambda, MyPy, Pydantic, GH CI/CD, Pre-Commit, Docker, and more.

## Steps

1. `pipenv install` - Create a new *virtual environment*, install dependencies inside *virtual environment*
   - **Useful Commands:**
      1. `pipenv shell` to get into virtual environment
      2. `pipenv run <<command>>` to run a command inside the virtual environment from **OUTSIDE** of it
      3. `pip install -r requirements.txt` - Install from `requirements.txt` file
2. `pipenv install "fastapi[all]"` - Install `FastAPI` with optional dependencies
3. Create `main.py` for `uvicorn` to run our server
4. Create basic starting code and run the server with `uvicorn main:app --reload`
   1. `uvicorn` - An ASGI (Asynchronous Server Gateway Interface) server implementation
   2. `main` - The file containing our server (`app`)
   3. `app` - The name of the variable we stored `FastAPI()` in
   4. `--reload` - Like nodemon, reload when sensing changes to code
5. You can now see `FastAPI`'s auto documentation by heading to the routes `/docs` or `/redoc`
6. Create some routes with `parameters`/`variables` and utilize `typing hints`, utilize `Unions`, etc..
7. Install `pipenv install pre-commit`
8. Create `.pre-commit-config.yaml` (pre-commit configuration file)