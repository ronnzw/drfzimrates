We are grateful for your interest in contributing to our Django project that uses Django REST framework. We welcome all contributions, big or small.


# Getting started

Before you start contributing, please take a moment to read through our contribution guidelines. These guidelines will help you to make sure that your contributions are consistent with the project's style and standards.

### Where to start contribute

There are many ways to contribute to the project. Here are a few ideas:
1. We welcome it if you need new features go ahead and raise an issue we will evalutate and discuss with you
2. Read through the issues that already exist and pick one that is interesting to you.
3. We also welcome contribution around documentation


## How to start contributing

1. Fork the repository

2. Clone the repository
```bash
git clone https://github.com/ronnzw/drfzimrates.git
```
3. Create a new branch for your changes using:
```bash
git checkout -b \<branch_name\>
```

4. Install requirements and run migrations
```bash
cd drfzimrates
pip install -r requirements.txt
python manage.py migrate
```
5. Run the server to ensure everything is working as expected
```bash
python manage.py runserver
```
Access your local server on `http://localhost:8000/`

6. Make your changes

7. Then run coverage and check if the sections you added are included in the coverage at least 80%
```bash
coverage run --source='.' manage.py test rates
coverage html
```

8. Write you test using the default Django Testcases and run test
```bash
./manage.py test
```

9. Commit and push your branch to your fork

10. Create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) on the main repository.

### Code review

Once you have submitted a pull request, it will be reviewed by other contributors. Please be patient and responsive to any comments or suggestions.

### Merging your pull request

Once your pull request has been reviewed and approved, it will be merged into the main repository.

**Thank you!**

We appreciate your contributions to the project. Your help makes the project better for everyone!