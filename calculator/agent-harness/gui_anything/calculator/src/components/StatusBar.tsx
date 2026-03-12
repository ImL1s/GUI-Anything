import { Activity, Hash, Layers } from 'lucide-react';

type Props = {
  lastResult: unknown;
  historyCount: number;
  activeGroup: string;
};

export function StatusBar({ lastResult, historyCount, activeGroup }: Props) {
  return (
    <footer className="status-bar">
      <div className="status-item">
        <Layers size={14} />
        <span>{activeGroup}</span>
      </div>
      <div className="status-item">
        <Hash size={14} />
        <span>{historyCount} actions</span>
      </div>
      <div className="status-item">
        <Activity size={14} />
        <span>
          {lastResult !== null
            ? String(lastResult).slice(0, 40)
            : 'idle'}
        </span>
      </div>
      <div className="status-agent">
        <span className="agent-dot" />
        <span>MCP Ready</span>
      </div>
    </footer>
  );
}
