# Shop Microservices

A basic implementation of microservices for a shop application.

## Services

*   **User Service:**  Manages user registration and login.
*   **Order Service:** Handles order creation, interacting with the User Service for authentication.

## Usage

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Gautam0610/Shop-Microservices.git
    ```

2.  **Navigate to each service directory:**

    ```bash
    cd User_Service
    ```

    and

    ```bash
    cd Order_Service
    ```

3.  **Build and run the Docker containers (example):**

    ```bash
    docker build -t user-service .
    docker run -p 5000:5000 user-service
    ```

    and

    ```bash
    docker build -t order-service .
    docker run -p 5001:5001 order-service
    ```


## Endpoints

### User Service

*   `/register`:  POST - Registers a new user.  Expects JSON with `username` and `password`.
*   `/login`:  POST - Logs in an existing user.  Expects JSON with `username` and `password`.

### Order Service

*   `/create_order`:  POST - Creates an order for a user.  Expects JSON with `username` (and optionally `password` for authentication against the User Service).
