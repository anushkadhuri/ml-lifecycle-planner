# Demonstration Project 2: Intrusion Detection System for IoT Devices (Deep Learning)

**Domain:** Cybersecurity & Internet of Things (IoT)  
**Paradigm:** Deep Learning  
**Frameworks:** TensorFlow 2, Keras, NumPy, Pandas, Scikit-learn, TensorBoard, Docker  
**Primary Architecture:** 4-Layer Deep Neural Network with Batch Normalization, Dropout, He-Normal Initialization, and Early Stopping  

---

## 1. Executive Summary & Problem Formulation
- **Business Charter:** Real-time intrusion detection and zero-day threat mitigation across distributed IoT sensor gateways and edge nodes.
- **Problem Statement:** Detect malicious network traffic, DDoS packets, brute-force attempts, and anomalous protocol behaviors within 5ms latency ceilings.
- **Optimization Metric:** Detection Rate / Recall (target >= 99.0%), False Positive Rate (target <= 0.1%), and p95 Inference Latency (target <= 5.0ms).

---

## 2. Mermaid Workflow Diagram

```mermaid
flowchart TD
    classDef stageNode fill:#111936,stroke:#7c3aed,stroke-width:2px,color:#f8fafc,rx:8,ry:8;
    classDef privNode fill:#07242c,stroke:#06b6d4,stroke-width:1.5px,color:#67e8f9,stroke-dasharray: 4 2,rx:6,ry:6;
    classDef biasNode fill:#2d123d,stroke:#ec4899,stroke-width:1.5px,color:#fbcfe8,stroke-dasharray: 4 2,rx:6,ry:6;
    classDef startNode fill:#1e1b4b,stroke:#6366f1,stroke-width:3px,color:#ffffff,rx:12,ry:12;
    classDef endNode fill:#064e3b,stroke:#10b981,stroke-width:3px,color:#ecfdf5,rx:12,ry:12;

    START(["🚀 <b>IoT Network Intrusion Detection System</b><br/><small>Deep Learning Roadmap</small>"]):::startNode

    S1["<b>1. Problem Definition</b><br/><small>Role: Lead AI Security Architect</small>"]:::stageNode
    S2["<b>2. Data Collection</b><br/><small>Role: Network Telemetry Engineer</small>"]:::stageNode
    S3["<b>3. Data Exploration (EDA)</b><br/><small>Role: Threat Intelligence Analyst</small>"]:::stageNode
    S4["<b>4. Data Preprocessing</b><br/><small>Role: ML Data Preparation</small>"]:::stageNode
    S5["<b>5. Feature Engineering</b><br/><small>Role: Cyber Feature Scientist</small>"]:::stageNode
    S6["<b>6. Model Selection</b><br/><small>Framework: TensorFlow 2 / Keras</small>"]:::stageNode
    S7["<b>7. Model Training</b><br/><small>Role: MLOps Training Specialist</small>"]:::stageNode
    S8["<b>8. Model Evaluation</b><br/><small>Role: Benchmarking Specialist</small>"]:::stageNode
    S9["<b>9. Model Optimization</b><br/><small>Role: Performance Tuning (TFLite/INT8)</small>"]:::stageNode
    S10["<b>10. Deployment</b><br/><small>Role: Edge MLOps Architect (Docker/Triton)</small>"]:::stageNode
    S11["<b>11. Monitoring & Maintenance</b><br/><small>Role: SOC Observability Lead</small>"]:::stageNode

    P1{{"🔒 Privacy: Anonymize IP & MAC Headers"}}:::privNode
    B2{{"⚖️ Fairness: Heterogeneous Sensor Coverage"}}:::biasNode
    P4{{"🔒 Privacy: Ephemeral Packet Parsing"}}:::privNode
    B5{{"⚖️ Bias: Protocol Representation Audit"}}:::biasNode
    B8{{"⚖️ Fairness: Zero-Day Slice Robustness"}}:::biasNode
    P10{{"🔒 Privacy: mTLS & Zero Payload Retention"}}:::privNode
    B11{{"⚖️ Fairness: Continuous Threat Drift Alarms"}}:::biasNode

    START --> S1
    S1 -.-> P1
    S1 --> S2
    S2 -.-> B2
    S2 --> S3
    S3 --> S4
    S4 -.-> P4
    S4 --> S5
    S5 -.-> B5
    S5 --> S6
    S6 --> S7
    S7 --> S8
    S8 -.-> B8
    S8 --> S9
    S9 --> S10
    S10 -.-> P10
    S10 --> S11
    S11 -.-> B11

    COMPLETE(["✅ <b>Production Operational State</b><br/><small>Active Threat Mitigation Live</small>"]):::endNode
    S11 --> COMPLETE
```

---

## 3. 11-Stage Technical Specification

### Stage 1: Problem Definition
- **Role:** Lead AI Security Architect & Product Strategist
- **Objective:** Formulate real-time binary and multi-class anomaly detection for IoT packet streams. Establish < 5ms inference SLA and > 99% detection rate.
- **Privacy Check:** PII Identification — classify IP addresses, MAC addresses, and payload payloads as sensitive device identifiers.
- **Fairness Check:** Sensor Parity — guarantee detection thresholds remain equally sensitive across low-power microcontrollers and high-throughput gateways.

