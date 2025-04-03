# API Documentation

## Overview
This document provides an overview of the API endpoints available in the Robotics Dashboard application. Each endpoint is described with its purpose, request method, parameters, and response format.

## Endpoints

### 1. Get Robot Specifications
- **Endpoint:** `/api/robots`
- **Method:** `GET`
- **Description:** Retrieves a list of all robot specifications.
- **Response:**
  - **200 OK**
    ```json
    {
      "robots": [
        {
          "id": "string",
          "name": "string",
          "specifications": {
            "weight": "number",
            "dimensions": {
              "length": "number",
              "width": "number",
              "height": "number"
            },
            "capabilities": ["string"]
          }
        }
      ]
    }
    ```

### 2. Create a New Robot
- **Endpoint:** `/api/robots`
- **Method:** `POST`
- **Description:** Creates a new robot specification.
- **Request Body:**
  ```json
  {
    "name": "string",
    "specifications": {
      "weight": "number",
      "dimensions": {
        "length": "number",
        "width": "number",
        "height": "number"
      },
      "capabilities": ["string"]
    }
  }
  ```
- **Response:**
  - **201 Created**
    ```json
    {
      "id": "string",
      "message": "Robot created successfully."
    }
    ```

### 3. Get Simulation Data
- **Endpoint:** `/api/simulations`
- **Method:** `GET`
- **Description:** Retrieves the latest simulation data.
- **Response:**
  - **200 OK**
    ```json
    {
      "simulationData": {
        "timestamp": "string",
        "data": {
          "metric1": "number",
          "metric2": "number"
        }
      }
    }
    ```

### 4. Start a Simulation
- **Endpoint:** `/api/simulations/start`
- **Method:** `POST`
- **Description:** Starts a new simulation.
- **Request Body:**
  ```json
  {
    "parameters": {
      "param1": "value",
      "param2": "value"
    }
  }
  ```
- **Response:**
  - **202 Accepted**
    ```json
    {
      "message": "Simulation started successfully."
    }
    ```

## Error Handling
All API responses will include an appropriate HTTP status code and a message detailing the error if applicable.

### Example Error Response
- **400 Bad Request**
  ```json
  {
    "error": "Invalid input data."
  }
  ```

## Conclusion
This API documentation provides a comprehensive guide to the available endpoints in the Robotics Dashboard application. For further details, please refer to the source code or contact the development team.