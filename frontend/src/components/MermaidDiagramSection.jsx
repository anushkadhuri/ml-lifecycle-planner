import React, { useEffect, useRef, useState } from 'react'
import mermaid from 'mermaid'
import {
  GitFork,
  Download,
  Copy,
  Check,
  Code,
  ZoomIn,
  ZoomOut,
  Maximize2,
  Minimize2,
  RotateCcw
} from 'lucide-react'

// Initialize mermaid
mermaid.initialize({
  startOnLoad: false,
  theme: 'dark',
  themeVariables: {
    darkMode: true,
    background: '#0c1228',
    primaryColor: '#172247',
    primaryTextColor: '#f8fafc',
    primaryBorderColor: '#7c3aed',
    lineColor: '#60a5fa',
    secondaryColor: '#07242c',
    tertiaryColor: '#2d123d'
  },
  flowchart: {
    useMaxWidth: true,
    htmlLabels: true,
    curve: 'basis'
  }
})

export default function MermaidDiagramSection({ mermaidData, projectTitle }) {
  const [copied, setCopied] = useState(false)
  const [showCode, setShowCode] = useState(false)
  const [isFullScreen, setIsFullScreen] = useState(false)
  const [zoomLevel, setZoomLevel] = useState(1)
  const [svgContent, setSvgContent] = useState('')
  const [renderError, setRenderError] = useState(null)
  const containerRef = useRef(null)

  const mermaidCode = mermaidData?.mermaid_code || ''

  useEffect(() => {
    let isMounted = true

    const renderChart = async () => {
      if (!mermaidCode) return
      setRenderError(null)
      try {
        const uniqueId = `mermaid-svg-${Date.now()}`
        const { svg } = await mermaid.render(uniqueId, mermaidCode)
        if (isMounted) {
          setSvgContent(svg)
        }
      } catch (err) {
        console.error('Mermaid render error:', err)
        if (isMounted) {
          setRenderError('Could not render SVG directly. Code view available below.')
        }
      }
    }

    renderChart()
    return () => {
      isMounted = false
    }
  }, [mermaidCode])

  const handleCopy = () => {
    navigator.clipboard.writeText(mermaidCode)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  const handleDownloadSVG = () => {
    if (!svgContent) return
    const blob = new Blob([svgContent], { type: 'image/svg+xml;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `${(projectTitle || 'ml_lifecycle').replace(/\s+/g, '_').toLowerCase()}_workflow.svg`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    URL.revokeObjectURL(url)
  }

  const handleZoomIn = () => setZoomLevel((z) => Math.min(2.0, z + 0.15))
  const handleZoomOut = () => setZoomLevel((z) => Math.max(0.6, z - 0.15))
  const handleResetZoom = () => setZoomLevel(1)

  return (
    <div className={`glass-panel rounded-2xl p-6 sm:p-8 border border-slate-700/60 shadow-xl transition-all ${
      isFullScreen ? 'fixed inset-4 z-50 overflow-auto bg-[#070b19]/98 p-8' : ''
    }`}>
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-5 border-b border-slate-800 gap-4">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center text-indigo-400">
            <GitFork className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h3 className="text-lg font-bold text-white">Mermaid Lifecycle Workflow Diagram</h3>
              <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                U1 & U5 Integrated
              </span>
            </div>
            <p className="text-xs text-slate-400">
              Interactive 11-stage pipeline with embedded Responsible AI (Privacy & Bias) checkpoint subgraphs.
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex flex-wrap items-center gap-2">
          {/* Zoom controls */}
          <div className="flex items-center bg-slate-900 border border-slate-800 rounded-lg p-0.5">
            <button
              onClick={handleZoomOut}
              className="p-1.5 text-slate-400 hover:text-white hover:bg-slate-800 rounded"
              title="Zoom Out"
            >
              <ZoomOut className="w-3.5 h-3.5" />
            </button>
            <span className="text-[11px] font-mono text-slate-400 px-2">
              {Math.round(zoomLevel * 100)}%
            </span>
            <button
              onClick={handleZoomIn}
              className="p-1.5 text-slate-400 hover:text-white hover:bg-slate-800 rounded"
              title="Zoom In"
            >
              <ZoomIn className="w-3.5 h-3.5" />
            </button>
            <button
              onClick={handleResetZoom}
              className="p-1.5 text-slate-400 hover:text-white hover:bg-slate-800 rounded ml-0.5"
              title="Reset Zoom"
            >
              <RotateCcw className="w-3.5 h-3.5" />
            </button>
          </div>

          {/* Toggle Code / Diagram */}
          <button
            onClick={() => setShowCode(!showCode)}
            className={`px-3 py-1.5 text-xs rounded-lg border font-medium flex items-center space-x-1.5 transition-all ${
              showCode
                ? 'bg-purple-600/30 border-purple-500 text-purple-200'
                : 'bg-slate-800/80 border-slate-700 text-slate-300 hover:bg-slate-700'
            }`}
          >
            <Code className="w-3.5 h-3.5" />
            <span>{showCode ? 'View Diagram' : 'View Code'}</span>
          </button>

          {/* Copy Code */}
          <button
            onClick={handleCopy}
            className="px-3 py-1.5 text-xs rounded-lg bg-slate-800/80 hover:bg-slate-700 border border-slate-700 text-slate-300 transition-all font-medium flex items-center space-x-1.5"
            title="Copy Mermaid syntax to clipboard"
          >
            {copied ? (
              <>
                <Check className="w-3.5 h-3.5 text-emerald-400" />
                <span className="text-emerald-400 font-semibold">Copied!</span>
              </>
            ) : (
              <>
                <Copy className="w-3.5 h-3.5" />
                <span>Copy Code</span>
              </>
            )}
          </button>

          {/* Download SVG */}
          <button
            onClick={handleDownloadSVG}
            disabled={!svgContent}
            className="px-3 py-1.5 text-xs rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 border border-indigo-500/30 text-indigo-300 transition-all font-medium flex items-center space-x-1.5"
            title="Download Mermaid Diagram as SVG"
          >
            <Download className="w-3.5 h-3.5" />
            <span>Download SVG</span>
          </button>

          {/* Fullscreen Toggle */}
          <button
            onClick={() => setIsFullScreen(!isFullScreen)}
            className="p-1.5 text-slate-400 hover:text-white hover:bg-slate-800 rounded-lg border border-slate-800"
            title={isFullScreen ? 'Exit Full Screen' : 'Full Screen'}
          >
            {isFullScreen ? <Minimize2 className="w-4 h-4" /> : <Maximize2 className="w-4 h-4" />}
          </button>
        </div>
      </div>

      {/* Diagram Canvas / Code View */}
      <div className="mt-6">
        {showCode ? (
          <div className="p-4 rounded-xl bg-slate-950 border border-slate-800 font-mono text-xs text-purple-300 overflow-x-auto max-h-[550px]">
            <pre>{mermaidCode}</pre>
          </div>
        ) : (
          <div className="relative rounded-xl bg-slate-950/70 border border-slate-800/80 p-6 min-h-[420px] flex items-center justify-center overflow-auto">
            {renderError ? (
              <div className="text-center p-6">
                <p className="text-sm text-amber-400 mb-3">{renderError}</p>
                <button
                  onClick={() => setShowCode(true)}
                  className="px-4 py-2 text-xs rounded-lg bg-purple-600 text-white font-medium"
                >
                  View Mermaid Definition
                </button>
              </div>
            ) : svgContent ? (
              <div
                ref={containerRef}
                className="w-full flex justify-center transition-transform duration-200"
                style={{ transform: `scale(${zoomLevel})`, transformOrigin: 'top center' }}
                dangerouslySetInnerHTML={{ __html: svgContent }}
              />
            ) : (
              <div className="flex flex-col items-center justify-center space-y-2 text-slate-400">
                <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500"></div>
                <span className="text-xs">Rendering Flowchart Topology...</span>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Legend */}
      <div className="mt-4 pt-4 border-t border-slate-800 flex flex-wrap items-center justify-between text-xs text-slate-400 gap-3">
        <div className="flex items-center space-x-4">
          <span className="font-semibold text-slate-300">Legend:</span>
          <span className="flex items-center space-x-1.5">
            <span className="w-3 h-3 rounded bg-[#111936] border border-purple-500 inline-block"></span>
            <span>Lifecycle Stages (1-11)</span>
          </span>
          <span className="flex items-center space-x-1.5">
            <span className="w-3 h-3 rounded bg-[#07242c] border border-cyan-400 border-dashed inline-block"></span>
            <span>Privacy Guardrail</span>
          </span>
          <span className="flex items-center space-x-1.5">
            <span className="w-3 h-3 rounded bg-[#2d123d] border border-pink-500 border-dashed inline-block"></span>
            <span>Fairness & Bias Guardrail</span>
          </span>
        </div>
        <span className="text-[11px] text-slate-500">
          Generated automatically with Mermaid.js
        </span>
      </div>
    </div>
  )
}
