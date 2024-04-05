# Oil Selector API

Oil Selector API is a Django-based RESTful API that provides information about cars, car models, recommended products, and more.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction


Oil Selector API is crafted to aid users in discovering suitable products for their vehicles, considering factors like car make, model, and engine type. It serves as a valuable tool, especially in the automotive aftermarket industry, enabling users to find the right motor oil or auto parts for their cars. This API is also beneficial for companies offering such products to streamline their customer service and enhance user experience.

## Features

- Retrieve a list of car makes, models, and engines.
- Find recommended products for a specific car.
- Filter products by category and other criteria.
- User-friendly APIs.

## Technologies

- Python 3
- Django
- Django REST Framework
- PostgreSQL
- Docker

## Installation

1. Clone the repository: `git clone https://github.com/your-username/oilSelector.git`
2. Navigate to the project directory: `cd oilSelector`
3. Create a `.env` file in the root directory and add the following environment variables:
   ```plaintext
   # DATABASES
   DATABASE__NAME=""
   DATABASE__HOST=""
   DATABASE__PORT=""
   DATABASE__USER=""
   DATABASE__PASSWORD=""

4. Install dependencies: `pip install -r requirements.txt`
5. Set up the database: `python manage.py migrate`
6. Run the development server: `python manage.py runserver`

Or

Alternatively, configure Docker and Docker Compose:

1. Modify the Dockerfile and docker-compose.yml files as needed.
2. Build the Docker image: `docker-compose build`
3. Run the containers: `docker-compose up -d`

## Usage

1. Access the API documentation available in Postman format. See `docs/oilSelector.postman_collection.json`.
2. Use the provided endpoints to retrieve car information and recommended products.

## API Endpoints

- `/api/cars/`: List all cars.
- `/api/cars/<car_id>/`: Retrieve a specific car by ID.
- `/api/makes/`: List all car makes.
- `/api/models/`: List all car models.
- `/api/engines/`: List all car engines.
- `/api/products/`: List all products.
- `/api/products/<product_id>/`: Retrieve a specific product by ID.
- `/api/recommended-products/`: List recommended products for a specific car.
- `/api/categories/`: List all product categories.

## Testing

1. Run tests using Django's test runner: `python manage.py test`.
2. Ensure all tests pass successfully before making any changes or updates.

## Contributing

Contributions are welcome!

## Contact

For questions or support regarding this project, please contact the project maintainer at amirbalouchi73@gmail.com

