# Deployment Guide for Sentiment Analysis Dashboard

This guide outlines the steps to deploy the Sentiment Analysis Dashboard application. You have two primary options: **Local Deployment** for quick setup and testing on your machine, and **Cloud Deployment** for making your application accessible via the web.

## Option 1: Local Deployment

Local deployment is suitable for development, testing, and personal use. The application will run on your local machine and be accessible via your web browser.

### Prerequisites

*   Python 3.8+ installed on your system.
*   `pip` (Python package installer).
*   Git (for cloning the repository).

### Steps for Local Deployment

1.  **Clone the Repository**:
    If you haven't already, clone the project repository from GitHub:
    ```bash
    git clone <your_github_repository_url>
    cd sentiment_dashboard
    ```
    *(Replace `<your_github_repository_url>` with the actual URL of your GitHub repository)*

2.  **Create a Virtual Environment** (Recommended):
    It's good practice to use a virtual environment to manage project dependencies. This prevents conflicts with other Python projects.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**:
    Install all required Python packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download NLTK Data** (Optional but Recommended):
    For full functionality, especially keyword extraction, download the necessary NLTK data:
    ```bash
    python -c "import nltk; nltk.download(\'stopwords\'); nltk.download(\'punkt\')"
    ```

5.  **Run the Streamlit Application**:
    Navigate to the project's root directory (if not already there) and run the application:
    ```bash
    streamlit run app.py
    ```
    The application will typically open in your default web browser at `http://localhost:8501`. If this port is in use, Streamlit will suggest an alternative.

## Option 2: Cloud Deployment (using Streamlit Community Cloud)

Deploying to Streamlit Community Cloud is a straightforward way to share your application with others via a public URL. This option requires your project to be hosted on a public GitHub repository.

### Prerequisites

*   A GitHub account with your project repository (public).
*   A Streamlit Community Cloud account (free to sign up).

### Steps for Cloud Deployment

1.  **Ensure Your Project is on GitHub**:
    Make sure your `app.py`, `requirements.txt`, and all other necessary files are pushed to a public GitHub repository. Refer to the "GitHub Repository Creation Guide" for instructions on setting this up.

2.  **Sign Up/Log In to Streamlit Community Cloud**:
    Go to [Streamlit Community Cloud](https://streamlit.io/cloud) and sign up or log in with your GitHub account.

3.  **Deploy a New App**:
    *   Once logged in, click on the `New app` button (usually located in the top right corner or central dashboard).
    *   You will be prompted to connect to your GitHub repository. Select the repository where your Sentiment Analysis Dashboard code resides.

4.  **Configure Deployment Settings**:
    *   **Repository**: Select your `sentiment-analysis-dashboard` repository.
    *   **Branch**: Choose the branch you want to deploy from (e.g., `main` or `master`).
    *   **Main file path**: This should be `app.py` (the default for Streamlit apps).
    *   **Python version**: Select a compatible Python version (e.g., `3.9`, `3.10`, or `3.11`).
    *   **Advanced settings** (Optional):
        *   **Secrets**: If your application uses API keys or other sensitive information, you can add them here as environment variables. For this application, it's unlikely to be needed unless you integrate external APIs beyond TextBlob/HuggingFace's local models.
        *   **Custom commands**: You might need to add a command to download NLTK data if you haven't included the `nltk_data` directory in your repository. Add `python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"` to the pre-install commands if needed.

5.  **Deploy the App**:
    Click the `Deploy!` button. Streamlit Cloud will then:
    *   Clone your repository.
    *   Create a virtual environment.
    *   Install dependencies from `requirements.txt`.
    *   Run your `app.py` file.

6.  **Access Your Deployed App**:
    Once deployed, Streamlit Cloud will provide you with a unique public URL for your application (e.g., `https://your-username.streamlit.app/`). You can share this URL with anyone.

### Maintaining Your Deployed App

*   **Automatic Updates**: By default, Streamlit Community Cloud automatically redeploys your app whenever you push changes to the selected branch of your GitHub repository.
*   **Monitoring**: The Streamlit Cloud dashboard provides logs and metrics to monitor your application's performance and troubleshoot issues.

## Choosing the Better Option

*   **Local Deployment**: Ideal for development, debugging, and private use. It gives you full control over the environment and is quicker to set up for personal testing.
*   **Cloud Deployment (Streamlit Community Cloud)**: The **better option** if you want to share your application with a wider audience, showcase it as a portfolio project, or run it continuously without keeping your local machine on. It handles hosting, scaling, and domain management, simplifying the process of making your app publicly available.

For showcasing your project, **Cloud Deployment** is highly recommended as it demonstrates a complete, accessible solution.
