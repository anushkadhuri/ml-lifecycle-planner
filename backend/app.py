"""
Flask Backend Application for ML/DL Lifecycle Planner.
Provides RESTful APIs for Chained Prompt Planning, Sentence-BERT Retrieval,
T5 Summarization, Mermaid Flowcharts, Notebook Generation, and Responsible AI Auditing.
Also serves the compiled React frontend for a unified full-stack application experience.
"""

import os
import io
import json
from flask import Flask, request, jsonify, send_file, send_from_directory, make_response
from flask_cors import CORS

from modules.lifecycle_engine import lifecycle_engine
from modules.sbert_retriever import retriever
from modules.t5_summarizer import t5_summarizer
from modules.mermaid_generator import mermaid_generator
from modules.notebook_generator import notebook_generator
from modules.cover_generator import cover_generator
from modules.responsible_ai import responsible_ai_auditor

# Path to built React frontend
DIST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "dist"))

app = Flask(__name__, static_folder=DIST_DIR, static_url_path="")
# Enable CORS for Vite dev server (port 5173) and any origin
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

# Sample Demonstration Projects (Requirement 8)
SAMPLE_DEMO_PROJECTS = {
    "student_performance": {
        "id": "demo-ml-student",
        "title": "Student Performance Prediction & Early Intervention System",
        "project_type": "Machine Learning",
        "domain": "Education & EdTech",
        "preferred_language": "Python",
        "dataset_info": "Historical student demographic data, weekly study hours, attendance rates, past test scores, and LMS activity logs.",
        "problem_statement": "Predict student end-of-semester academic outcomes and identify at-risk students early to enable proactive academic counseling and targeted support interventions. Use robust data preprocessing, feature engineering, Random Forest, and model evaluation."
    },
    "iot_intrusion_detection": {
        "id": "demo-dl-iot",
        "title": "Intrusion Detection System for IoT Devices (IoT-NIDS)",
        "project_type": "Deep Learning",
        "domain": "Cybersecurity & Internet of Things",
        "preferred_language": "Python",
        "dataset_info": "Heterogeneous IoT network traffic capture containing 78 statistical network flow features, packet lengths, inter-arrival times, and attack signatures (DDoS, PortScan, BruteForce).",
        "problem_statement": "Detect malicious network traffic and anomalous cyberattacks on IoT connected devices in near real-time using deep learning. Use network traffic preprocessing, neural network architecture, TensorFlow 2, and performance evaluation."
    }
}

# --- Frontend Serving Routes ---
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    """Serves the production React frontend bundle from frontend/dist."""
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    if os.path.exists(os.path.join(app.static_folder, "index.html")):
        return send_from_directory(app.static_folder, "index.html")
    return jsonify({
        "message": "ML/DL Lifecycle Planner Backend is running.",
        "api_docs": "/api/health",
        "frontend_status": "Build frontend with 'cd frontend && npm run build' to serve UI here."
    })

