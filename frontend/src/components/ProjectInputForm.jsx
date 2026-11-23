import React from 'react'
import { Sparkles, Brain, Network, Database, Code2, Globe, Layers, ArrowRight } from 'lucide-react'

export default function ProjectInputForm({
  formData,
  onChange,
  onSubmit,
  onLoadExample,
  loading
}) {
  const domains = [
    "Education & EdTech",
    "Cybersecurity & IoT",
    "Healthcare & Medical Imaging",
    "FinTech & Banking",
    "Natural Language Processing (NLP)",
    "Computer Vision & Autonomous Systems",
    "E-Commerce & Recommendation Systems",
    "Environmental Science & Smart Cities",
    "Manufacturing & Predictive Maintenance"
  ]

  const languages = ["Python", "Python & C++ (Edge)", "R", "Julia"]

  return (
    <div className="glass-panel rounded-2xl p-6 sm:p-8 border border-slate-700/60 shadow-2xl relative overflow-hidden">
      {/* Decorative accent top bar */}
      <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-purple-500 via-indigo-500 to-blue-500"></div>

      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-slate-800 gap-4">
        <div>
          <h2 className="text-xl font-bold text-white flex items-center space-x-2">
            <Sparkles className="w-5 h-5 text-purple-400" />
            <span>Project Specification & Scope Input</span>
          </h2>
          <p className="text-xs text-slate-400 mt-1">
            Specify your problem domain and parameters to trigger chained AI lifecycle planning.
          </p>
        </div>

        {/* Quick Demo Pre-fill Pills */}
        <div className="flex flex-wrap items-center gap-2">
          <span className="text-xs text-slate-400 font-medium">Load Preset:</span>
          <button
            type="button"
            onClick={() => onLoadExample('student_performance')}
            className="px-2.5 py-1 text-xs rounded-lg bg-indigo-500/15 hover:bg-indigo-500/25 text-indigo-300 border border-indigo-500/30 transition-all font-medium flex items-center space-x-1"
          >
            <span>📚 Student Performance (ML)</span>
          </button>
          <button
            type="button"
            onClick={() => onLoadExample('iot_intrusion_detection')}
            className="px-2.5 py-1 text-xs rounded-lg bg-purple-500/15 hover:bg-purple-500/25 text-purple-300 border border-purple-500/30 transition-all font-medium flex items-center space-x-1"
          >
            <span>🛡️ IoT Intrusion (DL)</span>
          </button>
        </div>
      </div>

      <form onSubmit={onSubmit} className="mt-6 space-y-6">
        {/* Project Title & Domain Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          <div>
            <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">
              Project Title <span className="text-purple-400">*</span>
            </label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={onChange}
              required
              placeholder="e.g. Student Academic Performance Prediction"
              className="w-full px-4 py-2.5 rounded-xl bg-slate-900/80 border border-slate-700/80 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500 text-sm transition-all"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2 flex items-center space-x-1.5">
              <Globe className="w-3.5 h-3.5 text-blue-400" />
              <span>Application Domain</span>
            </label>
            <select
              name="domain"
              value={formData.domain}
              onChange={onChange}
              className="w-full px-4 py-2.5 rounded-xl bg-slate-900/80 border border-slate-700/80 text-white focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500 text-sm transition-all"
            >
              {domains.map((d) => (
                <option key={d} value={d} className="bg-slate-900 text-white">
                  {d}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Project Type Selector: ML vs DL Visual Cards */}
        <div>
          <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">
            Project Type Selection <span className="text-purple-400">*</span>
          </label>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {/* Traditional ML Card */}
            <div
              onClick={() => onChange({ target: { name: 'project_type', value: 'Machine Learning' } })}
              className={`cursor-pointer p-4 rounded-xl border transition-all ${
                formData.project_type === 'Machine Learning'
                  ? 'bg-blue-600/15 border-blue-500 shadow-glow-blue'
                  : 'bg-slate-900/50 border-slate-700/60 hover:border-slate-600'
              }`}
            >
              <div className="flex items-center space-x-3">
                <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                  formData.project_type === 'Machine Learning' ? 'bg-blue-500/20 text-blue-400' : 'bg-slate-800 text-slate-400'
                }`}>
                  <Brain className="w-5 h-5" />
                </div>
                <div className="flex-1">
                  <div className="flex items-center justify-between">
                    <span className="font-semibold text-sm text-white">Machine Learning (ML)</span>
                    {formData.project_type === 'Machine Learning' && (
                      <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30">
                        ACTIVE
                      </span>
                    )}
                  </div>
                  <p className="text-xs text-slate-400 mt-0.5">
                    Traditional algorithms: Random Forest, Gradient Boosting, XGBoost, Scikit-learn
                  </p>
                </div>
              </div>
            </div>

            {/* Deep Learning Card */}
            <div
              onClick={() => onChange({ target: { name: 'project_type', value: 'Deep Learning' } })}
              className={`cursor-pointer p-4 rounded-xl border transition-all ${
                formData.project_type === 'Deep Learning'
                  ? 'bg-purple-600/15 border-purple-500 shadow-glow-purple'
                  : 'bg-slate-900/50 border-slate-700/60 hover:border-slate-600'
              }`}
            >
              <div className="flex items-center space-x-3">
                <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                  formData.project_type === 'Deep Learning' ? 'bg-purple-500/20 text-purple-400' : 'bg-slate-800 text-slate-400'
                }`}>
                  <Network className="w-5 h-5" />
                </div>
                <div className="flex-1">
                  <div className="flex items-center justify-between">
                    <span className="font-semibold text-sm text-white">Deep Learning (DL)</span>
                    {formData.project_type === 'Deep Learning' && (
                      <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-purple-500/20 text-purple-300 border border-purple-500/30">
                        ACTIVE
                      </span>
                    )}
                  </div>
                  <p className="text-xs text-slate-400 mt-0.5">
                    Neural networks: CNN, RNN/LSTM, Transformers, TensorFlow 2 / Keras
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Problem Statement Textarea */}
        <div>
          <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">
            Problem Statement & Functional Requirements <span className="text-purple-400">*</span>
          </label>
          <textarea
            name="problem_statement"
            value={formData.problem_statement}
            onChange={onChange}
            required
            rows={4}
            placeholder="Describe the analytical objective, target metric requirements, constraints, and business intent in detail..."
            className="w-full px-4 py-3 rounded-xl bg-slate-900/80 border border-slate-700/80 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500 text-sm transition-all font-sans leading-relaxed"
          ></textarea>
        </div>

        {/* Dataset Info & Language */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          <div className="md:col-span-2">
            <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2 flex items-center space-x-1.5">
              <Database className="w-3.5 h-3.5 text-emerald-400" />
              <span>Dataset Information (Optional)</span>
            </label>
            <input
              type="text"
              name="dataset_info"
              value={formData.dataset_info}
              onChange={onChange}
              placeholder="e.g. Student attendance, quiz scores, socio-demographic indicators (15,000 records)"
              className="w-full px-4 py-2.5 rounded-xl bg-slate-900/80 border border-slate-700/80 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500 text-sm transition-all"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2 flex items-center space-x-1.5">
              <Code2 className="w-3.5 h-3.5 text-cyan-400" />
              <span>Preferred Language</span>
            </label>
            <select
              name="language"
              value={formData.language}
              onChange={onChange}
              className="w-full px-4 py-2.5 rounded-xl bg-slate-900/80 border border-slate-700/80 text-white focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500 text-sm transition-all"
            >
              {languages.map((l) => (
                <option key={l} value={l} className="bg-slate-900 text-white">
                  {l}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Submit Button */}
        <div className="pt-2 flex justify-end">
          <button
            type="submit"
            disabled={loading}
            className={`w-full sm:w-auto px-8 py-3.5 rounded-xl font-bold text-sm tracking-wide text-white transition-all flex items-center justify-center space-x-2 shadow-lg ${
              loading
                ? 'bg-purple-800/50 cursor-not-allowed opacity-80'
                : 'bg-gradient-to-r from-purple-600 via-indigo-600 to-blue-600 hover:from-purple-500 hover:to-blue-500 shadow-glow-purple active:scale-95'
            }`}
          >
            {loading ? (
              <>
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span>Synthesizing Chained Lifecycle Plan...</span>
              </>
            ) : (
              <>
                <Sparkles className="w-4 h-4 text-purple-200" />
                <span>Generate Complete Project Plan</span>
                <ArrowRight className="w-4 h-4" />
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  )
}
