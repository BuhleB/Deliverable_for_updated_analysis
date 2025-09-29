# GitHub Repository Creation Guide

This guide provides detailed instructions on how to set up a GitHub repository for the Sentiment Analysis Dashboard application, including which files to include and the steps for initialization, committing, and pushing to GitHub.

## 1. Files to Include in the Repository

Ensure the following files and directories are included in your GitHub repository to make the project complete and runnable:

*   `app.py`: The main Streamlit application file.
*   `sentiment_analyzer.py`: Contains the core sentiment analysis logic.
*   `visualizations.py`: Handles the generation of various charts and graphs.
*   `export_utils.py`: Provides utility functions for data export.
*   `requirements.txt`: Lists all Python dependencies required to run the application.
*   `sample_data.csv`: Sample unstructured data for testing analysis features.
*   `sample_labeled_data.csv`: Sample labeled data for testing the accuracy report feature.
*   `README.md`: A comprehensive overview of the project, its features, installation, and usage (content provided below).
*   `nltk_data/` (Optional): If you manually downloaded NLTK data, include this directory. Otherwise, the application will attempt to download it on first run.

## 2. Initializing and Pushing to GitHub

Follow these steps to create a new GitHub repository and push your project files:

### Step 1: Create a New GitHub Repository

1.  Go to [GitHub](https://github.com/) and log in to your account.
2.  Click the `+` sign in the top right corner and select `New repository`.
3.  Give your repository a meaningful name (e.g., `sentiment-analysis-dashboard`).
4.  Add a brief description.
5.  Choose whether the repository should be `Public` or `Private`.
6.  **Do NOT** initialize the repository with a README, .gitignore, or license at this stage, as you will be adding your own files.
7.  Click `Create repository`.

### Step 2: Initialize Local Git Repository

Open your terminal or command prompt, navigate to your project's root directory (where `app.py`, `requirements.txt`, etc., are located), and initialize a Git repository:

```bash
cd /path/to/your/sentiment_dashboard
git init
```

### Step 3: Add Files to the Repository

Add all the necessary project files to your local Git repository. It's good practice to add them all at once:

```bash
git add .
```

This command stages all changes in the current directory for the next commit.

### Step 4: Commit the Files

Commit the staged files with a descriptive message:

```bash
git commit -m "Initial commit of the Sentiment Analysis Dashboard application"
```

### Step 5: Link to GitHub and Push

Connect your local repository to the remote GitHub repository you created and push your local commits:

```bash
git branch -M main
git remote add origin <your_github_repository_url>
git push -u origin main
```

*(Replace `<your_github_repository_url>` with the URL provided by GitHub after creating your repository, e.g., `https://github.com/your-username/sentiment-analysis-dashboard.git`)*

Your project files will now be uploaded to your GitHub repository.

## 3. `README.md` Content

The `README.md` file is crucial for any GitHub repository as it provides an overview of your project. Below is the content you should use for your `README.md`:

```markdown
# Sentiment Analysis Dashboard

An interactive web application for analyzing sentiment in text data with comprehensive visualization and export capabilities.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Technical Details](#technical-details)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Features

### Core Sentiment Analysis
- **Multi-class Classification**: Automatically classifies text as Positive, Negative, or Neutral
- **Dual Analyzer Support**: Choose between TextBlob and Hugging Face (DistilBERT) models
- **Confidence Scoring**: Provides confidence scores for each classification
- **Keyword Extraction**: Identifies key words that drive sentiment
- **Batch Processing**: Analyze multiple texts simultaneously
- **Explanation Features**: Detailed explanations for why text received specific sentiment scores

### Interactive Dashboard
- **Real-time Analysis**: Instant sentiment analysis as you type
- **Multiple Input Methods**: 
  - Single text input
  - Batch text analysis
  - File upload (CSV and TXT files)
- **Advanced Filtering**: Filter results by sentiment, source, and other criteria
- **Accuracy Report**: Evaluate model performance with labeled datasets.

### Comprehensive Visualizations
- **Sentiment Distribution**: Pie charts showing overall sentiment breakdown
- **Confidence Analysis**: Histograms of confidence score distributions
- **Keyword Analysis**: Word clouds and frequency charts
- **Polarity vs Subjectivity**: Scatter plots for detailed analysis
- **Trend Analysis**: Time-based sentiment trends
- **Source Comparison**: Compare sentiment across different data sources

### Export Capabilities
- **Multiple Formats**: Export results in CSV, JSON, Excel, and PDF formats
- **Comprehensive Reports**: PDF reports with executive summaries and detailed analysis
- **Visual Exports**: Option to include charts and graphs in PDF reports
- **Data Preservation**: All analysis results can be saved for future reference

## Installation

To set up the Sentiment Analysis Dashboard locally, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd sentiment_dashboard
    ```
    *(Replace `<repository_url>` with the actual URL of your GitHub repository)*

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download NLTK data** (optional, but recommended for full functionality):
    ```bash
    python -c "import nltk; nltk.download(\'stopwords\'); nltk.download(\'punkt\')"
    ```
    *Note: The application includes fallback mechanisms if NLTK data is not available, but downloading it ensures optimal keyword extraction.*

## Usage

### Running the Application

After installation, run the Streamlit application from your terminal:

```bash
streamlit run app.py
```

The application will typically open in your web browser at `http://localhost:8501`.

### Input Methods

The dashboard provides several ways to input text for analysis:

#### Single Text Analysis
1.  Select "Single Text Analysis" from the sidebar.
2.  Enter your text in the provided text area.
3.  Optionally specify a source and date for the text.
4.  Click "Analyze Text" to get instant sentiment results.

#### Batch Text Analysis
1.  Select "Batch Text Analysis" from the sidebar.
2.  Enter multiple texts, with each text on a new line.
3.  Specify a default source and date for the batch (optional).
4.  Click "Analyze Batch" to process all texts.

#### File Upload Analysis
1.  Select "File Upload Analysis" from the sidebar.
2.  Upload CSV or TXT files. 
    -   For CSV files, ensure there is a column named `text`. Optional columns `source` and `date` will also be used if present.
    -   TXT files will be processed line by line.
3.  Click "Analyze All Files" to process the uploaded data.

### Viewing Results

Results are displayed in various tabs within the main content area:

-   **📊 Overview**: Provides sentiment distribution, confidence analysis, and polarity vs. subjectivity plots.
-   **📈 Trends**: Shows time-based sentiment analysis if date information is available.
-   **🔍 Keywords**: Displays word clouds and frequency charts of extracted keywords.
-   **📋 Data**: Presents a detailed table of all analyzed texts with their sentiment, confidence, polarity, and source. Includes options to view explanations for each analysis.
-   **🎯 Accuracy Report**: Allows you to upload labeled data (CSV with `text` and `true_sentiment` columns) to generate a classification report, confusion matrix, and overall accuracy metrics for the chosen sentiment analyzer.

### Exporting Results

From the "Data" tab, you can export your analysis results:

1.  Choose your preferred export format (CSV, JSON, Excel, or PDF Report).
2.  For PDF Reports, you can opt to include visualizations.
3.  Click "Download Data" to save the report.

## File Structure

```
sentiment_dashboard/
├── app.py                 # Main Streamlit application, handles UI and orchestrates analysis
├── sentiment_analyzer.py  # Contains core sentiment analysis functions (TextBlob, Hugging Face, keyword extraction, accuracy report generation)
├── visualizations.py      # Functions for generating various charts and graphs
├── export_utils.py        # Utility functions for exporting data to different formats (CSV, JSON, Excel, PDF)
├── requirements.txt       # Lists all Python dependencies
├── sample_data.csv        # Sample unstructured data for testing analysis features
├── sample_labeled_data.csv# Sample labeled data for testing the accuracy report feature
├── nltk_data/            # (Optional) Directory for NLTK data, if downloaded manually
└── README.md             # This comprehensive guide to the project
```

## Technical Details

### Sentiment Analysis Engine
-   **Primary Libraries**: TextBlob for rule-based sentiment analysis and Hugging Face (DistilBERT) for transformer-based sentiment analysis.
-   **Keyword Extraction**: Utilizes NLTK with stop-word filtering to identify significant terms.
-   **Fallback Support**: Built-in fallbacks ensure basic functionality even if external NLTK data is not fully downloaded.

### Visualization Libraries
-   **Plotly**: Used for creating interactive and detailed charts such as sentiment distributions, trends, and scatter plots.
-   **Matplotlib**: Employed specifically for generating word clouds.
-   **Streamlit**: Provides the web interface and handles the interactive dashboard components.

### Export Libraries
-   **Pandas**: Essential for data manipulation and seamless export to CSV and Excel formats.
-   **ReportLab**: Powers the generation of comprehensive PDF reports, including the integration of visualizations.
-   **OpenPyXL**: Used for handling Excel file operations.

## Customization

-   **Adding New Sentiment Models**: Modify `sentiment_analyzer.py` to integrate additional sentiment analysis libraries or custom-trained models.
-   **Custom Visualizations**: Add new chart types or modify existing ones in `visualizations.py` and integrate them into the dashboard tabs in `app.py`.
-   **Export Formats**: Extend `export_utils.py` to support additional export formats or customize the content and layout of existing reports.

## Troubleshooting

-   **NLTK Data Issues**: If you encounter errors related to NLTK data, ensure it\'s downloaded as per the installation instructions. The application includes fallback mechanisms, but full functionality requires the data.
-   **Memory Issues with Large Files**: For very large datasets, consider processing files in smaller batches or increasing the system memory available to the application.
-   **Port Conflicts**: If the default port `8501` is in use, you can specify a different port when running the application:
    ```bash
    streamlit run app.py --server.port 8502
    ```

## License

This project is open source and available under the MIT License.
```
