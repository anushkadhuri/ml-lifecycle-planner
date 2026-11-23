import React, { useState, useEffect } from 'react'
import Navbar from './components/Navbar'
import HeroHeader from './components/HeroHeader'
import ProjectInputForm from './components/ProjectInputForm'
import T5SummarySection from './components/T5SummarySection'
import SimilarProjectsSection from './components/SimilarProjectsSection'
import MermaidDiagramSection from './components/MermaidDiagramSection'
import LifecycleStageCards from './components/LifecycleStageCards'
import NotebookDownloadSection from './components/NotebookDownloadSection'
import CoverImageSection from './components/CoverImageSection'
import ResponsibleAIReport from './components/ResponsibleAIReport'
import Footer from './components/Footer'
import {
  Sparkles,
  Layers,
  Search,
  Cpu,
  GitFork,
  FileCode2,
  Image as ImageIcon,
  ShieldCheck,
  CheckCircle2,
  AlertCircle
} from 'lucide-react'

// Backend API URL (Proxied via Vite or direct)
const API_BASE = '/api'

export default function App() {
  const [formData, setFormData] = useState({
    title: 'Student Performance Prediction & Early Intervention System',
    project_type: 'Machine Learning',
    domain: 'Education & EdTech',
    preferred_language: 'Python',
    dataset_info: 'Historical student demographic records, weekly attendance, study hours, and past test scores (1,500 records).',
    problem_statement: 'Predict student end-of-semester academic outcomes and identify at-risk students early to enable proactive academic counseling and targeted support interventions. Use robust data preprocessing, feature engineering, Random Forest, and model evaluation.'
  })

  const [loading, setLoading] = useState(false)
  const [activeTab, setActiveTab] = useState('ALL')
  const [planResult, setPlanResult] = useState(null)
  const [errorMessage, setErrorMessage] = useState(null)
  const [backendStatus, setBackendStatus] = useState('Checking...')

  // Check backend health & pre-generate default plan on mount
  useEffect(() => {
    fetch(`${API_BASE}/health`)
      .then((res) => res.json())
      .then((data) => {
        setBackendStatus(data.status === 'healthy' ? 'CONNECTED' : 'STANDBY')
      })
      .catch((err) => {
        console.warn('Backend connect notice:', err)
        setBackendStatus('LOCAL_OFFLINE')
      })

    // Automatically generate the initial plan so the user sees an immediate rich dashboard!
    handleGeneratePlan(null, formData)
  }, [])

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }))
  }

  const handleLoadExample = async (exampleKey) => {
    try {
      const res = await fetch(`${API_BASE}/examples`)
      const data = await res.json()
      if (data.examples) {
        const found = data.examples.find((ex) =>
          exampleKey === 'student_performance'
            ? ex.id.includes('student')
            : ex.id.includes('iot')
        )
        if (found) {
          const updated = {
            title: found.title,
            project_type: found.project_type,
            domain: found.domain,
            preferred_language: found.preferred_language || 'Python',
            dataset_info: found.dataset_info,
            problem_statement: found.problem_statement
          }
          setFormData(updated)
          handleGeneratePlan(null, updated)
        }
      }
    } catch (err) {
      console.error('Failed to load example from backend:', err)
    }
  }

  const handleGeneratePlan = async (e, customData = null) => {
    if (e) e.preventDefault()
    setLoading(true)
    setErrorMessage(null)

    const payload = customData || formData

    try {
      const res = await fetch(`${API_BASE}/plan/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })

      if (!res.ok) {
        throw new Error(`Server returned HTTP ${res.status}`)
      }

      const data = await res.json()
      if (data.success) {
        setPlanResult(data)
      } else {
        throw new Error(data.error || 'Failed to generate plan.')
      }
    } catch (err) {
      console.error('Generation error:', err)
      setErrorMessage(`Generation notice: ${err.message}. Ensure backend server is active.`)
    } finally {
      setLoading(false)
    }
  }

  const handleDownloadNotebook = async () => {
    try {
      const res = await fetch(`${API_BASE}/notebook/download`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          project_spec: planResult?.project_spec || formData
        })
      })

      if (!res.ok) throw new Error('Notebook download failed.')

      const blob = await res.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      const safeTitle = (formData.title || 'project').toLowerCase().replace(/\s+/g, '_')
      a.download = `${safeTitle}_starter_notebook.ipynb`
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)
    } catch (err) {
      console.error('Notebook download error:', err)
      alert('Could not download notebook: ' + err.message)
    }
  }

  const handleDownloadCoverImage = async () => {
    try {
      const res = await fetch(`${API_BASE}/image/download`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          project_spec: planResult?.project_spec || formData
        })
      })

      if (!res.ok) throw new Error('Image download failed.')

      const blob = await res.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      const safeTitle = (formData.title || 'project').toLowerCase().replace(/\s+/g, '_')
      a.download = `${safeTitle}_cover.png`
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)
    } catch (err) {
      console.error('Image download error:', err)
      alert('Could not download image: ' + err.message)
    }
  }

  // Section navigation anchors
  const navTabs = [
    { id: 'sec-input', label: '1. Project Scope' },
    { id: 'sec-summary', label: '2. T5 Summary' },
    { id: 'sec-sbert', label: '3. Similar Projects' },
    { id: 'sec-workflow', label: '4. Mermaid Diagram' },
    { id: 'sec-stages', label: '5. 11 Stages' },
    { id: 'sec-notebook', label: '6. Starter Notebook' },
    { id: 'sec-banner', label: '7. Cover Banner' },
    { id: 'sec-governance', label: '8. Responsible AI' }
  ]

  const scrollToSection = (id) => {
    const el = document.getElementById(id)
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }

  return (
    <div className="min-h-screen bg-[#070b19] text-slate-100 flex flex-col font-sans selection:bg-purple-600 selection:text-white">
      {/* 1. Global Navigation Bar */}
      <Navbar
        onSelectDemo={handleLoadExample}
        backendStatus={backendStatus}
      />

      {/* 2. Hero Header */}
      <HeroHeader />

      {/* Section Quick Jump Pill Bar */}
      <div className="sticky top-16 z-40 bg-[#070b19]/90 backdrop-blur-md border-b border-slate-800/80 py-2.5 shadow-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between overflow-x-auto no-scrollbar gap-2">
          <div className="flex items-center space-x-1 sm:space-x-2 shrink-0">
            {navTabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => scrollToSection(tab.id)}
                className="px-2.5 py-1 text-xs font-medium rounded-lg text-slate-300 hover:text-white hover:bg-slate-800/80 transition-all shrink-0"
              >
                {tab.label}
              </button>
            ))}
          </div>

          {planResult && (
            <div className="hidden lg:flex items-center space-x-2 text-xs font-mono text-purple-300 shrink-0">
              <span className="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
              <span>11 Stages Generated</span>
            </div>
          )}
        </div>
      </div>

      {/* Main Content Dashboard Container */}
      <main className="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-10">
        {/* Error Alert (if any) */}
        {errorMessage && (
          <div className="p-4 rounded-xl bg-red-950/40 border border-red-500/40 text-red-200 text-xs flex items-center space-x-2">
            <AlertCircle className="w-4 h-4 text-red-400 shrink-0" />
            <span>{errorMessage}</span>
          </div>
        )}

        {/* SECTION 1: Problem Statement Input & Configuration */}
        <section id="sec-input">
          <ProjectInputForm
            formData={formData}
            onChange={handleInputChange}
            onSubmit={handleGeneratePlan}
            onLoadExample={handleLoadExample}
            loading={loading}
          />
        </section>

        {/* Loading Spinner Indicator */}
        {loading && (
          <div className="p-12 glass-panel rounded-2xl border border-purple-500/30 flex flex-col items-center justify-center space-y-4 text-center">
            <div className="w-12 h-12 rounded-full border-4 border-purple-500/20 border-t-purple-500 animate-spin"></div>
            <h3 className="text-lg font-bold text-white">Synthesizing Chained Lifecycle Plan...</h3>
            <p className="text-xs text-slate-400 max-w-md">
              Executing role-based prompt chain, calculating Sentence-BERT similarities, formulating T5 abstractive summary, generating Mermaid topology, and compiling starter code.
            </p>
          </div>
        )}

        {/* Generated Plan Content Sections */}
        {!loading && planResult && (
          <>
            {/* SECTION 2: T5 Project Summary (U2) */}
            <section id="sec-summary">
              <T5SummarySection t5Summary={planResult.t5_summary} />
            </section>

            {/* SECTION 3: Sentence-BERT Similar Projects (U3) */}
            <section id="sec-sbert">
              <SimilarProjectsSection similarProjects={planResult.similar_projects} />
            </section>

            {/* SECTION 4: Mermaid Workflow Diagram (Requirement 6) */}
            <section id="sec-workflow">
              <MermaidDiagramSection
                mermaidData={planResult.mermaid_diagram}
                projectTitle={formData.title}
              />
            </section>

            {/* SECTION 5: 11 Lifecycle Stage Cards (U1) */}
            <section id="sec-stages">
              <LifecycleStageCards stages={planResult.stages} />
            </section>

            {/* SECTION 6: TensorFlow 2 / Scikit-Learn Notebook Download (U4) */}
            <section id="sec-notebook">
              <NotebookDownloadSection
                projectSpec={planResult.project_spec}
                onDownloadNotebook={handleDownloadNotebook}
              />
            </section>

            {/* SECTION 7: AI Project Cover Banner (U4) */}
            <section id="sec-banner">
              <CoverImageSection
                coverImage={planResult.cover_image}
                projectSpec={planResult.project_spec}
                onDownloadImage={handleDownloadCoverImage}
              />
            </section>

            {/* SECTION 8: Responsible AI & Governance Audit (U5) */}
            <section id="sec-governance">
              <ResponsibleAIReport responsibleAI={planResult.responsible_ai} />
            </section>
          </>
        )}
      </main>

      {/* Footer */}
      <Footer />
    </div>
  )
}
