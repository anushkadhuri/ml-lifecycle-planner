"""
Past ML/DL Projects Database for Sentence-BERT Similarity Retrieval.
Contains rich project profiles across domains, types, and tech stacks.
"""

PAST_PROJECTS = [
    {
        "id": "proj-001",
        "title": "Student Academic Performance Prediction & Early Intervention",
        "type": "Machine Learning",
        "domain": "Education & EdTech",
        "description": "Predict student semester grade outcomes and dropout risks using historical attendance, demographic indicators, LMS engagement metrics, and past test scores. Employs robust data preprocessing, feature engineering, and ensemble trees with fairness constraints.",
        "technologies": ["Scikit-learn", "Pandas", "Random Forest", "XGBoost", "SHAP", "Matplotlib"],
        "key_metrics": ["ROC-AUC 0.91", "F1-Score 0.88", "Disparate Impact Ratio 0.95"],
        "sample_features": ["attendance_rate", "study_hours_weekly", "assignment_completion_rate", "prior_gpa", "parent_education_level"],
        "lifecycle_summary": "Data cleaning handled missing socio-economic indicators via iterative imputation. Random Forest was calibrated to avoid demographic bias across geographic zones."
    },
    {
        "id": "proj-002",
        "title": "IoT Network Intrusion & Threat Detection System (NIDS)",
        "type": "Deep Learning",
        "domain": "Cybersecurity & IoT",
        "description": "Real-time deep learning system to detect zero-day exploits, DDoS attacks, port scans, and malicious payload patterns in heterogeneous IoT sensor network traffic using flow statistics and packet sequences.",
        "technologies": ["TensorFlow 2", "Keras", "1D-CNN", "Bi-LSTM", "NumPy", "Scapy", "Snort"],
        "key_metrics": ["Detection Rate 99.4%", "False Positive Rate 0.08%", "Inference Latency 4.2ms"],
        "sample_features": ["packet_length_variance", "flow_duration", "syn_ack_ratio", "inter_arrival_time", "byte_rate"],
        "lifecycle_summary": "Extracted 78 statistical network flow features, normalized with RobustScaler, fed into a 4-layer 1D-CNN + Dropout with EarlyStopping and quantization for edge router deployment."
    },
    {
        "id": "proj-003",
        "title": "Pediatric Chest X-Ray Pneumonia Diagnosis Assistant",
        "type": "Deep Learning",
        "domain": "Healthcare & Medical Imaging",
        "description": "Automated triaging and classification of bacterial versus viral pneumonia from chest radiographs using deep convolutional neural networks with Grad-CAM visual interpretability and strict HIPAA de-identification.",
        "technologies": ["TensorFlow 2", "Keras", "EfficientNetV2", "Grad-CAM", "Albumentations", "DICOM"],
        "key_metrics": ["Sensitivity 96.8%", "Specificity 94.2%", "AUC 0.982"],
        "sample_features": ["dicom_pixel_array", "lung_field_contrast", "patient_age_group", "exposure_index"],
        "lifecycle_summary": "De-identified patient metadata; applied heavy CLAHE contrast adjustment and data augmentation; fine-tuned EfficientNetV2 with focal loss to combat class imbalance."
    },
    {
        "id": "proj-004",
        "title": "Real-Time Streaming Credit Card Fraud & Anomaly Detector",
        "type": "Machine Learning",
        "domain": "FinTech & Banking",
        "description": "Low-latency sub-10ms transaction fraud detection on heavily imbalanced transactional streams using graph feature engineering, SMOTE, and ensemble gradient boosted trees with explainable risk scoring.",
        "technologies": ["Scikit-learn", "LightGBM", "XGBoost", "Imbalanced-Learn", "Apache Kafka", "Redis"],
        "key_metrics": ["Precision@Top1% 89.5%", "AUPRC 0.884", "Throughput 15,000 tx/sec"],
        "sample_features": ["tx_amount_zscore_user", "velocity_1h", "distance_from_last_tx", "merchant_risk_score", "card_present_flag"],
        "lifecycle_summary": "Addressed extreme 0.17% fraud prevalence with cost-sensitive XGBoost objective. Calibrated probability threshold to balance false declines against fraud losses."
    },
    {
        "id": "proj-005",
        "title": "Telecommunications Customer Churn & Retention Optimizer",
        "type": "Machine Learning",
        "domain": "Telecom & CRM",
        "description": "Predict 30-day subscriber churn probability and recommend personalized retention discounts based on customer billing history, usage degradation patterns, and support ticket sentiment.",
        "technologies": ["Scikit-learn", "CatBoost", "Pandas", "SHAP", "Optuna", "FastAPI"],
        "key_metrics": ["Churn Recall 86.2%", "F1-Score 0.82", "Annual ROI $2.4M saved"],
        "sample_features": ["monthly_charges", "tenure_months", "data_usage_trend_30d", "unresolved_tickets_count", "contract_type"],
        "lifecycle_summary": "Engineered non-linear usage decay features. Used CatBoost for native handling of categorical billing plans. Integrated TreeSHAP for customer-service explanations."
    },
    {
        "id": "proj-006",
        "title": "Enterprise Multi-Channel Customer Support Sentiment & Intent Classifier",
        "type": "Deep Learning",
        "domain": "Natural Language Processing (NLP)",
        "description": "Contextual classification of incoming omnichannel support tickets, chat transcripts, and emails to route high-urgency complaints, extract key entities, and suggest automated agent replies.",
        "technologies": ["Hugging Face Transformers", "PyTorch", "TensorFlow", "RoBERTa", "FastAPI", "Docker"],
        "key_metrics": ["Intent Accuracy 94.7%", "Macro F1 0.93", "Routing Time Reduced 70%"],
        "sample_features": ["ticket_subject_tokens", "body_embeddings", "customer_tier", "channel_type", "turn_count"],
        "lifecycle_summary": "PII scrubbed via regex and NER. Fine-tuned RoBERTa-base with classification head, quantized to ONNX for CPU-accelerated microservice deployment."
    },
    {
        "id": "proj-007",
        "title": "Autonomous Driving Lane Detection & Drivable Surface Segmentation",
        "type": "Deep Learning",
        "domain": "Automotive & Autonomous Systems",
        "description": "Pixel-level semantic segmentation of urban roadways, road lane markings, curbs, and static obstacles under challenging rain, night-time, and glare conditions using encoder-decoder vision networks.",
        "technologies": ["TensorFlow 2", "Keras", "U-Net", "MobileNetV3", "OpenCV", "TensorRT"],
        "key_metrics": ["Mean IoU 83.4%", "FPS on Jetson Orin: 48", "Boundary F-Score 0.89"],
        "sample_features": ["front_camera_rgb", "illumination_histogram", "weather_condition_flag", "vehicle_speed"],
        "lifecycle_summary": "Trained lightweight U-Net with MobileNetV3 backbone on multi-weather synthetic and real driving datasets. Exported to TensorRT engine with FP16 precision."
    },
    {
        "id": "proj-008",
        "title": "Industrial Turbine Vibration Anomaly & Predictive Maintenance",
        "type": "Deep Learning",
        "domain": "Manufacturing & Smart Energy",
        "description": "Early detection of mechanical degradation and bearing wear in high-speed turbines by modeling multi-axis accelerometer and thermal time series using unsupervised LSTM autoencoders.",
        "technologies": ["TensorFlow 2", "Keras", "LSTM Autoencoder", "SciPy", "Pandas", "Grafana"],
        "key_metrics": ["Mean Time to Detect Degradation: 14 days prior to failure", "Precision 92.1%"],
        "sample_features": ["vibration_axis_x_rms", "kurtosis", "fft_peak_frequencies", "temperature_bearing", "rpm"],
        "lifecycle_summary": "Applied Fast Fourier Transform (FFT) and wavelet transforms to raw 10kHz sensor data. Reconstructed normal operating windows; flagged reconstruction error anomalies."
    },
    {
        "id": "proj-009",
        "title": "Personalized E-Commerce Hybrid Recommendation & Re-Ranking Engine",
        "type": "Deep Learning",
        "domain": "E-Commerce & Retail",
        "description": "Two-stage recommendation system combining candidate retrieval (two-tower neural network) and deep re-ranking (DLRM) to personalize homepage product carousels based on session clicks and purchase affinity.",
        "technologies": ["TensorFlow 2", "Scikit-learn", "Two-Tower Neural Nets", "Faiss", "Pandas"],
        "key_metrics": ["HitRate@10 0.312", "NDCG@10 0.245", "Conversion Rate +14.8%"],
        "sample_features": ["user_purchase_history_vector", "category_clicks_30m", "item_price_tier", "brand_affinity_score"],
        "lifecycle_summary": "Two-tower architecture for fast vector dot-product candidate retrieval via Faiss index, followed by a multi-task ranking model optimizing both CTR and conversion probability."
    },
    {
        "id": "proj-010",
        "title": "Municipal Water Quality & Potability Classification",
        "type": "Machine Learning",
        "domain": "Environmental Science & Public Health",
        "description": "Binary classification of drinking water safety and contaminant levels based on chemical and physical parameters (pH, hardness, solids, chloramines, conductivity, organic carbon, trihalomethanes, turbidity).",
        "technologies": ["Scikit-learn", "Pandas", "Gradient Boosting", "KNN", "Seaborn"],
        "key_metrics": ["Accuracy 88.7%", "Recall (Hazardous Water) 97.4%", "F2-Score 0.94"],
        "sample_features": ["ph_level", "hardness", "solids_ppm", "chloramines", "sulfate", "conductivity", "turbidity"],
        "lifecycle_summary": "Prioritized high recall on non-potable water to prevent public health hazards. Engineered interaction terms between pH and heavy mineral hardness."
    }
]
