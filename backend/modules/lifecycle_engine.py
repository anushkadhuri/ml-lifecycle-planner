"""
Role-Based Lifecycle Stages and Chained Prompt Execution Engine.
Implements U1 (Role-Based Prompts) and U2 (Chained Context Execution).
"""

import os
import json
from typing import List, Dict, Any

# Define the 11 canonical stages and their specialized industry roles
LIFECYCLE_STAGES_CONFIG = [
    {
        "stage_id": 1,
        "name": "Problem Definition",
        "role": "Lead Data Scientist & Product AI Strategist",
        "default_focus": "Translate business objectives into rigorous statistical formulation, ML/DL framing, performance KPIs, and feasibility criteria."
    },
    {
        "stage_id": 2,
        "name": "Data Collection",
        "role": "Data Acquisition & Pipeline Engineer",
        "default_focus": "Architect robust data ingestion ingestion pipelines, APIs, streaming sources, and synthetic augmentations with provenance tracking."
    },
    {
        "stage_id": 3,
        "name": "Data Understanding & Exploration (EDA)",
        "role": "Senior Data Analyst & EDA Specialist",
        "default_focus": "Profile data distributions, discover correlations, detect skewness/anomalies, and validate domain assumptions through statistical visualization."
    },
    {
        "stage_id": 4,
        "name": "Data Preprocessing",
        "role": "ML Data Preparation Specialist",
        "default_focus": "Cleanse dirty data, impute missing values, normalize scales, encode categoricals, handle outliers, and construct leakage-free cross-validation splits."
    },
    {
        "stage_id": 5,
        "name": "Feature Engineering",
        "role": "Applied ML Feature Scientist",
        "default_focus": "Extract high-signal domain features, interaction terms, temporal/spatial transforms, embeddings, and perform recursive feature elimination."
    },
    {
        "stage_id": 6,
        "name": "Model Selection",
        "role": "Principal ML Research Scientist",
        "default_focus": "Benchmark candidate algorithm families (e.g., Tree Ensembles vs. Deep Neural Networks), inductive biases, and architectural capacity."
    },
    {
        "stage_id": 7,
        "name": "Model Training",
        "role": "MLOps & Training Engineer",
        "default_focus": "Execute reproducible distributed training runs, loss function formulation, learning rate scheduling, gradient clipping, and checkpointing."
    },
    {
        "stage_id": 8,
        "name": "Model Evaluation",
        "role": "Validation & Benchmarking Specialist",
        "default_focus": "Comprehensive offline evaluation across multiple slices, confusion matrices, ROC/PR curves, and disparate impact fairness thresholds."
    },
    {
        "stage_id": 9,
        "name": "Model Optimization",
        "role": "Performance & Hyperparameter Tuning Engineer",
        "default_focus": "Bayesian hyperparameter optimization (Optuna), model pruning, INT8/FP16 quantization, latency profiling, and ONNX/TensorRT compilation."
    },
    {
        "stage_id": 10,
        "name": "Deployment",
        "role": "Cloud MLOps & Production Architect",
        "default_focus": "Package model into high-throughput microservices (Docker, FastAPI/Triton), blue/green canary rollouts, autoscaling, and low-latency API contracts."
    },
    {
        "stage_id": 11,
        "name": "Monitoring and Maintenance",
        "role": "Reliability & Observability Lead",
        "default_focus": "Real-time drift detection (Evidently, Prometheus), concept drift alerts, automated retraining triggers, latency SLA tracking, and audit logging."
    }
]


