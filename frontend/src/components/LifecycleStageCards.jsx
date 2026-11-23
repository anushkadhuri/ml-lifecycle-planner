import React, { useState } from 'react'
import {
  Layers,
  UserCheck,
  Target,
  ListChecks,
  Wrench,
  FileInput,
  FileOutput,
  AlertTriangle,
  ShieldCheck,
  Scale,
  ChevronDown,
  ChevronUp,
  Sparkles,
  Link2
} from 'lucide-react'

export default function LifecycleStageCards({ stages }) {
  const [filterPhase, setFilterPhase] = useState('ALL')
  const [expandedStages, setExpandedStages] = useState(
    // By default expand first 3 stages
    stages ? stages.slice(0, 3).map((s) => s.stage_id) : [1, 2, 3]
  )

  if (!stages || stages.length === 0) return null

  const toggleStage = (id) => {
    if (expandedStages.includes(id)) {
      setExpandedStages(expandedStages.filter((sId) => sId !== id))
    } else {
      setExpandedStages([...expandedStages, id])
    }
  }

  const expandAll = () => setExpandedStages(stages.map((s) => s.stage_id))
  const collapseAll = () => setExpandedStages([])

  // Filter logic
  const filteredStages = stages.filter((s) => {
    if (filterPhase === 'DATA') return s.stage_id >= 1 && s.stage_id <= 4
    if (filterPhase === 'MODEL') return s.stage_id >= 5 && s.stage_id <= 9
    if (filterPhase === 'OPS') return s.stage_id >= 10 && s.stage_id <= 11
    return true
  })

  return (
    <div className="glass-panel rounded-2xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between pb-6 border-b border-slate-800 gap-4">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-purple-600/20 border border-purple-500/30 flex items-center justify-center text-purple-400">
            <Layers className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h3 className="text-lg font-bold text-white">Complete 11-Stage Lifecycle Plan</h3>
              <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-purple-500/20 text-purple-300 border border-purple-500/30">
                U1 Role-Based Personas
              </span>
            </div>
            <p className="text-xs text-slate-400">
              Chained sequential prompts generating deep technical activities, tooling, inputs/outputs, and governance checkpoints.
            </p>
          </div>
        </div>

        {/* Phase Filter Tabs & Toggle All */}
        <div className="flex flex-wrap items-center gap-2">
          <div className="bg-slate-900 border border-slate-800 rounded-lg p-0.5 flex text-xs">
            <button
              onClick={() => setFilterPhase('ALL')}
              className={`px-3 py-1 rounded font-medium transition-all ${
                filterPhase === 'ALL' ? 'bg-purple-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
              }`}
            >
              All (11)
            </button>
            <button
              onClick={() => setFilterPhase('DATA')}
              className={`px-3 py-1 rounded font-medium transition-all ${
                filterPhase === 'DATA' ? 'bg-purple-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
              }`}
            >
              Data (1-4)
            </button>
            <button
              onClick={() => setFilterPhase('MODEL')}
              className={`px-3 py-1 rounded font-medium transition-all ${
                filterPhase === 'MODEL' ? 'bg-purple-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
              }`}
            >
              Modeling (5-9)
            </button>
            <button
              onClick={() => setFilterPhase('OPS')}
              className={`px-3 py-1 rounded font-medium transition-all ${
                filterPhase === 'OPS' ? 'bg-purple-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
              }`}
            >
              MLOps (10-11)
            </button>
          </div>

          <div className="flex items-center space-x-1.5 text-xs text-slate-400">
            <button
              onClick={expandAll}
              className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700"
            >
              Expand All
            </button>
            <button
              onClick={collapseAll}
              className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700"
            >
              Collapse
            </button>
          </div>
        </div>
      </div>

      {/* Stage Cards List */}
      <div className="mt-6 space-y-4">
        {filteredStages.map((stage) => {
          const isExpanded = expandedStages.includes(stage.stage_id)

          return (
            <div
              key={stage.stage_id}
              className="rounded-xl border border-slate-800 bg-slate-900/50 overflow-hidden transition-all hover:border-slate-700"
            >
              {/* Stage Card Header (Clickable Accordion) */}
              <div
                onClick={() => toggleStage(stage.stage_id)}
                className="p-4 sm:p-5 flex items-center justify-between cursor-pointer hover:bg-slate-850/60 transition-colors"
              >
                <div className="flex items-center space-x-3.5">
                  <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-purple-600 to-indigo-600 flex items-center justify-center font-bold text-white text-xs font-mono shadow-md">
                    {stage.stage_id}
                  </div>
                  <div>
                    <div className="flex flex-wrap items-center gap-2">
                      <h4 className="text-base font-bold text-white">
                        {stage.name}
                      </h4>
                      {/* Role Persona Badge */}
                      <span className="text-[11px] font-medium px-2.5 py-0.5 rounded-full bg-indigo-500/15 text-indigo-300 border border-indigo-500/25 flex items-center space-x-1">
                        <UserCheck className="w-3 h-3" />
                        <span>Role: {stage.role}</span>
                      </span>
                    </div>
                    <p className="text-xs text-slate-400 line-clamp-1 mt-0.5">
                      {stage.objective}
                    </p>
                  </div>
                </div>

                <div className="flex items-center space-x-3">
                  {stage.stage_id > 1 && (
                    <span className="hidden sm:flex items-center space-x-1 text-[10px] font-mono text-purple-400 bg-purple-500/10 px-2 py-0.5 rounded border border-purple-500/20">
                      <Link2 className="w-2.5 h-2.5" />
                      <span>Chained (S{stage.stage_id - 1})</span>
                    </span>
                  )}
                  <button className="p-1 rounded-lg text-slate-400 hover:text-white">
                    {isExpanded ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
                  </button>
                </div>
              </div>

              {/* Stage Card Expanded Details */}
              {isExpanded && (
                <div className="px-5 pb-6 pt-2 border-t border-slate-800/80 bg-slate-950/40 space-y-5">
                  {/* Stage Objective */}
                  <div className="p-3.5 rounded-lg bg-purple-900/10 border border-purple-500/20">
                    <span className="text-xs font-semibold uppercase tracking-wider text-purple-300 flex items-center space-x-1.5 mb-1">
                      <Target className="w-3.5 h-3.5" />
                      <span>Stage Objective</span>
                    </span>
                    <p className="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
                      {stage.objective}
                    </p>
                  </div>

                  {/* Detailed Activities Checklist */}
                  <div>
                    <h5 className="text-xs font-semibold uppercase tracking-wider text-slate-300 mb-2 flex items-center space-x-1.5">
                      <ListChecks className="w-3.5 h-3.5 text-indigo-400" />
                      <span>Detailed Technical Activities ({stage.activities.length} Tasks)</span>
                    </h5>
                    <div className="grid grid-cols-1 gap-2">
                      {stage.activities.map((act, aIdx) => (
                        <div
                          key={aIdx}
                          className="flex items-start space-x-2.5 p-2.5 rounded-lg bg-slate-900/70 border border-slate-800/80 text-xs text-slate-200"
                        >
                          <span className="w-4 h-4 rounded-full bg-purple-600/20 text-purple-400 flex items-center justify-center font-mono text-[10px] font-bold shrink-0 mt-0.5">
                            {aIdx + 1}
                          </span>
                          <span className="leading-relaxed">{act}</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Inputs, Outputs & Tools Grid */}
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                    {/* Expected Input */}
                    <div className="p-3 rounded-lg bg-slate-900/60 border border-slate-800">
                      <span className="text-[10px] uppercase font-semibold text-slate-400 flex items-center space-x-1 mb-1.5">
                        <FileInput className="w-3 h-3 text-blue-400" />
                        <span>Expected Input</span>
                      </span>
                      <p className="text-slate-300 leading-relaxed text-[11px]">
                        {stage.expected_input}
                      </p>
                    </div>

                    {/* Expected Output */}
                    <div className="p-3 rounded-lg bg-slate-900/60 border border-slate-800">
                      <span className="text-[10px] uppercase font-semibold text-slate-400 flex items-center space-x-1 mb-1.5">
                        <FileOutput className="w-3 h-3 text-emerald-400" />
                        <span>Expected Output</span>
                      </span>
                      <p className="text-slate-300 leading-relaxed text-[11px]">
                        {stage.expected_output}
                      </p>
                    </div>

                    {/* Recommended Tools */}
                    <div className="p-3 rounded-lg bg-slate-900/60 border border-slate-800">
                      <span className="text-[10px] uppercase font-semibold text-slate-400 flex items-center space-x-1 mb-1.5">
                        <Wrench className="w-3 h-3 text-purple-400" />
                        <span>Recommended Tools</span>
                      </span>
                      <div className="flex flex-wrap gap-1 mt-1">
                        {stage.recommended_tools.map((tool, tIdx) => (
                          <span
                            key={tIdx}
                            className="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-purple-300 border border-slate-700 font-mono"
                          >
                            {tool}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>

                  {/* Possible Challenges & Mitigations */}
                  <div className="p-3 rounded-lg bg-amber-950/20 border border-amber-500/25 text-xs text-amber-200">
                    <span className="font-semibold text-amber-300 flex items-center space-x-1.5 mb-1 text-[11px] uppercase tracking-wider">
                      <AlertTriangle className="w-3.5 h-3.5 text-amber-400" />
                      <span>Possible Challenges & Mitigations</span>
                    </span>
                    <p className="leading-relaxed text-[11px] text-amber-200/90 font-sans">
                      {stage.possible_challenges}
                    </p>
                  </div>

                  {/* Responsible AI Checkpoints (Privacy & Fairness) */}
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2">
                    {/* Privacy Checkpoint */}
                    <div className="p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/25 text-xs">
                      <div className="flex items-center justify-between mb-1.5">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-cyan-300 flex items-center space-x-1">
                          <ShieldCheck className="w-3.5 h-3.5 text-cyan-400" />
                          <span>Privacy Checkpoint</span>
                        </span>
                        <span className="text-[9px] font-bold px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-mono">
                          {stage.privacy_checkpoint.status}
                        </span>
                      </div>
                      <p className="text-[11px] text-cyan-100 font-medium mb-1">
                        {stage.privacy_checkpoint.checkpoint}
                      </p>
                      <p className="text-[11px] text-slate-300 leading-relaxed mb-1.5 font-sans">
                        {stage.privacy_checkpoint.details}
                      </p>
                      <p className="text-[10px] text-cyan-300/80 font-mono">
                        Action: {stage.privacy_checkpoint.action}
                      </p>
                    </div>

                    {/* Fairness Checkpoint */}
                    <div className="p-3 rounded-lg bg-pink-950/20 border border-pink-500/25 text-xs">
                      <div className="flex items-center justify-between mb-1.5">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-pink-300 flex items-center space-x-1">
                          <Scale className="w-3.5 h-3.5 text-pink-400" />
                          <span>Bias & Fairness Checkpoint</span>
                        </span>
                        <span className={`text-[9px] font-bold px-1.5 py-0.5 rounded border font-mono ${
                          stage.fairness_checkpoint.status === 'WARNING'
                            ? 'bg-amber-500/20 text-amber-300 border-amber-500/30'
                            : 'bg-pink-500/20 text-pink-300 border-pink-500/30'
                        }`}>
                          {stage.fairness_checkpoint.status}
                        </span>
                      </div>
                      <p className="text-[11px] text-pink-100 font-medium mb-1">
                        {stage.fairness_checkpoint.checkpoint}
                      </p>
                      <p className="text-[11px] text-slate-300 leading-relaxed mb-1.5 font-sans">
                        {stage.fairness_checkpoint.details}
                      </p>
                      <p className="text-[10px] text-pink-300/80 font-mono">
                        Action: {stage.fairness_checkpoint.action}
                      </p>
                    </div>
                  </div>
                </div>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}
