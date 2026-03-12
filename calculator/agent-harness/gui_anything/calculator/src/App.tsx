import { useState, useCallback } from 'react';
import schema from '../gui-schema.json';
import { A2UIRenderer } from './components/A2UIRenderer';
import { ActionPanel } from './components/ActionPanel';
import { PreviewPane } from './components/PreviewPane';
import { StatusBar } from './components/StatusBar';

type ActionResult = {
  action: string;
  params: Record<string, unknown>;
  result: unknown;
  timestamp: string;
};

const groups = schema.surfaces[0].components[0].items;

export function App() {
  const [activeGroup, setActiveGroup] = useState(groups[0].id);
  const [results, setResults] = useState<ActionResult[]>([]);
  const [lastResult, setLastResult] = useState<unknown>(null);

  const handleAction = useCallback(
    (actionId: string, params: Record<string, unknown>) => {
      // In a real harness, this dispatches to the Python backend.
      // For the reference example, we simulate with a local result.
      const action = schema.actions[actionId as keyof typeof schema.actions];
      const entry: ActionResult = {
        action: action?.label ?? actionId,
        params,
        result: `[simulated] ${actionId}(${JSON.stringify(params)})`,
        timestamp: new Date().toISOString(),
      };
      setResults((prev) => [entry, ...prev]);
      setLastResult(entry.result);
    },
    [],
  );

  const groupActions = Object.entries(schema.actions).filter(
    ([, v]) => v.group === activeGroup,
  );

  return (
    <div className="app-layout">
      <A2UIRenderer
        groups={groups}
        activeGroup={activeGroup}
        onGroupChange={setActiveGroup}
      />
      <main className="main-content">
        <header className="main-header">
          <h1>{groups.find((g) => g.id === activeGroup)?.label ?? 'Calculator'}</h1>
          <span className="badge">{groupActions.length} actions</span>
        </header>
        <div className="content-area">
          <ActionPanel
            actions={groupActions}
            onSubmit={handleAction}
          />
          <PreviewPane result={lastResult} history={results} />
        </div>
      </main>
      <StatusBar
        lastResult={lastResult}
        historyCount={results.length}
        activeGroup={activeGroup}
      />
    </div>
  );
}
