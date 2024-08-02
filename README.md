# Project Setup Instructions

This project requires Python 3.11.9 and several Python packages to be installed. Follow the instructions below to set up your development environment.

## Prerequisites

- **Python 3.11.9**: Make sure you have Python 3.11.9 installed on your system.

## Installation

1. **Install Required Packages**:

    Install the necessary packages using `pip`:

    ```sh
    pip install tensorflow==2.15.0
    pip install Flask
    pip install flask_sqlalchemy
    pip install opencv-python
    pip install pandas
    pip install matplotlib
    ```

## Verify Installation

To ensure that all packages are installed correctly, you can run the following command:

```sh
pip list

## Endpoint Information

### POST `/predicted`

This endpoint accepts a multipart/form-data request to upload a file and receive a prediction.

#### Request

The request should be a multipart/form-data with the following parts:

- **file**: The file to be uploaded for prediction.

#### Example Request

```http
POST /predicted 
Content-Type: multipart/form-data;
Content-Disposition: form-data; name="file"; value="example.png"


The response message you will receive is:

fomart : json
{
    "message": string,
    "predicted_class": string,
    "status": string
}
