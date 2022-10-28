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

## Related Screenshots

### Home Page ('/'):

<img width="1680" alt="image" src="https://user-images.githubusercontent.com/78806673/180879038-ee1686a4-8796-4469-bdce-d986ff73427a.png">

### Polls Index ('/polls'):

<img width="1680" alt="image" src="https://user-images.githubusercontent.com/78806673/180879385-34933c61-afb5-40dd-8da8-d2b49ec44248.png">

### Polls Details ('/polls/<int:id>):

<img width="1673" alt="image" src="https://user-images.githubusercontent.com/78806673/180879813-933c85a5-308c-4335-9cc6-19fce83fe464.png">

### Polls Result ('/polls/ques_id/results'):

<img width="1675" alt="image" src="https://user-images.githubusercontent.com/78806673/180881386-ad8b7a22-051d-4c32-bd5c-42e994a699fd.png">

### Polls Administration Page ('/admin):

- To Access Admin Rights first, we create Super User by running following command in terminal

```bash
     python3 manage.py createsuperuser
```

<img width="1680" alt="image" src="https://user-images.githubusercontent.com/78806673/180880461-bc4910d2-e367-4b80-a4f8-3394177e2d6b.png">
<img width="1680" alt="image" src="https://user-images.githubusercontent.com/78806673/180881089-bf815653-1e63-443f-9978-58f7e0a1cdec.png">
<img width="1680" alt="image" src="https://user-images.githubusercontent.com/78806673/180881212-935ebaa0-88d5-45aa-b1de-ec3cbcfa7e0d.png">
