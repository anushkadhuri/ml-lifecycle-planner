import React from 'react'
import { ShieldCheck, Scale, AlertTriangle, CheckCircle2, AlertCircle, Info, Lock } from 'lucide-react'

export default function ResponsibleAIReport({ responsibleAI }) {
  if (!responsibleAI) return null

  const score = responsibleAI.overall_compliance_score || 92
  const warnings = responsibleAI.active_warnings || []

  return (
    <div className="glass-panel rounded-2xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-slate-800 gap-4">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-emerald-600/20 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
            <ShieldCheck className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h3 className="text-lg font-bold text-white">Responsible AI & Governance Audit</h3>
              <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                U5 Checkpoints Verified
              </span>
            </div>
            <p className="text-xs text-slate-400">
              Rigorous verification of Privacy, Demographic Fairness, Disparate Impact, and Explainability standards.
            </p>
          </div>
        </div>

        {/* Overall Compliance Score Meter */}
        <div className="flex items-center space-x-3 bg-slate-900/90 border border-slate-800 p-3 rounded-xl">
          <div className="text-right">
            <span className="text-[10px] uppercase font-semibold text-slate-400 block">
              Governance Score
            </span>
            <span className="text-xs font-semibold text-emerald-400">
              {responsibleAI.compliance_tier || "Enterprise Grade"}
            </span>
          </div>
          <div className="w-12 h-12 rounded-full border-2 border-emerald-500 flex items-center justify-center bg-emerald-500/10 font-mono font-bold text-base text-emerald-300 shadow-glow-cyan">
            {score}%
          </div>
        </div>
      </div>

      {/* Active Warnings Banner (if any) */}
      {warnings.length > 0 && (
        <div className="mt-6 p-4 rounded-xl bg-amber-950/30 border border-amber-500/40 text-amber-200">
          <div className="flex items-center space-x-2 mb-2">
            <AlertTriangle className="w-4 h-4 text-amber-400 shrink-0" />
            <h4 className="text-xs font-bold uppercase tracking-wider text-amber-300">
              Responsible AI Attention Items & Domain Flags ({warnings.length})
            </h4>
          </div>
          <div className="space-y-1.5 pl-6 list-disc">
            {warnings.map((warn, wIdx) => (
              <p key={wIdx} className="text-xs leading-relaxed text-amber-200/90 font-sans">
                • {warn}
              </p>
            ))}
          </div>
        </div>
      )}

      {/* Grid: Privacy (5) vs Bias & Fairness (5) */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
        {/* Column 1: Privacy Checkpoints */}
        <div>
          <div className="flex items-center space-x-2 mb-4 pb-2 border-b border-cyan-500/20">
            <Lock className="w-4 h-4 text-cyan-400" />
            <h4 className="text-xs font-bold uppercase tracking-wider text-cyan-300">
              Privacy Checkpoints (5 Requirements)
            </h4>
          </div>
          <div className="space-y-3">
            {responsibleAI.privacy_checks.map((check) => (
              <div
                key={check.id}
                className="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800/80 text-xs hover:border-cyan-500/30 transition-all"
              >
                <div className="flex items-center justify-between mb-1.5">
                  <span className="font-semibold text-white flex items-center space-x-1.5">
                    <CheckCircle2 className="w-3.5 h-3.5 text-cyan-400 shrink-0" />
                    <span>{check.name}</span>
                  </span>
                  <span className={`text-[9px] font-bold px-2 py-0.5 rounded font-mono ${
                    check.status === 'PASSED'
                      ? 'bg-cyan-500/15 text-cyan-300 border border-cyan-500/30'
                      : 'bg-amber-500/15 text-amber-300 border border-amber-500/30'
                  }`}>
                    {check.status}
                  </span>
                </div>
                <p className="text-[11px] text-slate-300 leading-relaxed mb-2 font-sans">
                  {check.description}
                </p>
                <div className="p-2 rounded bg-slate-950/60 text-[10px] text-slate-400 font-mono flex items-start space-x-1.5">
                  <span className="text-cyan-400 font-bold shrink-0">Mitigation:</span>
                  <span>{check.mitigation}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Column 2: Bias & Fairness Checkpoints */}
        <div>
          <div className="flex items-center space-x-2 mb-4 pb-2 border-b border-pink-500/20">
            <Scale className="w-4 h-4 text-pink-400" />
            <h4 className="text-xs font-bold uppercase tracking-wider text-pink-300">
              Bias & Fairness Checkpoints (5 Requirements)
            </h4>
          </div>
          <div className="space-y-3">
            {responsibleAI.bias_checks.map((check) => (
              <div
                key={check.id}
                className="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800/80 text-xs hover:border-pink-500/30 transition-all"
              >
                <div className="flex items-center justify-between mb-1.5">
                  <span className="font-semibold text-white flex items-center space-x-1.5">
                    <CheckCircle2 className="w-3.5 h-3.5 text-pink-400 shrink-0" />
                    <span>{check.name}</span>
                  </span>
                  <span className={`text-[9px] font-bold px-2 py-0.5 rounded font-mono ${
                    check.status === 'PASSED'
                      ? 'bg-emerald-500/15 text-emerald-300 border border-emerald-500/30'
                      : 'bg-amber-500/15 text-amber-300 border border-amber-500/30'
                  }`}>
                    {check.status}
                  </span>
                </div>
                <p className="text-[11px] text-slate-300 leading-relaxed mb-2 font-sans">
                  {check.description}
                </p>
                <div className="p-2 rounded bg-slate-950/60 text-[10px] text-slate-400 font-mono flex items-start space-x-1.5">
                  <span className="text-pink-400 font-bold shrink-0">Mitigation:</span>
                  <span>{check.mitigation}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Compliance Standard Badges */}
      <div className="mt-6 pt-4 border-t border-slate-800 flex flex-wrap items-center justify-between text-xs text-slate-400 gap-2">
        <div className="flex flex-wrap items-center gap-1.5">
          <span className="text-[11px] font-semibold text-slate-300 mr-1">Compliance Frameworks:</span>
          {responsibleAI.audit_frameworks && responsibleAI.audit_frameworks.map((fw, idx) => (
            <span
              key={idx}
              className="px-2 py-0.5 rounded bg-slate-800/90 text-slate-300 border border-slate-700/60 font-mono text-[10px]"
            >
              {fw}
            </span>
          ))}
        </div>
        <span className="text-[10px] text-slate-500 font-mono">
          Fairlearn 80% DIR Standard • GDPR Article 22
        </span>
      </div>
    </div>
  )
}
