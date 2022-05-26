# fastapi-project

A project where I am hoping to create a basic skeleton utilizing: FastAPI, Next.JS, Terraform, S3, RDS, SQS, SNS, Lambda, MyPy, Pydantic, GH CI/CD, Pre-Commit, Docker, and more.

## Steps

1. `pipenv install` - Create a new _virtual environment_, install dependencies inside _virtual environment_
   - **Useful Commands:**
     1. `pipenv shell` to get into virtual environment
     2. `pipenv run <<command>>` to run a command inside the virtual environment from **OUTSIDE** of it
     3. `pip install -r requirements.txt` - Install from `requirements.txt` file
2. **FastAPI:**
   1. `pipenv install "fastapi[all]"` - Install `FastAPI` with optional dependencies
   2. Create `main.py` for `uvicorn` to run our server
   3. Create basic starting code and run the server with `uvicorn main:app --reload`
      1. `uvicorn` - An ASGI (Asynchronous Server Gateway Interface) server implementation
      2. `main` - The file containing our server (`app`)
      3. `app` - The name of the variable we stored `FastAPI()` in
      4. `--reload` - Like nodemon, reload when sensing changes to code
   4. You can now see `FastAPI`'s auto documentation by heading to the routes `/docs` or `/redoc`
   5. Create some routes with `parameters`/`variables` and utilize `typing hints`, utilize `Unions`, etc..
3. **Pre-Commit:**
   1. Install `pipenv install pre-commit`
   2. Create `.pre-commit-config.yaml` (pre-commit configuration file). View sample with `pre-commit sample-config`
      1. **`WARNING`**: The `sample-config` is out of date and may cause an error with `Black`
   3. Run `pre-commit install` to set up the git hook scripts (now pre-commit will run automatically on git commit)
   4. `pre-commit run --all-files` to run pre-commit on all files
   5. `pre-commit autoupdate` update all revisions in `.pre-commit-config.yaml`
