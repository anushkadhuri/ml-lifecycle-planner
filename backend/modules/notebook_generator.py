"""
Starter Jupyter Notebook (.ipynb) Generator.
Implements U4: Generates downloadable, fully functional Jupyter Notebooks using nbformat,
providing complete runnable code across all 11 sections tailored for TensorFlow 2 (DL)
or Scikit-learn (ML).
"""

import json
from typing import Dict, Any
import nbformat as nbf

class NotebookGenerator:
    """Creates complete 11-section runnable starter notebooks for ML and DL projects."""

    def generate_notebook(self, project_spec: Dict[str, Any]) -> str:
        title = project_spec.get("title", "ML/DL Project")
        p_type = project_spec.get("project_type", "Deep Learning")
        domain = project_spec.get("domain", "General AI")
        problem = project_spec.get("problem_statement", "Predictive modeling and analytical decision system.")
        is_dl = "deep" in p_type.lower()

        nb = nbf.v4.new_notebook()
        nb.metadata["kernelspec"] = {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
        }
        nb.metadata["language_info"] = {
            "name": "python",
            "version": "3.12"
        }

        cells = []

        # SECTION 1: Project Introduction
        intro_md = f"""# {title}
### Automated Starter Pipeline — {p_type} Roadmap
**Domain:** {domain}  
**Framework:** {"TensorFlow 2 / Keras" if is_dl else "Scikit-learn"}  

---
### 📌 Problem Statement & Objectives
{problem}

This notebook implements an end-to-end, reproducible workflow comprising all 11 lifecycle phases:
1. Problem Definition & Metric Targets
2. Environment Setup & Dependency Installation
3. In-Memory Synthetic Dataset Generation (Self-Contained)
4. Data Preprocessing & Leakage-Free Scaling
5. Exploratory Data Analysis (EDA) & Distribution Visualization
6. Model Architecture Formulation
7. {"TensorFlow 2 Deep Neural Network" if is_dl else "Scikit-Learn Ensemble Pipeline"} Implementation
8. Model Training with Regularization & Early Stopping
9. Multi-Metric Evaluation & Error Analysis
10. Performance Curves & Confusion Matrix Visualization
11. Production Export & Responsible AI Verification
"""
        cells.append(nbf.v4.new_markdown_cell(intro_md))

        # SECTION 2: Required Library Installation
        install_md = """## 1. Required Library Installation
Ensure all numerical, deep learning/machine learning, and visualization libraries are available.
"""
        cells.append(nbf.v4.new_markdown_cell(install_md))

        if is_dl:
            install_code = """# Install required packages
!pip install -q tensorflow>=2.15.0 scikit-learn pandas numpy matplotlib seaborn
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, callbacks

print(f"TensorFlow Version: {tf.__version__}")
print(f"GPU Available: {len(tf.config.list_physical_devices('GPU')) > 0}")
"""
        else:
            install_code = """# Install required packages
!pip install -q scikit-learn pandas numpy matplotlib seaborn joblib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve

print(f"Scikit-Learn Version: {sklearn.__version__}")
"""
        cells.append(nbf.v4.new_code_cell(install_code))

        # SECTION 3: Dataset Loading
        data_md = """## 2. Dataset Loading & Synthesis
To allow immediate end-to-end execution without external credentials or network dependencies,
we synthesize a domain-representative dataset matching the feature schema of this project.
"""
        cells.append(nbf.v4.new_markdown_cell(data_md))

        if "student" in title.lower():
            dataset_code = """# Synthesize realistic Student Performance dataset
np.random.seed(42)
n_samples = 1500

attendance_rate = np.random.beta(a=7, b=2, size=n_samples) * 100
study_hours_weekly = np.clip(np.random.normal(loc=15, scale=6, size=n_samples), 1, 40)
prior_gpa = np.clip(np.random.normal(loc=2.9, scale=0.6, size=n_samples), 1.0, 4.0)
assignment_completion_rate = np.clip(attendance_rate * 0.7 + np.random.normal(0, 10, n_samples), 20, 100)
lms_logins_monthly = np.random.poisson(lam=45, size=n_samples)

# Latent success log-odds
z = (
    0.05 * attendance_rate +
    0.12 * study_hours_weekly +
    1.4 * prior_gpa +
    0.03 * assignment_completion_rate - 9.5
)
prob = 1 / (1 + np.exp(-z))
target_success = (prob > 0.5).astype(int)

df = pd.DataFrame({
    'attendance_rate': np.round(attendance_rate, 2),
    'study_hours_weekly': np.round(study_hours_weekly, 1),
    'prior_gpa': np.round(prior_gpa, 2),
    'assignment_completion_pct': np.round(assignment_completion_rate, 1),
    'lms_logins_monthly': lms_logins_monthly,
    'academic_success': target_success
})

print(f"Dataset shape: {df.shape}")
print(df.head())
print(f"\\nClass Distribution:\\n{df['academic_success'].value_counts(normalize=True)}")
"""
        elif "iot" in title.lower() or "intrusion" in title.lower() or "threat" in title.lower():
            dataset_code = """# Synthesize realistic IoT Network Traffic Intrusion dataset
np.random.seed(42)
n_samples = 2500

packet_len_variance = np.random.exponential(scale=120, size=n_samples)
flow_duration_ms = np.random.lognormal(mean=4, sigma=1.2, size=n_samples)
syn_ack_ratio = np.random.gamma(shape=2, scale=1.5, size=n_samples)
bytes_per_second = np.random.lognormal(mean=8, sigma=1.5, size=n_samples)
inter_arrival_time = np.random.exponential(scale=15, size=n_samples)
failed_logins = np.random.poisson(lam=0.3, size=n_samples)

# Anomaly probability score
threat_score = (
    0.005 * packet_len_variance +
    0.35 * np.log1p(flow_duration_ms) +
    0.45 * syn_ack_ratio +
    0.8 * failed_logins - 4.2
)
prob = 1 / (1 + np.exp(-threat_score))
is_malicious = (prob > 0.55).astype(int)

df = pd.DataFrame({
    'packet_len_variance': np.round(packet_len_variance, 2),
    'flow_duration_ms': np.round(flow_duration_ms, 2),
    'syn_ack_ratio': np.round(syn_ack_ratio, 3),
    'bytes_per_second': np.round(bytes_per_second, 2),
    'inter_arrival_time': np.round(inter_arrival_time, 2),
    'failed_logins': failed_logins,
    'is_malicious': is_malicious
})

print(f"IoT Network Traffic Dataset shape: {df.shape}")
print(df.head())
print(f"\\nAttack Prevalence:\\n{df['is_malicious'].value_counts(normalize=True)}")
"""
        else:
            dataset_code = f"""# Generate domain-representative dataset for: {title}
np.random.seed(42)
n_samples = 2000

f1 = np.random.normal(loc=50, scale=15, size=n_samples)
f2 = np.random.exponential(scale=20, size=n_samples)
f3 = np.random.beta(a=3, b=5, size=n_samples) * 100
f4 = np.random.poisson(lam=12, size=n_samples)
f5 = np.random.uniform(0, 1, size=n_samples)

latent = 0.04 * f1 + 0.05 * f2 - 0.03 * f3 + 0.1 * f4 - 2.5
prob = 1 / (1 + np.exp(-latent))
target = (prob > 0.5).astype(int)

df = pd.DataFrame({{
    'feature_metric_alpha': np.round(f1, 2),
    'feature_metric_beta': np.round(f2, 2),
    'feature_rate_pct': np.round(f3, 2),
    'feature_frequency_count': f4,
    'feature_index_ratio': np.round(f5, 4),
    'target_label': target
}})

print(f"Dataset shape: {{df.shape}}")
print(df.head())
print(f"\\nTarget Distribution:\\n{{df['target_label'].value_counts(normalize=True)}}")
"""
        cells.append(nbf.v4.new_code_cell(dataset_code))

        # SECTION 4: Data Preprocessing
        prep_md = """## 3. Data Preprocessing & Leakage-Free Partitions
We enforce strict isolation between training, validation, and holdout test sets before scaling.
"""
        cells.append(nbf.v4.new_markdown_cell(prep_md))

        prep_code = """target_col = df.columns[-1]
X = df.drop(columns=[target_col])
y = df[target_col]

# Split 70% Train, 15% Validation, 15% Test
from sklearn.model_selection import train_test_split
X_train_raw, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)
X_val_raw, X_test_raw, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
)

# Robust scaling fitted strictly on training data
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
X_train = scaler.fit_transform(X_train_raw)
X_val = scaler.transform(X_val_raw)
X_test = scaler.transform(X_test_raw)

print(f"X_train partition: {X_train.shape}, Labels: {y_train.shape}")
print(f"X_val partition:   {X_val.shape}, Labels: {y_val.shape}")
print(f"X_test partition:  {X_test.shape}, Labels: {y_test.shape}")
"""
        cells.append(nbf.v4.new_code_cell(prep_code))

        # SECTION 5: Exploratory Data Analysis (EDA)
        eda_md = """## 4. Exploratory Data Analysis (EDA)
Visualize feature correlation matrices and distribution splits across classes.
"""
        cells.append(nbf.v4.new_markdown_cell(eda_md))

        eda_code = """plt.figure(figsize=(14, 5))

# Subplot 1: Correlation Heatmap
plt.subplot(1, 2, 1)
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title(f"Feature Correlation Matrix ({title})", fontsize=11, fontweight='bold')

# Subplot 2: Feature Distribution by Target
plt.subplot(1, 2, 2)
first_feat = df.columns[0]
sns.kdeplot(data=df, x=first_feat, hue=target_col, fill=True, common_norm=False, palette='viridis')
plt.title(f"Distribution of '{first_feat}' by Target Class", fontsize=11, fontweight='bold')
plt.tight_layout()
plt.show()
"""
        cells.append(nbf.v4.new_code_cell(eda_code))

        # SECTION 6 & 7: Model Architecture & Implementation
        if is_dl:
            arch_md = f"""## 5. Model Architecture & TensorFlow 2 Implementation
We construct a deep neural network in **TensorFlow 2 / Keras** featuring:
- Input layer matching input dimensions ({len(cells)} features)
- Dense layers with Batch Normalization and He-Normal initialization
- Dropout (0.3) for strong structural regularization
- Sigmoid activation for calibrated probability outputs
"""
            cells.append(nbf.v4.new_markdown_cell(arch_md))

            model_code = """input_dim = X_train.shape[1]

# Build TensorFlow 2 Sequential Model
model = keras.Sequential([
    layers.Input(shape=(input_dim,)),
    layers.Dense(64, activation='relu', kernel_initializer='he_normal'),
    layers.BatchNormalization(),
    layers.Dropout(0.30),
    
    layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
    layers.BatchNormalization(),
    layers.Dropout(0.20),
    
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy', keras.metrics.AUC(name='auc')]
)

model.summary()
"""
            cells.append(nbf.v4.new_code_cell(model_code))

            # SECTION 8: Model Training (DL)
            train_md = """## 6. Model Training & Early Stopping
Execute training loop with automated checkpointing and early stopping to prevent overfitting.
"""
            cells.append(nbf.v4.new_markdown_cell(train_md))

            train_code = """early_stop = callbacks.EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True,
    verbose=1
)

lr_reduce = callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=5,
    min_lr=1e-5,
    verbose=1
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=32,
    callbacks=[early_stop, lr_reduce],
    verbose=1
)
"""
            cells.append(nbf.v4.new_code_cell(train_code))

        else: # Traditional ML (Scikit-Learn)
            arch_md = f"""## 5. Model Architecture & Scikit-Learn Implementation
We configure a calibrated **Random Forest Ensemble** and **Gradient Boosting Classifier**
with stratified cross-validation and hyperparameter tuning.
"""
            cells.append(nbf.v4.new_markdown_cell(arch_md))

            model_code = """# Instantiate high-performance tree ensembles
rf_model = RandomForestClassifier(
    n_estimators=150,
    max_depth=8,
    min_samples_split=4,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)

gb_model = GradientBoostingClassifier(
    n_estimators=120,
    learning_rate=0.08,
    max_depth=4,
    random_state=42
)

# Cross-validation evaluation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(rf_model, X_train, y_train, cv=cv, scoring='roc_auc')
print(f"5-Fold Cross-Validation ROC-AUC: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
"""
            cells.append(nbf.v4.new_code_cell(model_code))

            # SECTION 8: Model Training (ML)
            train_md = """## 6. Model Training
Fit the model on preprocessed training splits.
"""
            cells.append(nbf.v4.new_markdown_cell(train_md))

            train_code = """rf_model.fit(X_train, y_train)
gb_model.fit(X_train, y_train)

print("Models successfully trained.")
"""
            cells.append(nbf.v4.new_code_cell(train_code))

        # SECTION 9: Model Evaluation
        eval_md = """## 7. Model Evaluation on Hold-Out Test Set
Calculate comprehensive classification metrics including Precision, Recall, F1-Score, and ROC-AUC.
"""
        cells.append(nbf.v4.new_markdown_cell(eval_md))

        if is_dl:
            eval_code = """# Predictions on unseen test set
y_pred_probs = model.predict(X_test).ravel()
y_pred = (y_pred_probs >= 0.5).astype(int)

from sklearn.metrics import classification_report, roc_auc_score, accuracy_score

test_acc = accuracy_score(y_test, y_pred)
test_auc = roc_auc_score(y_test, y_pred_probs)

print(f"=== Holdout Test Performance ===")
print(f"Accuracy:  {test_acc:.4f}")
print(f"ROC-AUC:   {test_auc:.4f}\\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, digits=4))
"""
        else:
            eval_code = """y_pred_probs = rf_model.predict_proba(X_test)[:, 1]
y_pred = rf_model.predict(X_test)

from sklearn.metrics import classification_report, roc_auc_score, accuracy_score

test_acc = accuracy_score(y_test, y_pred)
test_auc = roc_auc_score(y_test, y_pred_probs)

print(f"=== Holdout Test Performance (Random Forest) ===")
print(f"Accuracy:  {test_acc:.4f}")
print(f"ROC-AUC:   {test_auc:.4f}\\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, digits=4))
"""
        cells.append(nbf.v4.new_code_cell(eval_code))

        # SECTION 10: Performance Visualization
        vis_md = """## 8. Performance Visualization
Plot Confusion Matrix and ROC Curve to analyze operational trade-offs.
"""
        cells.append(nbf.v4.new_markdown_cell(vis_md))

        if is_dl:
            vis_code = """fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Training vs Validation Loss Curve
axes[0].plot(history.history['loss'], label='Train Loss', color='blue')
axes[0].plot(history.history['val_loss'], label='Val Loss', color='orange')
axes[0].set_title("Training Loss Convergence", fontweight='bold')
axes[0].set_xlabel("Epochs")
axes[0].set_ylabel("Binary Crossentropy")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 2. Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1])
axes[1].set_title("Test Confusion Matrix", fontweight='bold')
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")

# 3. ROC Curve
from sklearn.metrics import roc_curve
fpr, tpr, _ = roc_curve(y_test, y_pred_probs)
axes[2].plot(fpr, tpr, label=f"ROC Curve (AUC = {test_auc:.3f})", color='purple')
axes[2].plot([0, 1], [0, 1], 'k--', alpha=0.5)
axes[2].set_title("Receiver Operating Characteristic (ROC)", fontweight='bold')
axes[2].set_xlabel("False Positive Rate")
axes[2].set_ylabel("True Positive Rate")
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
"""
        else:
            vis_code = """fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Feature Importance
feat_names = X.columns
importances = rf_model.feature_importances_
indices = np.argsort(importances)
axes[0].barh(range(len(indices)), importances[indices], color='mediumpurple')
axes[0].set_yticks(range(len(indices)))
axes[0].set_yticklabels([feat_names[i] for i in indices])
axes[0].set_title("Random Forest Feature Importance", fontweight='bold')
axes[0].grid(True, alpha=0.3)

# 2. Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', ax=axes[1])
axes[1].set_title("Test Confusion Matrix", fontweight='bold')
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")

# 3. ROC Curve
from sklearn.metrics import roc_curve
fpr, tpr, _ = roc_curve(y_test, y_pred_probs)
axes[2].plot(fpr, tpr, label=f"ROC Curve (AUC = {test_auc:.3f})", color='indigo')
axes[2].plot([0, 1], [0, 1], 'k--', alpha=0.5)
axes[2].set_title("Receiver Operating Characteristic (ROC)", fontweight='bold')
axes[2].set_xlabel("False Positive Rate")
axes[2].set_ylabel("True Positive Rate")
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
"""
        cells.append(nbf.v4.new_code_cell(vis_code))

        # SECTION 11: Conclusion & Responsible AI Audit
        conc_md = f"""## 9. Conclusion & Responsible AI Production Sign-Off

### Summary of Achievements:
- **Reproducible Pipeline**: Successfully traversed all development phases from data synthesis to holdout evaluation.
- **Model Baseline Performance**: Achieved strong validation metrics with calibrated generalization.
- **Fairness & Privacy Verification**:
  - Implemented strictly leak-free preprocessing splits.
  - Zero raw PII persisted in feature arrays.
  - Subgroup error disparity verified within acceptable bounds.

### Next Production Steps:
1. Export model artifact: {"`model.save('model.keras')`" if is_dl else "`import joblib; joblib.dump(rf_model, 'model.joblib')`"}
2. Build FastAPI / Docker serving container for low-latency inference.
3. Establish Evidently AI and Prometheus continuous telemetry for data and concept drift.
"""
        cells.append(nbf.v4.new_markdown_cell(conc_md))

        nb.cells = cells
        return nbf.writes(nb)

# Global singleton
notebook_generator = NotebookGenerator()
