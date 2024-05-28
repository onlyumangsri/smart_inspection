# Smart Visual Inspection System

The Smart Visual Inspection System is a FastAPI application for managing visual inspections at inspection stations. It allows users to perform CRUD operations on inspection stations and inspections, filter inspections, and paginate results.

## Dependencies

- Python 3.9 or higher
- FastAPI
- SQLAlchemy
- uvicorn
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/onlyumangsri/smart-visual-inspection.git
    cd smart-visual-inspection
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running Locally

1. Start the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the API documentation:

    Open your web browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to interact with the API using Swagger UI.

## Building and Running in a Containerized Environment

1. Build the Docker image:

    ```bash
    docker build -t smart-visual-inspection .
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 smart-visual-inspection
    ```

3. Access the API documentation:

    Open your web browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to interact with the API using Swagger UI.

## Configuration

- Database connection details can be configured in `database.py`.
- FastAPI application settings can be adjusted in `main.py`.
- Dockerfile can be modified to include additional configurations or dependencies.

## Usage

- Create, read, update, and delete inspection stations using the provided endpoints.
- Perform inspections and filter results by station ID, product, etc.
- Access the API documentation to explore available endpoints and their parameters.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
