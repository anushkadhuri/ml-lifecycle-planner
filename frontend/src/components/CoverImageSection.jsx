import React, { useState } from 'react'
import { Image as ImageIcon, Download, Sparkles, Maximize2, Minimize2 } from 'lucide-react'

export default function CoverImageSection({ coverImage, projectSpec, onDownloadImage }) {
  const [downloading, setDownloading] = useState(false)
  const [zoomed, setZoomed] = useState(false)

  if (!coverImage || !coverImage.data_uri) return null

  const handleDownload = async () => {
    setDownloading(true)
    try {
      await onDownloadImage()
    } finally {
      setDownloading(false)
    }
  }

  return (
    <div className="glass-panel rounded-2xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-5 border-b border-slate-800 gap-4">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-purple-600/20 border border-purple-500/30 flex items-center justify-center text-purple-400">
            <ImageIcon className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h3 className="text-lg font-bold text-white">AI Project Cover Banner</h3>
              <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-purple-500/20 text-purple-300 border border-purple-500/30">
                U4 AI Art Synthesis
              </span>
            </div>
            <p className="text-xs text-slate-400">
              Cybernetic neural banner with glowing nodes, synapses, project title, and domain tags.
            </p>
          </div>
        </div>

        {/* Download Button */}
        <button
          onClick={handleDownload}
          disabled={downloading}
          className="px-6 py-2.5 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-bold text-xs tracking-wider transition-all shadow-glow-purple flex items-center justify-center space-x-2 active:scale-95 disabled:opacity-50"
        >
          {downloading ? (
            <span>Downloading...</span>
          ) : (
            <>
              <Download className="w-4 h-4" />
              <span>Download Cover Image (.png)</span>
            </>
          )}
        </button>
      </div>

      {/* Banner Preview Card */}
      <div className="mt-6 relative rounded-xl overflow-hidden border border-slate-800 bg-slate-950/70 group">
        <img
          src={coverImage.data_uri}
          alt={projectSpec?.title || "AI Project Banner"}
          className="w-full h-auto object-cover max-h-[460px] rounded-xl shadow-2xl transition-transform duration-300 group-hover:scale-[1.01]"
        />

        {/* Hover overlay with zoom button */}
        <div className="absolute inset-0 bg-slate-950/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center pointer-events-none">
          <span className="px-4 py-2 rounded-lg bg-slate-900/90 text-white text-xs font-medium border border-slate-700 shadow-lg flex items-center space-x-1.5 pointer-events-auto cursor-pointer"
            onClick={() => setZoomed(true)}>
            <Maximize2 className="w-4 h-4 text-purple-400" />
            <span>View Full Resolution (1200x630)</span>
          </span>
        </div>
      </div>

      {/* Metadata Pills */}
      <div className="mt-4 pt-3 border-t border-slate-800/80 flex flex-wrap items-center justify-between text-xs text-slate-400 gap-2">
        <div className="flex items-center space-x-3">
          <span className="font-mono text-[11px] text-purple-300 bg-purple-500/10 px-2 py-0.5 rounded border border-purple-500/20">
            Dimensions: 1200 x 630 px
          </span>
          <span className="font-mono text-[11px] text-blue-300 bg-blue-500/10 px-2 py-0.5 rounded border border-blue-500/20">
            Format: PNG (Lossless)
          </span>
          <span className="text-[11px] text-slate-400 hidden sm:inline">
            Theme: {coverImage.theme || 'Deep Navy & Cyber Purple'}
          </span>
        </div>
        <span className="text-[10px] text-slate-500">
          Generated via Autonomous Neural Canvas Synthesis Engine
        </span>
      </div>

      {/* Zoom Modal */}
      {zoomed && (
        <div
          className="fixed inset-0 z-50 bg-black/90 backdrop-blur-sm flex items-center justify-center p-4 cursor-pointer"
          onClick={() => setZoomed(false)}
        >
          <div className="relative max-w-5xl w-full">
            <button
              onClick={() => setZoomed(false)}
              className="absolute -top-10 right-0 text-white hover:text-purple-400 text-sm font-semibold flex items-center space-x-1"
            >
              <Minimize2 className="w-4 h-4" />
              <span>Close</span>
            </button>
            <img
              src={coverImage.data_uri}
              alt={projectSpec?.title}
              className="w-full h-auto rounded-xl border border-purple-500/40 shadow-2xl"
            />
          </div>
        </div>
      )}
    </div>
  )
}
