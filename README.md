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

Endpoint Information
The only endpoint for this application will be:

POST /predicted

The response message you will receive is:

json

{
    "message": string,
    "predicted_class": string,
    "status": string
}
