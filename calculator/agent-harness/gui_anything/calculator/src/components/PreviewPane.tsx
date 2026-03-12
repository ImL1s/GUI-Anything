import { Terminal, Clock } from 'lucide-react';

type ActionResult = {
  action: string;
  params: Record<string, unknown>;
  result: unknown;
  timestamp: string;
};

type Props = {
  result: unknown;
  history: ActionResult[];
};

export function PreviewPane({ result, history }: Props) {
  return (
    <div className="preview-pane">
      <div className="preview-section">
        <div className="preview-header">
          <Terminal size={16} />
          <span>Output</span>
        </div>
        <div className="preview-output">
          {result !== null ? (
            <pre>{typeof result === 'string' ? result : JSON.stringify(result, null, 2)}</pre>
          ) : (
            <p className="placeholder">Run an action to see results here</p>
          )}
        </div>
      </div>

      <div className="preview-section">
        <div className="preview-header">
          <Clock size={16} />
          <span>History ({history.length})</span>
        </div>
        <div className="history-list">
          {history.length === 0 ? (
            <p className="placeholder">No actions executed yet</p>
          ) : (
            history.slice(0, 20).map((entry, i) => (
              <div key={i} className="history-entry">
                <span className="history-action">{entry.action}</span>
                <span className="history-time">
                  {new Date(entry.timestamp).toLocaleTimeString()}
                </span>
                <code className="history-result">
                  {typeof entry.result === 'string'
                    ? entry.result
                    : JSON.stringify(entry.result)}
                </code>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
