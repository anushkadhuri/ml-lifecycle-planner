import React from 'react'
import { Search, Sparkles, Layers, Tag, CheckCircle, BarChart3, ExternalLink } from 'lucide-react'

export default function SimilarProjectsSection({ similarProjects }) {
  if (!similarProjects || similarProjects.length === 0) return null

  return (
    <div className="glass-panel rounded-2xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-5 border-b border-slate-800 gap-3">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-blue-600/20 border border-blue-500/30 flex items-center justify-center text-blue-400">
            <Search className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h3 className="text-lg font-bold text-white">Sentence-BERT Similar Project Retrieval</h3>
              <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30">
                U3 Top 3 Matches
              </span>
            </div>
            <p className="text-xs text-slate-400">
              Matched via S-BERT semantic embeddings and cosine similarity against historical project repository.
            </p>
          </div>
        </div>

        <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-slate-800/80 border border-slate-700 text-xs text-slate-300 font-mono">
          <Sparkles className="w-3.5 h-3.5 text-blue-400" />
          <span>Injected as Planning Context</span>
        </div>
      </div>

      {/* 3 Project Cards Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-5 mt-6">
        {similarProjects.map((project, idx) => {
          const score = project.similarity_score || 75
          const isTop = idx === 0

          return (
            <div
              key={project.id || idx}
              className={`p-5 rounded-xl border flex flex-col justify-between transition-all ${
                isTop
                  ? 'bg-gradient-to-b from-blue-900/20 to-slate-900/60 border-blue-500/50 shadow-glow-blue'
                  : 'bg-slate-900/40 border-slate-800 hover:border-slate-700'
              }`}
            >
              <div>
                {/* Header with Rank & Similarity Score */}
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-semibold px-2 py-0.5 rounded-md bg-slate-800 text-slate-300 border border-slate-700">
                    Rank #{idx + 1}
                  </span>
                  <div className="flex items-center space-x-1.5">
                    <BarChart3 className="w-3.5 h-3.5 text-blue-400" />
                    <span className="text-sm font-bold font-mono text-blue-300">
                      {score}% Match
                    </span>
                  </div>
                </div>

                {/* Similarity Progress Bar */}
                <div className="w-full bg-slate-800/80 rounded-full h-1.5 mb-4 overflow-hidden">
                  <div
                    className="h-1.5 rounded-full bg-gradient-to-r from-blue-500 to-indigo-500 transition-all duration-1000"
                    style={{ width: `${score}%` }}
                  ></div>
                </div>

                {/* Title */}
                <h4 className="text-sm font-bold text-white leading-snug mb-1">
                  {project.title}
                </h4>

                {/* Domain & Type Badge */}
                <div className="flex flex-wrap gap-1.5 mb-3">
                  <span className="text-[10px] font-medium px-2 py-0.5 rounded bg-purple-500/10 text-purple-300 border border-purple-500/20">
                    {project.domain}
                  </span>
                  <span className="text-[10px] font-medium px-2 py-0.5 rounded bg-blue-500/10 text-blue-300 border border-blue-500/20">
                    {project.type}
                  </span>
                </div>

                {/* Description */}
                <p className="text-xs text-slate-300 line-clamp-3 mb-4 leading-relaxed font-sans">
                  {project.description}
                </p>
              </div>

              <div>
                {/* Key Metrics */}
                {project.key_metrics && project.key_metrics.length > 0 && (
                  <div className="mb-3 p-2 rounded bg-slate-950/50 border border-slate-800/60">
                    <span className="text-[10px] uppercase font-semibold tracking-wider text-slate-400 block mb-1">
                      Historical Benchmark Metrics:
                    </span>
                    <div className="flex flex-wrap gap-1">
                      {project.key_metrics.map((m, mIdx) => (
                        <span key={mIdx} className="text-[10px] font-mono text-emerald-300 bg-emerald-500/10 px-1.5 py-0.5 rounded">
                          {m}
                        </span>
                      ))}
                    </div>
                  </div>
                )}

                {/* Technologies */}
                <div className="pt-2 border-t border-slate-800/80">
                  <span className="text-[10px] uppercase font-semibold tracking-wider text-slate-400 block mb-1.5">
                    Tech Stack:
                  </span>
                  <div className="flex flex-wrap gap-1">
                    {project.technologies && project.technologies.map((t, tIdx) => (
                      <span
                        key={tIdx}
                        className="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700/50 font-mono"
                      >
                        {t}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