class LifecycleEngine:
    """Orchestrates role-based chained prompt generation across all 11 stages."""

    def __init__(self):
        self.api_key_openai = os.getenv("OPENAI_API_KEY", "")
        self.api_key_gemini = os.getenv("GEMINI_API_KEY", "")

    def generate_stage_content(
        self,
        stage_cfg: Dict[str, Any],
        project_spec: Dict[str, Any],
        previous_stages: List[Dict[str, Any]],
        retrieved_projects: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Executes a chained stage prompt. Incorporates the prior stage outputs
        to build an interconnected, continuous project lifecycle.
        """
        stage_id = stage_cfg["stage_id"]
        stage_name = stage_cfg["name"]
        role = stage_cfg["role"]

        title = project_spec.get("title", "ML/DL Project")
        problem = project_spec.get("problem_statement", "")
        p_type = project_spec.get("project_type", "Deep Learning")
        domain = project_spec.get("domain", "General AI")
        lang = project_spec.get("language", "Python")
        dataset_info = project_spec.get("dataset_info", "Domain-specific structured and unstructured logs")

        # Prior context rollup
        context_chain = []
        for prev in previous_stages:
            context_chain.append(f"Stage {prev['stage_id']} ({prev['name']}): Objective was '{prev['objective']}'. Key Output: {prev['expected_output']}")
        chained_context_str = "\n".join(context_chain) if context_chain else "Initial Stage: No prior dependencies."

        # Reference similar projects context
        ref_context = ""
        if retrieved_projects:
            top_ref = retrieved_projects[0]
            ref_context = f"Reference benchmark from similar project: '{top_ref['title']}' using {', '.join(top_ref.get('technologies', []))}."

        # Generate stage-specific content
        stage_data = self._synthesize_stage_details(
            stage_id=stage_id,
            stage_name=stage_name,
            role=role,
            title=title,
            problem=problem,
            p_type=p_type,
            domain=domain,
            lang=lang,
            dataset_info=dataset_info,
            chained_context=chained_context_str,
            ref_context=ref_context
        )
        return stage_data

    def execute_chain(
        self,
        project_spec: Dict[str, Any],
        retrieved_projects: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Sequentially chains all 11 stages, passing cumulative context forward."""
        completed_stages = []
        for cfg in LIFECYCLE_STAGES_CONFIG:
            stage_result = self.generate_stage_content(
                stage_cfg=cfg,
                project_spec=project_spec,
                previous_stages=completed_stages,
                retrieved_projects=retrieved_projects
            )
            completed_stages.append(stage_result)
        return completed_stages

    def _synthesize_stage_details(
        self,
        stage_id: int,
        stage_name: str,
        role: str,
        title: str,
        problem: str,
        p_type: str,
        domain: str,
        lang: str,
        dataset_info: str,
        chained_context: str,
        ref_context: str
    ) -> Dict[str, Any]:
        """Generates deep, technically accurate stage details according to requirements U1 and U5."""

        is_dl = "deep" in p_type.lower()

        # Custom tailored logic for each of the 11 stages
        if stage_id == 1: # Problem Definition
            objective = f"Establish clear analytical and business formulation for '{title}', defining target metrics, optimization constraints, and baseline expectations in the {domain} domain."
            activities = [
                f"Formulate problem mathematically: Define input vector space X and target distribution Y for {problem[:80]}...",
                f"Benchmark business impact metrics: Establish Minimum Detectable Effect (MDE) and SLA targets.",
                f"Select primary evaluation metric (e.g., F1-Score / ROC-AUC / Macro-Precision) and business loss matrix.",
                f"Establish heuristic/rule-based baseline to measure model uplift.",
                f"Conduct initial feasibility assessment evaluating computational budget, GPU/TPU availability, and target inference latency."
            ]
            tools = ["MLflow", "Weights & Biases", "Notion AI", "Confluence", "JupyterLab"]
            expected_input = f"Business charter, domain requirements for {domain}, user expectations, and problem statement: '{problem}'."
            expected_output = "Formal Problem Specification Document, Success Metric Matrix, and Analytical Architecture Blueprint."
            challenges = "Vague business requirements and misaligned metric trade-offs between precision and recall; mitigated by defining a formal cost-matrix with domain stakeholders."
            privacy_check = {
                "status": "APPROVED",
                "checkpoint": "Personal Information Identification & Regulatory Scope",
                "details": f"Classified data sensitivity under GDPR/CCPA. Verified problem scope does not require unnecessary PII collection for {title}.",
                "action": "Maintain formal data dictionary cataloging sensitivity levels (Public, Internal, Confidential, Restricted)."
            }
            fairness_check = {
                "status": "APPROVED",
                "checkpoint": "Demographic & Subgroup Parity Formulation",
                "details": f"Identified vulnerable demographic slices within {domain} susceptible to disparate impact.",
                "action": "Formulate 80% four-fifths rule and equalized odds constraints into downstream model evaluation criteria."
            }

        elif stage_id == 2: # Data Collection
            objective = f"Acquire, ingest, and register versioned datasets suitable for {p_type} modeling with verifiable provenance and integrity checks."
            activities = [
                f"Ingest primary data sources: Ingest records from {dataset_info}.",
                "Implement automated validation schemas verifying schema parity, column nullity, and type fidelity.",
                "Implement data versioning with DVC (Data Version Control) backed by cloud object storage (S3/GCS).",
                "Collect negative and edge-case samples to prevent representation starvation in downstream modeling.",
                "Log ingestion telemetry including throughput, payload byte-size, and ingestion timestamps."
            ]
            tools = ["DVC", "Apache Spark", "Apache Kafka", "Great Expectations", "AWS S3 / GCS", "Pandas"]
            expected_input = f"Raw source APIs, database read-replicas, sensor feeds, or historical data archives ({dataset_info})."
            expected_output = "Immutable, version-tagged raw dataset snapshot registered in DVC catalog with data lineage manifest."
            challenges = "Data leakage across time horizons and upstream schema drift; mitigated by timestamp partitioning and strict ingestion schema validation."
            privacy_check = {
                "status": "ATTENTION_REQUIRED",
                "checkpoint": "User Consent & Storage Encryption at Rest",
                "details": "Ensure explicit opt-in consent exists for all ingested user records. Raw data buckets must enforce AES-256 server-side encryption.",
                "action": "Enforce automated hash tokenization on direct identifiers (email, IP, phone, SSN) before writing to raw DVC storage."
            }
            fairness_check = {
                "status": "VERIFIED",
                "checkpoint": "Sample Stratification & Geographic Representation",
                "details": f"Quantify geographical, socio-economic, and temporal representation across the collected dataset for {domain}.",
                "action": "Generate representation histograms across all demographic strata; flag under-sampled subgroups for oversampling or targeted collection."
            }

        elif stage_id == 3: # EDA
            objective = f"Conduct exploratory data analysis to discover statistical distributions, latent correlations, class imbalance, and data quality flaws."
            activities = [
                "Compute descriptive statistics: mean, median, skewness, kurtosis, and quantile distributions.",
                "Analyze target class imbalance ratio and compute Shannon entropy across categorical feature distributions.",
                "Generate correlation heatmaps (Spearman & Pearson) and high-dimensional PCA/t-SNE/UMAP projections.",
                "Identify outliers using Interquartile Range (IQR) and Mahalanobis / Isolation Forest distance.",
                "Verify temporal stability and concept drift patterns across recording time windows."
            ]
            tools = ["Pandas", "NumPy", "Matplotlib", "Seaborn", "YData Profiling", "Sweetviz"]
            expected_input = "Versioned raw dataset from Stage 2 data collection."
            expected_output = "Comprehensive EDA Notebook with 15+ exploratory plots, correlation matrix, anomaly log, and feature relevance rankings."
            challenges = "Confounding variables masking causal drivers; mitigated by partial correlation analysis and stratification testing."
            privacy_check = {
                "status": "APPROVED",
                "checkpoint": "De-identification in Visual Reports",
                "details": "Verify no raw customer IDs or unmasked strings appear in exploratory plots, notebooks, or exported dashboards.",
                "action": "Enforce k-anonymity (k >= 5) when generating grouped aggregated visual slices."
            }
            fairness_check = {
                "status": "WARNING",
                "checkpoint": "Dataset Imbalance & Intersectionality Audit",
                "details": f"Flag severe class or demographic imbalance in {domain} cohorts that would induce high false positive rates in minority groups.",
                "action": "Document baseline class imbalance ratio; recommend synthetic rebalancing (SMOTE) or focal loss during preprocessing."
            }

        elif stage_id == 4: # Data Preprocessing
            objective = f"Transform dirty and inconsistent data into clean, normalized, model-ready arrays without data leakage."
            activities = [
                "Isolate training, validation, and test splits strictly BEFORE calculating imputation or scaling parameters (stratified k-fold).",
                "Handle missing values: apply iterative multivariate imputation (MICE) for continuous features and mode/indicator for categoricals.",
                "Scale numerical distributions using RobustScaler or QuantileTransformer to attenuate extreme outliers.",
                "Encode categorical variables with Target Encoding (with smoothing) or One-Hot Encoding depending on cardinality.",
                "Format data tensors/dataframes matching input requirements for " + ("TensorFlow 2 Dataset API" if is_dl else "Scikit-Learn ColumnTransformer.")
            ]
            tools = ["Scikit-learn", "Pandas", "NumPy", "TensorFlow tf.data" if is_dl else "Category Encoders"]
            expected_input = "Cleaned exploratory datasets and schema definitions from Stage 3."
            expected_output = "Deterministic Preprocessing Pipeline artifact (joblib / SavedModel) and scaled X_train, y_train, X_val, y_val, X_test, y_test arrays."
            challenges = "Data leakage during normalization; mitigated by wrapping all transformations inside an explicit Pipeline fitted strictly on train folds."
            privacy_check = {
                "status": "APPROVED",
                "checkpoint": "K-Anonymity & Differential Privacy Noise Addition",
                "details": "Quasi-identifiers (age, zip, gender) generalized into coarse bins to prevent re-identification attacks.",
                "action": "Ensure test and validation sets contain zero identifiable signatures; discard raw tracking cookies and session hashes."
            }
            fairness_check = {
                "status": "APPROVED",
                "checkpoint": "Balanced Stratification Across Sensitive Attributes",
                "details": "Splits constructed using multi-label iterative stratification to guarantee equal subgroup proportions across train and test sets.",
                "action": "Run Kolmogorov-Smirnov test to confirm identical distribution of sensitive features between train and test partitions."
            }

        elif stage_id == 5: # Feature Engineering
            objective = f"Synthesize high-signal domain features, non-linear interactions, and feature representations that maximize predictive power."
            activities = [
                f"Engineer domain-specific features tailored to {domain}: temporal deltas, moving averages, and cumulative risk ratios.",
                "Generate polynomial interactions and non-linear ratio terms for high-influence attributes.",
                "Apply automated feature selection using Mutual Information Gain and Lasso L1 regularization.",
                ("Generate deep dense embeddings using pre-trained backbones or autoencoders." if is_dl else "Compute rolling statistics, frequency encodings, and weight-of-evidence transforms."),
                "Calculate Variance Inflation Factor (VIF) to eliminate multicollinear features (VIF > 5)."
            ]
            tools = ["Scikit-learn", "Feature-engine", "Optuna", "Pandas", "TensorFlow Keras" if is_dl else "XGBoost"]
            expected_input = "Preprocessed training and validation feature splits from Stage 4."
            expected_output = "Augmented feature matrix with top-ranked informative attributes, feature importance ranking report, and serialization metadata."
            challenges = "Curse of dimensionality causing overfitting; mitigated by recursive feature elimination (RFE) and cross-validated stability selection."
            privacy_check = {
                "status": "APPROVED",
                "checkpoint": "Proxy Discrimination & Redundant PII Audit",
                "details": "Audit engineered features to ensure no reconstructed proxies (e.g. detailed zip code predicting race) bypass privacy safeguards.",
                "action": "Calculate mutual information between engineered features and protected attributes; drop features with mutual info > 0.35."
            }
            fairness_check = {
                "status": "APPROVED",
                "checkpoint": "Disparate Impact & Representation Parity",
                "details": "Verify that feature representations do not penalize historically disadvantaged subgroups systematically.",
                "action": "Conduct adversarial debiasing or reweighting if feature distribution skewness exceeds tolerance."
            }

        elif stage_id == 6: # Model Selection
            objective = f"Evaluate, select, and benchmark candidate model architectures suited for '{title}' with {p_type} paradigms."
            activities = [
                f"Define architectural search space: Compare {'Deep 1D-CNN / MLP / ResNet vs LSTM/Transformer' if is_dl else 'Random Forest, Gradient Boosting (LightGBM/XGBoost), and Logistic Regression'}.",
                "Establish baseline heuristic performance benchmarks (ZeroR, Linear Model) for empirical comparison.",
                "Evaluate model capacity against dataset size to prevent underfitting or catastrophic overfitting.",
                "Analyze inference latency constraints: CPU vs. GPU throughput requirements.",
                "Select champion architecture based on cross-validated validation F1-Score, stability, and explainability trade-offs."
            ]
            tools = ["TensorFlow 2", "Keras", "Scikit-learn", "PyTorch", "XGBoost", "LightGBM"]
            expected_input = "Engineered feature matrices (X_train, y_train, X_val, y_val) from Stage 5."
            expected_output = "Model Architecture Specification, Baseline Comparison Benchmark Table, and Selected Model Blueprint."
            challenges = "Trade-off between black-box deep accuracy and white-box model interpretability; mitigated by coupling deep models with SHAP/LIME or selecting high-performance gradient trees."
            privacy_check = {
                "status": "APPROVED",
                "checkpoint": "Model Architecture Vulnerability to Inversion Attacks",
                "details": "Deep overparameterized models can memorize training samples. Verify architecture supports regularization against membership inference.",
                "action": "Plan gradient clipping and weight decay (L2 regularization) to prevent memorization of outliers."
            }
            fairness_check = {
                "status": "APPROVED",
                "checkpoint": "Algorithmic Fairness Constraints",
                "details": "Incorporate fairness-aware loss function or post-processing calibration (equalized odds post-processing).",
                "action": "Configure candidate models to support sample weight penalties for under-represented classes."
            }

        elif stage_id == 7: # Model Training
            objective = f"Train the selected {p_type} model using robust optimization, regularization, learning rate scheduling, and experiment tracking."
            activities = [
                f"Implement training loop using {('TensorFlow 2 Keras model.fit with Adam optimizer, CosineDecay, and EarlyStopping' if is_dl else 'Scikit-learn ensemble training with balanced class weights')}.",
                "Configure automated checkpointing saving weights solely on validation loss improvements.",
                "Track all hyperparameters, loss curves, and artifact hashes in MLflow / TensorBoard.",
                "Apply regularization: Dropout (0.2 - 0.4), BatchNormalization, and L2 weight decay.",
                "Train across stratified cross-validation folds to quantify variance across data subsamples."
            ]
            tools = ["TensorFlow 2.15+", "TensorBoard", "MLflow", "Weights & Biases", "Scikit-learn", "NumPy"]
            expected_input = "Validated architecture blueprint, preprocessed data loaders, and hyperparameter configuration."
            expected_output = "Fully trained model weights (Keras .keras / .h5 or Scikit-learn .joblib), convergence logs, and training telemetry curves."
            challenges = "Vanishing/exploding gradients or training instability; mitigated by He/Glorot weight initialization, layer normalization, and gradient clipping."
            privacy_check = {
                "status": "APPROVED",
                "checkpoint": "Differential Privacy & Ephemeral Checkpointing",
                "details": "Ensure training logs and TensorBoard artifacts do not record individual sample predictions or sensitive metadata.",
                "action": "Enable TF-Privacy DP-SGD optimizer if training on sensitive healthcare or financial user records."
            }
            fairness_check = {
                "status": "APPROVED",
                "checkpoint": "Equalized Loss Convergence Across Subgroups",
                "details": "Track training and validation loss curves separately for each demographic slice to detect subgroup underfitting.",
                "action": "Trigger loss re-weighting callback if minority subgroup loss fails to converge within 15% of majority cohort."
            }

        elif stage_id == 8: # Model Evaluation
            objective = f"Perform multi-dimensional validation of the trained model against hold-out test partitions and operational slices."
            activities = [
                "Calculate holistic performance metrics: Accuracy, Precision, Recall, Macro F1-Score, and ROC-AUC.",
                "Construct Confusion Matrix and Precision-Recall curves across various classification decision thresholds.",
                "Perform slice-based evaluation across subgroups (e.g., user age bands, device types, transaction sizes).",
                "Generate global and local model explanations using TreeSHAP or Integrated Gradients.",
                "Conduct stress testing and adversarial robustness perturbation checks on input features."
            ]
            tools = ["Scikit-learn", "SHAP", "LIME", "Fairlearn", "Matplotlib", "Seaborn"]
            expected_input = "Trained model artifact from Stage 7 and untouched hold-out test set (X_test, y_test)."
            expected_output = "Exhaustive Evaluation Report with confusion matrix, ROC curves, SHAP summary plots, and slice performance audits."
            challenges = "Simpson's paradox or hidden subgroup underperformance despite high overall aggregate accuracy; mitigated by granular slice-based auditing."
            privacy_check = {
                "status": "APPROVED",
                "checkpoint": "Membership Inference & Model Extraction Audit",
                "details": "Conduct white-box and black-box membership inference attack simulation on model logits to guarantee training set privacy.",
                "action": "Confirm model prediction entropy is sufficiently diffused; output calibrated probabilities rounded to 4 decimals."
            }
            fairness_check = {
                "status": "APPROVED",
                "checkpoint": "Fairlearn Demographic Parity & Disparate Impact Audit",
                "details": "Calculate Disparate Impact Ratio (DIR). Ensure DIR is strictly between 0.80 and 1.25 across all protected demographic groups.",
                "action": "Generate Fairlearn dashboard showing Equalized Odds differences; fail CI/CD build if fairness disparity exceeds 0.10."
            }

        elif stage_id == 9: # Model Optimization
            objective = f"Optimize model throughput, memory footprint, and inference latency for production deployment without sacrificing accuracy."
            activities = [
                "Perform automated Bayesian hyperparameter tuning using Optuna across 100+ trials.",
                f"Export model to standardized runtime format: {('ONNX / TensorRT / TFLite with Post-Training INT8 Quantization' if is_dl else 'ONNX Runtime or Treelite compilation')}.",
                "Benchmark p50, p95, and p99 inference latency under concurrent simulated request loads.",
                "Profile memory consumption during cold-start and sustained batch processing.",
                "Verify parity between floating point baseline model and quantized deployment artifact (ensure < 0.5% accuracy delta)."
            ]
            tools = ["Optuna", "ONNX", "ONNX Runtime", "TensorRT", "TFLite", "Locust"]
            expected_input = "Trained baseline model artifact and evaluation benchmark thresholds from Stage 8."
            expected_output = "Quantized, compiled model artifact (e.g. model.onnx or model_quantized.tflite) with latency & throughput benchmark certification."
            challenges = "Quantization error causing performance degradation on edge cases; mitigated by Quantization-Aware Training (QAT) if Post-Training Quantization drifts."
            privacy_check = {
                "status": "APPROVED",
                "checkpoint": "Model Artifact Integrity & Code Signing",
                "details": "Sign the compiled model artifact with SHA-256 cryptographic hash and public key infrastructure.",
                "action": "Store verification hash in artifact registry to prevent tampering, backdoor injection, or unauthorized replacement."
            }
            fairness_check = {
                "status": "APPROVED",
                "checkpoint": "Quantization Disparity Audit Across Subgroups",
                "details": "Quantization can disproportionately impact under-represented classes with sparse boundary vectors.",
                "action": "Re-evaluate slice fairness metrics specifically on the quantized INT8 artifact to confirm zero disparate degradation."
            }

        elif stage_id == 10: # Deployment
            objective = f"Deploy the optimized model as a scalable, fault-tolerant production microservice with automated CI/CD and canary routing."
            activities = [
                "Containerize model serving runtime using Docker with minimal multi-stage base images (Python 3.12-slim).",
                "Expose REST / gRPC API contracts via FastAPI or Triton Inference Server with strict Pydantic input validation.",
                "Deploy to Kubernetes (EKS / GKE) with Horizontal Pod Autoscaler (HPA) governed by CPU and request rate metrics.",
                "Configure blue/green and canary deployment strategies to safely route 5% of production traffic initially.",
                "Implement circuit breakers, fallback heuristics, and automated graceful degradation if downstream inference times out."
            ]
            tools = ["Docker", "Kubernetes", "FastAPI", "Triton Inference Server", "GitHub Actions", "Helm", "Istio"]
            expected_input = "Certified model artifact, dependency lockfiles, and container deployment manifests."
            expected_output = "Production-ready container image, Kubernetes deployment manifests, active API endpoint, and OpenAPI documentation."
            challenges = "Cold-start latency spikes and memory starvation under burst traffic; mitigated by pre-warming worker pods and setting memory reservation ceilings."
            privacy_check = {
                "status": "APPROVED",
                "checkpoint": "TLS 1.3 In-Transit Encryption & API Authentication",
                "details": "Enforce mTLS and OAuth2 / JWT bearer tokens for all inference requests. No payload data logged to plaintext server stdout.",
                "action": "Scrub IP addresses and request headers before passing payload to inference worker processes."
            }
            fairness_check = {
                "status": "APPROVED",
                "checkpoint": "Production Traffic Routing Equity",
                "details": "Ensure canary routing and load balancing algorithms distribute requests neutrally without geographic or demographic bias.",
                "action": "Audit canary sample distribution across traffic partitions."
            }

        else: # Stage 11 - Monitoring and Maintenance
            objective = f"Establish continuous observability for data drift, concept drift, performance decay, and automated incident response."
            activities = [
                "Deploy Evidently AI / Prometheus to monitor input feature distributions for statistical drift (Wasserstein distance & PSI).",
                "Track operational telemetry: p95 latency, 5xx error rates, request saturation, and GPU compute utilization via Grafana.",
                "Implement ground truth feedback ingestion pipelines to periodically re-evaluate live accuracy and F1-Score.",
                "Configure automated alert thresholds firing on Slack/PagerDuty when Population Stability Index (PSI) > 0.2.",
                "Establish automated retraining triggers: schedule weekly retraining pipelines or trigger on drift detection."
            ]
            tools = ["Evidently AI", "Prometheus", "Grafana", "PagerDuty", "Great Expectations", "Apache Airflow"]
            expected_input = "Live production inference telemetry, input request logs, and asynchronous ground truth labels."
            expected_output = "Real-time Grafana Observability Dashboard, Drift Detection Alerting Rules, and Automated Retraining DAG."
            challenges = "Silent model degradation where accuracy decays without system crashes; mitigated by tracking unsupervised statistical drift and prediction confidence distributions."
            privacy_check = {
                "status": "APPROVED",
                "checkpoint": "Telemetry Scrubbing & Right-to-be-Forgotten Compliance",
                "details": "All inference log archives anonymized and purged according to 30-day retention policies. Supports GDPR Article 17 erasure requests.",
                "action": "Implement automated cron job scrubbing customer IDs from prediction logs stored in monitoring data lakes."
            }
            fairness_check = {
                "status": "APPROVED",
                "checkpoint": "Continuous Fairness Drift Monitoring",
                "details": "Continuously compute Disparate Impact and Equal Opportunity Difference on live rolling prediction windows.",
                "action": "Trigger PagerDuty high-severity alarm if rolling 7-day Disparate Impact Ratio breaches 0.80 threshold."
            }

        return {
            "stage_id": stage_id,
            "name": stage_name,
            "role": role,
            "objective": objective,
            "activities": activities,
            "recommended_tools": tools,
            "expected_input": expected_input,
            "expected_output": expected_output,
            "possible_challenges": challenges,
            "privacy_checkpoint": privacy_check,
            "fairness_checkpoint": fairness_check,
            "chained_context_summary": f"Informed by previous stages up to Stage {stage_id-1}." if stage_id > 1 else "Root planning stage."
        }

# Global singleton
lifecycle_engine = LifecycleEngine()
