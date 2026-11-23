import React from 'react'
import { Cpu, Heart, ShieldCheck, Terminal, Sparkles } from 'lucide-react'

export default function Footer() {
  const techStack = [
    "React 18",
    "Tailwind CSS",
    "Flask / FastAPI",
    "Sentence-BERT",
    "Hugging Face T5",
    "TensorFlow 2",
    "Scikit-Learn",
    "Mermaid.js",
    "nbformat"
  ]

  return (
    <footer className="mt-16 border-t border-slate-800/80 bg-[#070b19] py-10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6">
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 rounded-lg bg-purple-600/20 border border-purple-500/30 flex items-center justify-center text-purple-400">
              <Cpu className="w-4 h-4" />
            </div>
            <div>
              <span className="font-bold text-sm text-white">
                ML/DL Lifecycle Planner
              </span>
              <p className="text-xs text-slate-500">
                AI-Powered Machine Learning and Deep Learning Project Planning System
              </p>
            </div>
          </div>

          {/* Tech Stack Pills */}
          <div className="flex flex-wrap items-center justify-center gap-1.5 max-w-xl">
            {techStack.map((tech, idx) => (
              <span
                key={idx}
                className="text-[10px] px-2 py-0.5 rounded bg-slate-900 border border-slate-800 text-slate-400 font-mono"
              >
                {tech}
              </span>
            ))}
          </div>

          <div className="text-xs text-slate-500 text-center md:text-right">
            <span>Built with Responsible AI Standards</span>
            <div className="flex items-center justify-center md:justify-end space-x-1 mt-0.5 text-purple-400">
              <Sparkles className="w-3 h-3" />
              <span>Full-Stack AI Architecture</span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}
