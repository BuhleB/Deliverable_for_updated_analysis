# Sentiment Analysis Dashboard: Comprehensive Documentation

This document provides in-depth documentation for the Sentiment Analysis Dashboard application, covering the rationale behind API selections, significant implementation challenges encountered, and a detailed user guide with practical examples.

## 1. API Selection Justification

The Sentiment Analysis Dashboard leverages two distinct sentiment analysis APIs: **TextBlob** and **Hugging Face (DistilBERT)**. This dual-API approach was chosen to offer users flexibility, cater to different performance requirements, and provide a comparative perspective on sentiment analysis methodologies.

### 1.1 TextBlob

**TextBlob** was selected primarily for its **simplicity, speed, and ease of integration**. As a rule-based sentiment analysis library, it is lightweight and does not require extensive computational resources or complex model loading. This makes it an excellent choice for:

*   **Quick, real-time analysis**: Ideal for single text inputs where immediate feedback is desired.
*   **Educational purposes**: Its rule-based nature makes it easier to understand the underlying mechanics of sentiment scoring, as it relies on lexical dictionaries and predefined rules.
*   **Baseline performance**: TextBlob provides a solid baseline for sentiment classification, often performing adequately for texts with clear positive or negative indicators.

However, it's important to note that TextBlob's rule-based approach can sometimes struggle with nuance, sarcasm, and context-dependent sentiment, which are inherent limitations of lexical-based methods.

### 1.2 Hugging Face (DistilBERT)

**Hugging Face's DistilBERT** model was integrated to provide a **more advanced, context-aware, and potentially more accurate** sentiment analysis option. DistilBERT, a distilled version of BERT, is a transformer-based model known for its:

*   **Superior accuracy**: Transformer models generally outperform rule-based systems on complex NLP tasks, including sentiment analysis, by understanding the contextual relationships between words.
*   **Handling nuance**: These models are better equipped to interpret sarcasm, irony, and subtle emotional cues in text.
*   **State-of-the-art capabilities**: Leveraging pre-trained models from the Hugging Face Transformers library allows access to cutting-edge NLP research and models trained on vast datasets.

The inclusion of DistilBERT aims to offer a more robust analysis for users dealing with diverse and complex textual data, where a deeper understanding of language is critical. While it requires more computational resources and a proper deep learning framework setup (e.g., PyTorch or TensorFlow), its potential for higher accuracy justifies its inclusion.

## 2. Implementation Challenges

Developing the Sentiment Analysis Dashboard involved several technical challenges, particularly in integrating diverse libraries and ensuring a smooth user experience within the Streamlit framework.

### 2.1 Streamlit Session State Management

**Challenge**: Streamlit applications re-run from top to bottom whenever an input widget changes. This behavior can lead to loss of data if not properly managed, especially for analysis results that should persist across user interactions.

**Solution**: The `st.session_state` object was extensively used to store persistent data, such as `analysis_results` (a Pandas DataFrame holding all analyzed texts and their sentiments). This ensured that once texts were analyzed, their results remained available for visualization, filtering, and export without re-running the analysis unnecessarily.

### 2.2 Integrating Multiple Sentiment Analyzers

**Challenge**: Seamlessly switching between TextBlob (a rule-based library) and Hugging Face (a transformer-based model requiring a deep learning backend) within the same application.

**Solution**: A `selected_analyzer` variable in `st.session_state` was used to dynamically choose which analysis function to call (`analyze_sentiment_textblob` or `analyze_sentiment_huggingface`). The `sentiment_analyzer.py` module was designed to encapsulate the logic for both, abstracting away their differences from the main `app.py` file. This modular design allowed for easy extension and maintenance.

### 2.3 Handling File Uploads and Batch Processing

**Challenge**: Processing various file formats (CSV, TXT) and handling large batches of text efficiently, while also allowing users to map columns from CSV files.

**Solution**: The `export_utils.py` module was created to centralize file processing logic. It includes a `batch_process_files` function that intelligently reads CSV files (expecting a `text` column and optionally `source` and `date`) and TXT files (line by line). This function prepares a standardized format for the `batch_analyze_sentiment` function, ensuring consistency across different input methods. Streamlit's `st.file_uploader` and `st.dataframe` were used to provide an intuitive interface for file handling and preview.

### 2.4 Dynamic Visualization and Export

**Challenge**: Generating a wide array of interactive visualizations and exporting results in multiple formats, including PDF reports with embedded charts.

**Solution**: The `visualizations.py` module was dedicated to creating Plotly and Matplotlib charts, making them reusable and maintainable. The `export_utils.py` module was extended to handle CSV, JSON, Excel, and PDF exports. For PDF reports, a mechanism was implemented to temporarily save Plotly figures as static images, which could then be embedded into the PDF using ReportLab. This required careful management of temporary files and image generation to ensure all visuals were correctly included.

### 2.5 NLTK Data Download

**Challenge**: NLTK (used for keyword extraction) requires specific data packages (e.g., `stopwords`, `punkt`) to be downloaded, which might not be present in all environments.

