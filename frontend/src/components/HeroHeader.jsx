import React from 'react'
import { Sparkles, Layers, Search, FileCode2, ShieldAlert, Cpu } from 'lucide-react'

export default function HeroHeader() {
  const highlights = [
    { label: "11 Lifecycle Stages", icon: Layers, desc: "Role-based AI prompts" },
    { label: "Sentence-BERT Search", icon: Search, desc: "Semantic retrieval" },
    { label: "T5 Summarization", icon: Cpu, desc: "Encoder-decoder model" },
    { label: "Starter Notebooks", icon: FileCode2, desc: "TF2 & Scikit-learn .ipynb" },
    { label: "Responsible AI", icon: ShieldAlert, desc: "Privacy & fairness audits" }
  ]

  return (
    <div className="relative py-8 md:py-12 border-b border-slate-800/60 overflow-hidden">
      {/* Background glow effects */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-purple-600/10 rounded-full blur-3xl pointer-events-none"></div>
      <div className="absolute top-1/3 left-1/4 w-64 h-64 bg-blue-600/10 rounded-full blur-3xl pointer-events-none"></div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
        {/* Sub-badge */}
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-gradient-to-r from-purple-500/10 via-indigo-500/10 to-blue-500/10 border border-purple-500/20 text-xs font-medium text-purple-300 mb-4">
          <Sparkles className="w-3.5 h-3.5 text-purple-400" />
          <span>Enterprise AI/ML Architecture & Governance System</span>
        </div>

        {/* Title */}
        <h1 className="text-3xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-white mb-4">
          Intelligent <span className="bg-gradient-to-r from-purple-400 via-indigo-300 to-blue-400 bg-clip-text text-transparent">ML/DL Lifecycle</span> Planner
        </h1>

        <p className="max-w-3xl mx-auto text-base sm:text-lg text-slate-300 font-light leading-relaxed mb-8">
          Converts simple problem statements into comprehensive, stage-wise Machine Learning and Deep Learning development blueprints. Powered by chained role-based prompts, Sentence-BERT semantic search, T5 summarization, Mermaid flowcharts, and downloadable TensorFlow 2 starter notebooks.
        </p>

        {/* Feature Pills */}
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3 max-w-5xl mx-auto">
          {highlights.map((item, idx) => {
            const Icon = item.icon
            return (
              <div
                key={idx}
                className="glass-panel p-3 rounded-xl border border-slate-700/50 flex flex-col items-center justify-center text-center transition-all hover:border-purple-500/40"
              >
                <div className="w-8 h-8 rounded-lg bg-purple-500/10 flex items-center justify-center text-purple-400 mb-2">
                  <Icon className="w-4 h-4" />
                </div>
                <span className="text-xs font-semibold text-white">{item.label}</span>
                <span className="text-[11px] text-slate-400 mt-0.5">{item.desc}</span>
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
