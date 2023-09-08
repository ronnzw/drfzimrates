# Zimbabwe Market Rates API




This is a REST API built with Django REST framework that provides access to the latest market rates in Zimbabwe. You can use this API to get the exchange rates of various currencies, commodities and services in Zimbabwe.

## Installation

To install this project, you need to have Python and Pip installed on your system. Then, clone this repository and run the following commands:

```bash
cd zim-market-rates-api
pip install -r requirements.txt
python manage.py migrate


This will install the dependencies and create the database.


##Usage
To start the server, run:

```bash
python manage.py runserver


This will launch the server on http://localhost:8000.
You can use any HTTP client to make requests to the API. The API supports the following endpoint:

- `GET /rates` - Returns a list of all available rates

The API uses JSON as the data format for both requests and responses. For example, a successful response for `GET /rates` might look like this:

```json
[
  {
    "id": 1,
    "black_market": 85.0,
    "black_market_sell": 90.0,
    "created_on": "2023-09-08T17:45:58Z"
  },
  {
    "id": 2,
    "black_market": 1800.0,
    "black_market_sell": 1850.0,
    "created_on": "2023-09-08T17:45:58Z"
  }
]



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## References

This README file was generated based on the following sources:

- [encode/django-rest-framework: Web APIs for Django. - GitHub](https://github.com/encode/django-rest-framework)
- [REST API example application - GitHub: Let’s build from here](https://github.com/bbc/REST-API-example/blob/master/README.md)
- [Working with Git and GitHub | Django documentation | Django](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/working-with-git/)