**Solution**: The `requirements.txt` includes `nltk`, and the installation instructions guide users to download the necessary data programmatically. Additionally, the `sentiment_analyzer.py` includes checks and fallback mechanisms to handle cases where NLTK data might be missing, providing informative error messages without crashing the application.

## 3. User Guide with Examples

This section provides a detailed guide on how to effectively use the Sentiment Analysis Dashboard, complete with practical examples for each feature.

### 3.1 Getting Started

1.  **Installation**: Follow the [Installation](#installation) steps in the `README.md` to set up the application locally.
2.  **Run the App**: Execute `streamlit run app.py` in your terminal.
3.  **Access**: Open your web browser and navigate to `http://localhost:8501` (or the port indicated by Streamlit).

### 3.2 Choosing an Analysis Mode

In the sidebar, select one of the three analysis modes:

*   **Single Text Analysis**: For analyzing individual pieces of text.
*   **Batch Text Analysis**: For analyzing multiple texts entered directly into a text area.
*   **File Upload Analysis**: For processing sentiment from CSV or TXT files.

Also, select your preferred **Sentiment Analyzer**: `TextBlob` or `HuggingFace`.

### 3.3 Single Text Analysis Example

This mode is perfect for quick checks or understanding the sentiment of a short phrase.

1.  **Select Mode**: Choose "Single Text Analysis" from the sidebar.
2.  **Enter Text**: In the text area, type: `"I absolutely love the new update! It's so intuitive and fast."`
3.  **Optional Inputs**: Add `Source: App Store Review` and select today's date.
4.  **Analyze**: Click the "🚀 Analyze Text" button.

**Expected Output**: The dashboard will display the sentiment (likely `Positive`), confidence, polarity, and subjectivity. An explanation of the sentiment will also be provided.

### 3.4 Batch Text Analysis Example

Use this mode to analyze several short texts without needing a file.

1.  **Select Mode**: Choose "Batch Text Analysis" from the sidebar.
2.  **Enter Texts**: In the text area, enter the following (one per line):
    ```
    The service was terrible, I'm very disappointed.
    The product is okay, but it could be better.
    Fantastic experience, highly recommend!
    ```
3.  **Optional Inputs**: Set `Default source for all texts: Customer Feedback`.
4.  **Analyze**: Click the "🚀 Analyze Batch" button.

**Expected Output**: The results will be added to the `Analysis Results` table, and visualizations will update to reflect the new data. You can then explore the sentiment distribution across these texts.

### 3.5 File Upload Analysis Example

This is ideal for analyzing larger datasets from external sources.

1.  **Select Mode**: Choose "File Upload Analysis" from the sidebar.
2.  **Upload File**: Click "Choose files" and upload the `sample_data.csv` file (or your own CSV/TXT file).
3.  **Preview**: The app will show a preview of the file.
4.  **Analyze**: Click the "🚀 Analyze All Files" button.

**Expected Output**: The application will process all texts from the file, update the `Analysis Results`, and populate the various visualization tabs.

### 3.6 Exploring Analysis Results

After performing an analysis, the "Analysis Results" section will appear below the input areas. It consists of several tabs:

*   **📊 Overview**: View pie charts of sentiment distribution, confidence histograms, and polarity vs. subjectivity scatter plots. If multiple sources are present, you can also see sentiment by source.
*   **📈 Trends**: If your data includes date information, this tab will display sentiment trends over time.
*   **🔍 Keywords**: Explore word clouds generated from your texts and a bar chart of the most frequent keywords.
*   **📋 Data**: See a detailed table of all analyzed texts, their sentiments, confidence scores, and explanations. You can also filter this data.
*   **🎯 Accuracy Report**: (See next section for details).

### 3.7 Generating an Accuracy Report

This feature allows you to evaluate the performance of the chosen sentiment analyzer against a manually labeled dataset.

1.  **Navigate**: Go to the "🎯 Accuracy Report" tab within the "Analysis Results" section.
2.  **Upload Labeled Data**: Click "Upload Labeled Data (CSV)" and upload a CSV file. This file **must** contain at least two columns: `text` (the content to analyze) and `true_sentiment` (the ground truth sentiment: `Positive`, `Negative`, or `Neutral`). You can use `sample_labeled_data.csv` as an example.
3.  **Generate Report**: After uploading, click the "Generate Accuracy Report" button.

**Expected Output**: The tab will display a classification report (precision, recall, f1-score), a confusion matrix, and the overall accuracy of the selected sentiment analyzer against your labeled data.

### 3.8 Exporting Results

From the "📋 Data" tab, you can export your analysis results for further use.

1.  **Select Format**: Choose your desired export format from the dropdown: `CSV`, `JSON`, `Excel`, or `PDF Report`.
2.  **Include Visuals (PDF only)**: If exporting to PDF, you can check "Include visualizations in PDF" to embed charts in your report.
3.  **Download**: Click the "📥 Download Data" button to save the file to your local machine.

This comprehensive documentation should provide a solid understanding of the Sentiment Analysis Dashboard's functionality and how to effectively utilize its features.
