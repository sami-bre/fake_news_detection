# Fake News Detection API

This is a FastAPI application for detecting amharic fake news.

## Installation

### Using Virtual Environment

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

### Using Virtual Environment

1. Start the FastAPI application:
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 3000
    ```

## API Endpoints

- `GET /`: Returns a welcome message.
- `POST /predict/`: Predicts whether the provided news text is fake or not.

## Example

### Request

```sh
curl -X POST "http://0.0.0.0:3000/predict/" -H "Content-Type: application/json" -d '{"text": "Some news text"}'