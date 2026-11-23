"""
Mermaid Workflow Flowchart Generator for ML/DL Project Lifecycles.
Generates interactive, syntax-compliant flowcharts connecting all 11 stages
with integrated Responsible AI (Privacy & Bias) checkpoints.
"""

from typing import Dict, Any, List

class MermaidGenerator:
    """Generates Mermaid flowchart diagrams with embedded privacy & fairness checkpoints."""

    def generate_diagram(self, project_spec: Dict[str, Any], stages: List[Dict[str, Any]]) -> Dict[str, Any]:
        title = project_spec.get("title", "ML/DL Project")
        p_type = project_spec.get("project_type", "Deep Learning")
        is_dl = "deep" in p_type.lower()

        # Build clean Mermaid diagram syntax
        lines = [
            "flowchart TD",
            "    %% Global Styles",
            "    classDef stageNode fill:#111936,stroke:#7c3aed,stroke-width:2px,color:#f8fafc,rx:8,ry:8;",
            "    classDef privNode fill:#07242c,stroke:#06b6d4,stroke-width:1.5px,color:#67e8f9,stroke-dasharray: 4 2,rx:6,ry:6;",
            "    classDef biasNode fill:#2d123d,stroke:#ec4899,stroke-width:1.5px,color:#fbcfe8,stroke-dasharray: 4 2,rx:6,ry:6;",
            "    classDef startNode fill:#1e1b4b,stroke:#6366f1,stroke-width:3px,color:#ffffff,rx:12,ry:12;",
            "    classDef endNode fill:#064e3b,stroke:#10b981,stroke-width:3px,color:#ecfdf5,rx:12,ry:12;",
            "",
            f"    %% Project: {title} ({p_type})",
            f"    START([\"🚀 <b>{title}</b><br/><small>{p_type} Roadmap</small>\"]):::startNode",
            "",
            "    S1[\"<b>1. Problem Definition</b><br/><small>Role: Lead Data Scientist</small>\"]:::stageNode",
            "    S2[\"<b>2. Data Collection</b><br/><small>Role: Data Acquisition Engineer</small>\"]:::stageNode",
            "    S3[\"<b>3. Data Exploration (EDA)</b><br/><small>Role: Senior Data Analyst</small>\"]:::stageNode",
            "    S4[\"<b>4. Data Preprocessing</b><br/><small>Role: ML Data Preparation</small>\"]:::stageNode",
            "    S5[\"<b>5. Feature Engineering</b><br/><small>Role: Applied ML Feature Scientist</small>\"]:::stageNode",
            f"    S6[\"<b>6. Model Selection</b><br/><small>Framework: {'TensorFlow 2 / Keras' if is_dl else 'Scikit-Learn Ensemble'}</small>\"]:::stageNode",
            "    S7[\"<b>7. Model Training</b><br/><small>Role: MLOps Training Specialist</small>\"]:::stageNode",
            "    S8[\"<b>8. Model Evaluation</b><br/><small>Role: Validation Specialist</small>\"]:::stageNode",
            "    S9[\"<b>9. Model Optimization</b><br/><small>Role: Performance Tuning (Optuna/ONNX)</small>\"]:::stageNode",
            "    S10[\"<b>10. Deployment</b><br/><small>Role: Cloud MLOps Architect (Docker/FastAPI)</small>\"]:::stageNode",
            "    S11[\"<b>11. Monitoring & Maintenance</b><br/><small>Role: Observability Lead (Evidently/Prometheus)</small>\"]:::stageNode",
            "",
            "    %% Responsible AI Checkpoint Nodes",
            "    P1{{\"🔒 Privacy Check:<br/>PII Classification & GDPR\"}}:::privNode",
            "    B2{{\"⚖️ Fairness Check:<br/>Demographic Parity & Sampling\"}}:::biasNode",
            "    P4{{\"🔒 Privacy Check:<br/>K-Anonymity & Storage AES-256\"}}:::privNode",
            "    B5{{\"⚖️ Fairness Check:<br/>Proxy Discrimination Audit\"}}:::biasNode",
            "    B8{{\"⚖️ Fairness Check:<br/>Fairlearn 80% Rule & Disparate Impact\"}}:::biasNode",
            "    P10{{\"🔒 Privacy Check:<br/>TLS 1.3 & Ephemeral Payload Serving\"}}:::privNode",
            "    B11{{\"⚖️ Fairness Check:<br/>Continuous Subgroup Drift Monitor\"}}:::biasNode",
            "",
            "    %% Execution Flow",
            "    START --> S1",
            "    S1 -.-> P1",
            "    S1 --> S2",
            "    S2 -.-> B2",
            "    S2 --> S3",
            "    S3 --> S4",
            "    S4 -.-> P4",
            "    S4 --> S5",
            "    S5 -.-> B5",
            "    S5 --> S6",
            "    S6 --> S7",
            "    S7 --> S8",
            "    S8 -.-> B8",
            "    S8 --> S9",
            "    S9 --> S10",
            "    S10 -.-> P10",
            "    S10 --> S11",
            "    S11 -.-> B11",
            "",
            "    COMPLETE([\"✅ <b>Production Operational State</b><br/><small>SLA & Drift Monitored</small>\"]):::endNode",
            "    S11 --> COMPLETE"
        ]

        mermaid_code = "\n".join(lines)

        return {
            "mermaid_code": mermaid_code,
            "stage_count": len(stages),
            "checkpoint_count": 7,
            "project_title": title,
            "diagram_type": "flowchart TD"
        }

# Global singleton
mermaid_generator = MermaidGenerator()
