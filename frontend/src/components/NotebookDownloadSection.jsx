import React, { useState } from 'react'
import { FileCode2, Download, CheckCircle2, Terminal, Code2, Sparkles } from 'lucide-react'

export default function NotebookDownloadSection({ projectSpec, onDownloadNotebook }) {
  const [downloading, setDownloading] = useState(false)

  if (!projectSpec) return null

  const isDL = (projectSpec.project_type || '').toLowerCase().includes('deep')
  const framework = isDL ? 'TensorFlow 2 / Keras' : 'Scikit-Learn'

  const sections = [
    "1. Project Introduction & Problem Definition",
    "2. Required Library Installation (!pip install)",
    "3. In-Memory Synthetic Dataset Loading",
    "4. Data Preprocessing & Leakage-Free Scaling",
    "5. Exploratory Data Analysis (EDA Heatmaps & KDE)",
    "6. Model Architecture Specification",
    `7. ${isDL ? 'TensorFlow 2 Sequential Model Implementation' : 'Scikit-Learn Random Forest Pipeline'}`,
    "8. Model Training & Early Stopping Callbacks",
    "9. Multi-Metric Evaluation & Classification Report",
    "10. Performance Curves & Confusion Matrix Plots",
    "11. Production Export & Responsible AI Verification"
  ]

  const handleDownload = async () => {
    setDownloading(true)
    try {
      await onDownloadNotebook()
    } finally {
      setDownloading(false)
    }
  }

  return (
    <div className="glass-panel rounded-2xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-5 border-b border-slate-800 gap-4">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-cyan-600/20 border border-cyan-500/30 flex items-center justify-center text-cyan-400">
            <FileCode2 className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h3 className="text-lg font-bold text-white">Starter Jupyter Notebook (.ipynb)</h3>
              <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">
                U4 Automated Code Generator
              </span>
            </div>
            <p className="text-xs text-slate-400">
              Runnable, self-contained starter notebook with synthetic domain data and complete 11-section pipeline.
            </p>
          </div>
        </div>

        {/* Download Button */}
        <button
          onClick={handleDownload}
          disabled={downloading}
          className="px-6 py-3 rounded-xl bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white font-bold text-xs tracking-wider transition-all shadow-glow-cyan flex items-center justify-center space-x-2 active:scale-95 disabled:opacity-50"
        >
          {downloading ? (
            <>
              <svg className="animate-spin h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>Generating .ipynb...</span>
            </>
          ) : (
            <>
              <Download className="w-4 h-4" />
              <span>Download Starter Notebook (.ipynb)</span>
            </>
          )}
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
        {/* Sections Checklist */}
        <div>
          <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-300 mb-3 flex items-center space-x-1.5">
            <CheckCircle2 className="w-4 h-4 text-cyan-400" />
            <span>11 Embedded Notebook Sections:</span>
          </h4>
          <div className="space-y-1.5">
            {sections.map((sec, idx) => (
              <div
                key={idx}
                className="flex items-center space-x-2.5 p-2 rounded-lg bg-slate-900/60 border border-slate-800/80 text-xs text-slate-200"
              >
                <span className="w-2 h-2 rounded-full bg-cyan-400"></span>
                <span className="font-mono text-[11px]">{sec}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Code Snippet Preview */}
        <div>
          <div className="flex items-center justify-between mb-3">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-300 flex items-center space-x-1.5">
              <Terminal className="w-4 h-4 text-blue-400" />
              <span>Code Implementation Preview ({framework})</span>
            </h4>
            <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700">
              nbformat v4
            </span>
          </div>

          <div className="p-4 rounded-xl bg-slate-950 border border-slate-800 font-mono text-xs text-slate-300 overflow-x-auto max-h-[360px] leading-relaxed">
            {isDL ? (
              <pre className="text-purple-300">{`# TensorFlow 2 Deep Learning Architecture
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, callbacks

model = keras.Sequential([
    layers.Input(shape=(input_dim,)),
    layers.Dense(64, activation='relu', kernel_initializer='he_normal'),
    layers.BatchNormalization(),
    layers.Dropout(0.30),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy', keras.metrics.AUC(name='auc')]
)

# Training with EarlyStopping
early_stop = callbacks.EarlyStopping(
    monitor='val_loss', patience=10, restore_best_weights=True
)
history = model.fit(
    X_train, y_train, validation_data=(X_val, y_val),
    epochs=50, batch_size=32, callbacks=[early_stop]
)`}</pre>
            ) : (
              <pre className="text-blue-300">{`# Scikit-Learn Ensemble Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, roc_auc_score

rf_model = RandomForestClassifier(
    n_estimators=150,
    max_depth=8,
    min_samples_split=4,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)

# Stratified 5-Fold Cross Validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(rf_model, X_train, y_train, cv=cv, scoring='roc_auc')
print(f"CV ROC-AUC: {scores.mean():.4f}")

rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)
print(classification_report(y_test, y_pred))`}</pre>
            )}
          </div>

          <div className="mt-3 p-2.5 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-[11px] text-cyan-200 flex items-center justify-between">
            <span>✨ Self-contained synthetic data included — runnable directly in Google Colab or JupyterLab.</span>
          </div>
        </div>
      </div>
    </div>
  )
}
