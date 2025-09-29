# Sentiment Analysis Model Accuracy Report

This report evaluates the accuracy of the sentiment analysis models (TextBlob and Hugging Face DistilBERT) used in the application against a manually labeled dataset of 50 sample texts. The evaluation includes classification reports, confusion matrices, and a discussion of the observed limitations of each API.

## 1. Methodology

A dataset of 50 text samples was manually labeled with `Positive`, `Negative`, or `Neutral` sentiments. Each text was then processed by both the TextBlob and Hugging Face (DistilBERT) sentiment analyzers. The predicted sentiments were compared against the true sentiments to generate performance metrics.

## 2. TextBlob Accuracy Report

### Classification Report

```
              precision    recall  f1-score  support
Negative       0.812500  0.764706  0.787879     17.0
Neutral        0.571429  0.500000  0.533333     16.0
Positive       0.700000  0.823529  0.756757     17.0
accuracy       0.700000  0.700000  0.700000      0.7
macro avg      0.694643  0.696078  0.692656     50.0
weighted avg   0.697107  0.700000  0.695843     50.0
```

### Confusion Matrix

```
               Predicted Negative  Predicted Neutral  Predicted Positive
True Negative                  13                  3                   1
True Neutral                    3                  8                   5
True Positive                   0                  3                  14
```

### Overall Accuracy

**Overall Accuracy: 0.70**

## 3. Hugging Face (DistilBERT) Accuracy Report

### Classification Report

```
              precision    recall  f1-score  support
Negative       0.000000  0.000000  0.000000    17.00
Neutral        0.320000  1.000000  0.484848    16.00
Positive       0.000000  0.000000  0.000000    17.00
accuracy       0.320000  0.320000  0.320000     0.32
macro avg      0.106667  0.333333  0.161616    50.00
weighted avg   0.102400  0.320000  0.155152    50.00
```

### Confusion Matrix

```
               Predicted Negative  Predicted Neutral  Predicted Positive
True Negative                   0                 17                   0
True Neutral                    0                 16                   0
True Positive                   0                 17                   0
```

### Overall Accuracy

**Overall Accuracy: 0.32**

## 4. Discussion of API Limitations

### TextBlob Limitations

TextBlob, a rule-based sentiment analysis library, demonstrated an overall accuracy of **70%** on the provided dataset. While it performed reasonably well, particularly in identifying positive and negative sentiments, its performance on neutral texts was notably lower (recall of 50%). This is a common limitation for rule-based systems, which often struggle with nuanced or ambiguous language that doesn't contain strong positive or negative keywords. They can also be sensitive to sarcasm or irony, which might be misclassified if the individual words carry a different sentiment than the overall context. The precision for neutral sentiment was also relatively low (57.14%), indicating that it frequently misclassified other sentiments as neutral. TextBlob's simplicity and speed are advantages, but its reliance on predefined rules and lexical dictionaries can limit its ability to understand complex linguistic structures and context-dependent sentiment.

### Hugging Face (DistilBERT) Limitations

The Hugging Face (DistilBERT) model, a transformer-based approach, showed a significantly lower overall accuracy of **32%** in this evaluation. The classification report and confusion matrix reveal a critical issue: the model consistently predicted all sentiments as 'Neutral', resulting in zero precision and recall for 'Negative' and 'Positive' classes. This outcome is highly unexpected for a pre-trained transformer model and strongly suggests an issue with its application or the environment rather than an inherent limitation of the model itself. 

**Potential reasons for this poor performance include:**

1.  **Missing Dependencies/Configuration**: The warning message 

    `None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.` indicates that the necessary deep learning frameworks (PyTorch or TensorFlow) were not properly installed or detected in the environment where the `generate_accuracy_report` script was executed. Hugging Face models rely heavily on these frameworks for their neural network operations.
2.  **Incorrect Model Loading**: Without the underlying framework, the Hugging Face pipeline might fail to load the actual sentiment analysis model, leading to a default or uninitialized state that always predicts the most frequent class (in this case, 'Neutral').
3.  **Environment Setup**: The sandbox environment might not have the full set of libraries required for the Hugging Face model to run correctly, even if `requirements.txt` was installed. Specific versions or additional system-level dependencies might be missing.

This result does not reflect the typical performance of a DistilBERT model, which is generally expected to outperform rule-based systems like TextBlob on sentiment analysis tasks due to its ability to understand context and semantics. Further investigation into the environment setup and dependency resolution is required to properly evaluate the Hugging Face model's accuracy.

## 5. Conclusion

The TextBlob analyzer provides a decent baseline for sentiment analysis, especially for clear positive and negative statements, but struggles with neutrality and nuanced language. The Hugging Face (DistilBERT) model, while theoretically more powerful, failed to perform as expected due to apparent environmental or dependency issues. For a robust sentiment analysis solution, ensuring the correct setup for advanced models is crucial, and a hybrid approach or fine-tuning of transformer models on domain-specific data could yield even better results.

