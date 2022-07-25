# Django-Polls-App

Polls is a simple Django app that allows you to create polls and vote on them.
It has its admin interface and allows you to add, delete, and update questions and choices.

# Testing Django-Polls-App

### Clone the repository
- Clone the repository from [GitHub](https://github.com/AfaqShuaib09/Django-Polls-App)

```bash
git clone https://github.com/AfaqShuaib09/Django-Polls-App
```

### Navigate to the directory
- Change your current pwd (Present Working Direvctory) to the directory where the repository is cloned

```bash
cd Django-Polls-App
```

### Create Virtual Environment
- In the project directory, you can create a virtual environment by running the following command in the terminal:

```bash
   python3 -m venv env
```
- Activate the virtual environment by running the following command in the terminal:
```bash
   source env/bin/activate
```

- Install the dependencies by running the following command in the terminal:
```bash
   pip install -r requirements.txt
```

### Run the tests
- Run the tests (Unit tests) in tests.py of the polls directory

```bash
    python3 manage.py test polls
```

### Run the Django App
```bash
    python3 manage.py runserver
```
