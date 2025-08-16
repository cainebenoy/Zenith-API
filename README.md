# Zenith API

This is a simple and fast API built with **FastAPI** that provides a daily dose of inspiration. The **Zenith API** serves a new, random inspirational quote with its author on demand. It’s perfect for integrating into a variety of applications, such as a **New Tab** browser extension, a productivity dashboard, or a daily email newsletter. The project is designed to be lightweight and easy to deploy, demonstrating the power and simplicity of the **FastAPI** framework.

## Team members
1. [Caine Benoy](https://github.com/TH-Activities/saturday-hack-night-template)

## Link to product walkthrough
[link to video](Link Here)

## How it Works ?
1. The project uses a Python backend built with **FastAPI** and **Uvicorn**. It hosts a single **GET** endpoint, `/quote`.
2. When a user or application sends a request to this endpoint, the API randomly selects a quote from a pre-defined list and returns it in **JSON** format.
3. The returned **JSON** object contains both the quote text and its author.
4. The basic front-end is an HTML page that uses JavaScript's `fetch` API to call the backend and dynamically display the returned quote.

## Libraries used
* FastAPI - 0.111.0
* Uvicorn - 0.30.1

## How to configure
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Zenith-API.git](https://github.com/your-username/Zenith-API.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Zenith-API
    ```
3.  **Install the dependencies** listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run
1.  **Start the FastAPI server** from your terminal in the project directory:
    ```bash
    uvicorn main:app --reload
    ```
2.  The API will be accessible at `http://127.0.0.1:8000`. You can test the endpoint by navigating to `http://127.0.0.1:8000/quote` in your browser.
3.  To view the basic website, simply open the `index.html` file in your web browser. It will use JavaScript to fetch data from your locally running API.
