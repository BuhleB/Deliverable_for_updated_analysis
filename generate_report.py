import pandas as pd
from sentiment_analyzer import generate_accuracy_report

# Load the labeled data
df_labeled = pd.read_csv("accuracy_report_data.csv")

# Generate accuracy report for TextBlob
report_data_textblob, error_textblob = generate_accuracy_report(df_labeled, analyzer_type='TextBlob')

# Generate accuracy report for HuggingFace
report_data_huggingface, error_huggingface = generate_accuracy_report(df_labeled, analyzer_type='HuggingFace')

# Save the reports to a file
with open("accuracy_report_output.txt", "w") as f:
    f.write("--- TextBlob Accuracy Report ---\n")
    if error_textblob:
        f.write(f"Error: {error_textblob}\n")
    else:
        f.write("Classification Report:\n")
        f.write(str(pd.DataFrame(report_data_textblob["classification_report"]).transpose()))
        f.write("\n\nConfusion Matrix:\n")
        f.write(str(pd.DataFrame(report_data_textblob["confusion_matrix"], index=[f'True {label}' for label in report_data_textblob["labels"]], columns=[f'Predicted {label}' for label in report_data_textblob["labels"]])))
        f.write(f"\n\nOverall Accuracy: {report_data_textblob['accuracy']:.2f}\n")

    f.write("\n--- HuggingFace Accuracy Report ---\n")
    if error_huggingface:
        f.write(f"Error: {error_huggingface}\n")
    else:
        f.write("Classification Report:\n")
        f.write(str(pd.DataFrame(report_data_huggingface["classification_report"]).transpose()))
        f.write("\n\nConfusion Matrix:\n")
        f.write(str(pd.DataFrame(report_data_huggingface["confusion_matrix"], index=[f'True {label}' for label in report_data_huggingface["labels"]], columns=[f'Predicted {label}' for label in report_data_huggingface["labels"]])))
        f.write(f"\n\nOverall Accuracy: {report_data_huggingface['accuracy']:.2f}\n")

print("Accuracy reports generated and saved to accuracy_report_output.txt")

