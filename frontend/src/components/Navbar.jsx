import React from 'react'
import { Cpu, Sparkles, BookOpen, ShieldCheck, CheckCircle2 } from 'lucide-react'

export default function Navbar({ onSelectDemo, backendStatus }) {
  return (
    <header className="sticky top-0 z-50 border-b border-slate-800/80 bg-[#070b19]/90 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand */}
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-purple-600 via-indigo-600 to-blue-500 p-0.5 shadow-glow-purple flex items-center justify-center">
            <div className="w-full h-full bg-[#0c1228] rounded-[10px] flex items-center justify-center">
              <Cpu className="w-5 h-5 text-purple-400" />
            </div>
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="font-bold text-lg tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-400 bg-clip-text text-transparent">
                ML/DL Lifecycle Planner
              </span>
              <span className="text-[11px] font-semibold uppercase tracking-wider px-2 py-0.5 rounded-full bg-purple-500/10 text-purple-400 border border-purple-500/20">
                v2.4 AI Engine
              </span>
            </div>
            <p className="text-xs text-slate-400 hidden sm:block">
              AI-Powered Project Planning & Architecture Roadmap
            </p>
          </div>
        </div>

        {/* Status & Quick Demos */}
        <div className="flex items-center space-x-3">
          {/* Status Badge */}
          <div className="hidden md:flex items-center space-x-2 px-3 py-1 rounded-full bg-slate-800/60 border border-slate-700/60 text-xs text-slate-300">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>API: Connected</span>
            <span className="text-slate-600">|</span>
            <span className="text-purple-300">S-BERT & T5 Active</span>
          </div>

          {/* Quick Demo Buttons */}
          <button
            onClick={() => onSelectDemo('student_performance')}
            className="px-3 py-1.5 text-xs font-medium rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-500/30 transition-all flex items-center space-x-1.5"
            title="Load Student Performance Prediction (ML)"
          >
            <span>📚 ML Demo</span>
          </button>

          <button
            onClick={() => onSelectDemo('iot_intrusion_detection')}
            className="px-3 py-1.5 text-xs font-medium rounded-lg bg-purple-600/20 hover:bg-purple-600/30 text-purple-300 border border-purple-500/30 transition-all flex items-center space-x-1.5"
            title="Load IoT Network Intrusion Detection (DL)"
          >
            <span>🛡️ DL Demo</span>
          </button>
        </div>
      </div>
    </header>
  )
}