# --- API Endpoints ---
@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check and AI module status report."""
    return jsonify({
        "status": "healthy",
        "service": "ML/DL Lifecycle Planner Engine",
        "version": "2.4.0",
        "modules": {
            "sbert_retriever": {
                "active": True,
                "engine": "Sentence-BERT (all-MiniLM-L6-v2) / Semantic Vector Cosine Engine",
                "corpus_size": len(retriever.projects)
            },
            "t5_summarizer": {
                "active": True,
                "engine": "Hugging Face T5-small / Abstractive Synthesis Pipeline"
            },
            "lifecycle_engine": {
                "active": True,
                "stages_configured": 11,
                "chain_enabled": True
            },
            "notebook_generator": {
                "active": True,
                "backend": "nbformat v4",
                "frameworks": ["TensorFlow 2 / Keras", "Scikit-Learn"]
            },
            "cover_generator": {
                "active": True,
                "engine": "Autonomous Neural Canvas Synthesis Engine (Pillow)"
            },
            "responsible_ai": {
                "active": True,
                "checkpoints": 10
            }
        }
    })

@app.route("/api/examples", methods=["GET"])
def get_examples():
    """Returns the two ready-to-use sample demonstration projects."""
    return jsonify({
        "success": True,
        "examples": list(SAMPLE_DEMO_PROJECTS.values())
    })

@app.route("/api/similar-projects", methods=["POST"])
def get_similar_projects():
    """U3: Sentence-BERT semantic similarity search against past projects repository."""
    data = request.get_json() or {}
    query = data.get("problem_statement") or data.get("query") or ""
    project_type = data.get("project_type")
    top_k = int(data.get("top_k", 3))

    results = retriever.retrieve_similar(query=query, top_k=top_k, project_type_filter=project_type)
    return jsonify({
        "success": True,
        "query": query,
        "top_similar_projects": results
    })

@app.route("/api/summarize/t5", methods=["POST"])
def summarize_plan_endpoint():
    """U2: T5 summarization of a project plan."""
    data = request.get_json() or {}
    project_spec = data.get("project_spec", {})
    stages = data.get("stages", [])

    summary_result = t5_summarizer.summarize_plan(project_spec=project_spec, stages=stages)
    return jsonify({
        "success": True,
        "summary": summary_result
    })

@app.route("/api/plan/generate", methods=["POST"])
def generate_full_plan():
    """
    Core Orchestrator Endpoint:
    Traverses U1 to U5 sequentially:
    1. Sentence-BERT retrieves similar past projects (U3)
    2. Chained prompt engine executes all 11 lifecycle stages with role-based personas (U1, U2)
    3. T5 encoder-decoder summarizes complete plan (U2)
    4. Mermaid generator builds flowchart diagram with privacy/bias nodes (U1, U5)
    5. Responsible AI auditor evaluates safety guardrails (U5)
    6. Cover image generator creates AI-themed project banner (U4)
    """
    data = request.get_json() or {}

    title = data.get("title", "").strip() or "Intelligent Predictive Analytics System"
    problem_statement = data.get("problem_statement", "").strip() or "Build an automated machine learning prediction model."
    project_type = data.get("project_type", "Deep Learning")
    domain = data.get("domain", "").strip() or "General Artificial Intelligence"
    language = data.get("language", "Python")
    dataset_info = data.get("dataset_info", "").strip() or "Standard domain tabular and sequential event logs"

    project_spec = {
        "title": title,
        "problem_statement": problem_statement,
        "project_type": project_type,
        "domain": domain,
        "language": language,
        "dataset_info": dataset_info
    }

    # Step 1: Sentence-BERT Retrieval (U3)
    similar_projects = retriever.retrieve_similar(
        query=f"{title}. {domain}. {problem_statement}",
        top_k=3,
        project_type_filter=project_type
    )

    # Step 2: Sequential Chained Prompt Execution for all 11 stages (U1, U2)
    stages = lifecycle_engine.execute_chain(
        project_spec=project_spec,
        retrieved_projects=similar_projects
    )

    # Step 3: T5 Summarization (U2)
    t5_summary = t5_summarizer.summarize_plan(
        project_spec=project_spec,
        stages=stages
    )

    # Step 4: Mermaid Workflow Diagram Generation (U1, U5)
    mermaid_data = mermaid_generator.generate_diagram(
        project_spec=project_spec,
        stages=stages
    )

    # Step 5: Responsible AI Privacy & Bias Audit (U5)
    responsible_ai_report = responsible_ai_auditor.evaluate_project(
        project_spec=project_spec,
        stages=stages
    )

    # Step 6: Cover Image Generation (U4)
    cover_data = cover_generator.generate_cover_image(project_spec=project_spec)

    response_payload = {
        "success": True,
        "project_spec": project_spec,
        "t5_summary": t5_summary,
        "similar_projects": similar_projects,
        "stages": stages,
        "mermaid_diagram": mermaid_data,
        "responsible_ai": responsible_ai_report,
        "cover_image": {
            "data_uri": cover_data["image_data_uri"],
            "theme": cover_data["theme"],
            "engine": cover_data["generator_mode"]
        }
    }

    return jsonify(response_payload)

@app.route("/api/notebook/download", methods=["POST"])
def download_notebook():
    """U4: Downloads starter Jupyter Notebook (.ipynb) with TensorFlow 2 or Scikit-learn."""
    data = request.get_json() or {}
    project_spec = data.get("project_spec") or {
        "title": data.get("title", "ML_Project"),
        "project_type": data.get("project_type", "Deep Learning"),
        "domain": data.get("domain", "General AI"),
        "problem_statement": data.get("problem_statement", "Predictive modeling pipeline")
    }

    notebook_content = notebook_generator.generate_notebook(project_spec=project_spec)

    # Sanitize title for filename
    clean_title = "".join(c for c in project_spec.get("title", "ml_dl_project") if c.isalnum() or c in (' ', '_', '-')).rstrip()
    filename = f"{clean_title.replace(' ', '_').lower()}_starter_notebook.ipynb"

    bio = io.BytesIO()
    bio.write(notebook_content.encode("utf-8"))
    bio.seek(0)

    return send_file(
        bio,
        as_attachment=True,
        download_name=filename,
        mimetype="application/x-ipynb+json"
    )

@app.route("/api/image/download", methods=["POST"])
def download_cover_image():
    """U4: Downloads high-resolution AI-themed project cover image (.png)."""
    data = request.get_json() or {}
    project_spec = data.get("project_spec") or {
        "title": data.get("title", "AI_Project"),
        "project_type": data.get("project_type", "Deep Learning"),
        "domain": data.get("domain", "General AI")
    }

    cover_data = cover_generator.generate_cover_image(project_spec=project_spec)
    clean_title = "".join(c for c in project_spec.get("title", "project") if c.isalnum() or c in (' ', '_', '-')).rstrip()
    filename = f"{clean_title.replace(' ', '_').lower()}_cover.png"

    bio = io.BytesIO(cover_data["image_bytes"])
    bio.seek(0)

    return send_file(
        bio,
        as_attachment=True,
        download_name=filename,
        mimetype="image/png"
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5050))
    print(f"[*] ML/DL Lifecycle Planner backend starting on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
