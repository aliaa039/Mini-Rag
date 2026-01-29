# Mini-RAG 🤖

**Mini-RAG** is a lightweight, minimal implementation of the **Retrieval-Augmented Generation (RAG)** architecture for Question Answering tasks. Built with **FastAPI** and **Python**, this project serves as a streamlined boilerplate or educational reference for integrating LLMs with external knowledge bases.

## 🚀 Features

* **Minimalist Core:** Strip-down implementation focusing on the essentials of RAG.
* **FastAPI Powered:** High-performance, asynchronous web framework.
* **Easy Configuration:** Environment-based setup using `.env` files.
* **Ready for Testing:** Includes a Postman collection for immediate API interaction.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**
* **Conda** (MiniConda or Anaconda)

## 🛠️ Installation & Setup

Follow these steps to set up the development environment.

### 1. Configure the Environment

We recommend using **MiniConda** to manage dependencies.

**Step 1:** Download and install MiniConda from the [official documentation](https://docs.anaconda.com/free/miniconda/#quick-command-line-install).

**Step 2:** Create a clean virtual environment:

```bash
conda create -n mini-rag python=3.8

```

**Step 3:** Activate the environment:

```bash
conda activate mini-rag

```

### 2. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt

```

### 3. Environment Variables

Configure your secrets and API keys.

1. Copy the example environment file:
```bash
cp .env.example .env

```


2. Open the `.env` file in your text editor and populate the variables (e.g., your `OPENAI_API_KEY`).

---

## ⚡ Usage

### Running the Server

Start the FastAPI application using Uvicorn. The server will run on port **5000**.

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000

```

* `--reload`: Enables auto-reload for development (server restarts on code changes).
* `--host 0.0.0.0`: Makes the server accessible externally.

### API Documentation

Once the server is running, you can access the automatic interactive API documentation provided by FastAPI:

* **Swagger UI:** `http://localhost:5000/docs`
* **ReDoc:** `http://localhost:5000/redoc`

---

## 🧪 Testing with Postman

We have included a Postman collection to help you test the endpoints quickly.

1. **Download:** [Click here to download the Postman Collection](https://www.google.com/search?q=/assets/mini-rag-app.postman_collection.json).
2. **Import:** Open Postman -> `File` -> `Import` -> Select the downloaded JSON file.
3. **Run:** Execute the requests against your local server.