### Stage 2: Data Collection
- **Role:** Network Telemetry & Data Acquisition Engineer
- **Objective:** Capture raw PCAP packet dumps across heterogeneous IoT testbeds (MQTT, CoAP, ZigBee, HTTP). Extract 78 flow-level statistical metrics.
- **Tools:** Zeek, Wireshark, Scapy, Kafka, DVC.
- **Expected Output:** Versioned network telemetry dataset snapshot.
- **Privacy Check:** Automated hash tokenization on IP source/destination headers.

### Stage 3: Data Understanding and Exploration (EDA)
- **Role:** Threat Intelligence & Data Analyst
- **Objective:** Profile packet length distributions, inter-arrival time variances, and extreme class imbalance (99.8% benign traffic vs. 0.2% attack vectors).
- **Tools:** Pandas, NumPy, Seaborn, Matplotlib.
- **Expected Output:** 15-plot exploratory security report and class imbalance audit.

### Stage 4: Data Preprocessing
- **Role:** ML Data Preparation Specialist
- **Objective:** Apply log1p transform to heavy-tailed flow durations; scale using RobustScaler; encode categorical network protocols.
- **Tools:** Scikit-learn, TensorFlow `tf.data` API.
- **Expected Output:** Preprocessed float32 tensors with zero leakage across train/validation/test partitions.
- **Privacy Check:** Confirm complete removal of raw packet payloads; retain purely statistical flow metrics.

### Stage 5: Feature Engineering
- **Role:** Cyber Feature Scientist
- **Objective:** Compute rolling SYN/ACK ratios, byte-per-second velocity, failed authentication counts, and flow entropy.
- **Tools:** Scikit-learn, SciPy, Pandas.
- **Expected Output:** 32 high-signal dimensional feature representation.

### Stage 6: Model Selection
- **Role:** Principal ML Research Scientist
- **Objective:** Benchmark Deep 1D-CNN vs. Multi-Layer Perceptron (MLP) vs. Bi-LSTM. Select Deep MLP with Batch Normalization for ultra-fast edge CPU/MCU inference.
- **Tools:** TensorFlow 2, Keras.
- **Expected Output:** Neural Architecture Specification (Input -> Dense 64 -> BN -> Dropout 0.3 -> Dense 32 -> Dense 1 Sigmoid).

### Stage 7: Model Training
- **Role:** MLOps Training Specialist
- **Objective:** Train model in TensorFlow 2 with Adam optimizer (lr=0.001), Binary Crossentropy loss, and EarlyStopping with patience=10.
- **Tools:** TensorFlow 2.15, TensorBoard, MLflow.
- **Expected Output:** Trained `.keras` model artifact with convergence loss logs.

### Stage 8: Model Evaluation
- **Role:** Benchmarking & Security Validation Specialist
- **Objective:** Evaluate against unseen test packet flows; calculate Detection Rate (Recall: 99.4%), False Alarm Rate (0.08%), and ROC-AUC (0.992).
- **Tools:** Scikit-learn, Matplotlib, Integrated Gradients.
- **Expected Output:** Evaluation report with Confusion Matrix and ROC curve.

### Stage 9: Model Optimization
- **Role:** Performance & Hyperparameter Tuning Engineer
- **Objective:** Post-Training INT8 Quantization via TensorFlow Lite; benchmark inference latency on simulated ARM Cortex-A53 / Raspberry Pi.
- **Tools:** TFLite Converter, ONNX, Netron.
- **Expected Output:** Quantized `iot_nids.tflite` model (< 2.1 MB binary footprint, 3.8ms latency).

### Stage 10: Deployment
- **Role:** Edge MLOps & Production Architect
- **Objective:** Deploy as lightweight containerized microservice via Docker or Triton Server at the IoT network edge gateway.
- **Tools:** Docker, Triton Inference Server, FastAPI, Kubernetes.
- **Expected Output:** Running inference service with authenticated gRPC/REST endpoints.

### Stage 11: Monitoring and Maintenance
- **Role:** SOC Observability & Reliability Lead
- **Objective:** Real-time monitoring of feature distribution drift; detect new attack variants when reconstruction confidence degrades.
- **Tools:** Prometheus, Grafana, Evidently AI, Snort.
- **Expected Output:** Live SOC dashboard with automated alert webhooks to security incident response teams.

---

## 4. T5 Executive Summary
> "The 'Intrusion Detection System for IoT Devices' initiative delivers an enterprise-ready Deep Learning solution for Cybersecurity & IoT. Targeting real-time malicious network traffic and zero-day threat detection, the roadmap establishes an 11-stage development lifecycle leveraging a TensorFlow 2 deep neural network architecture. The pipeline transitions from DVC-versioned network telemetry ingestion and exploratory distribution profiling to rigorous leakage-free preprocessing. Model training integrates hyperparameter optimization and cross-validated holdout evaluation, reinforced by Fairlearn subgroup audits and strict IP/MAC de-identification. Deployment leverages containerized microservices equipped with Prometheus telemetry and Evidently AI concept drift alarms for resilient long-term maintenance."
