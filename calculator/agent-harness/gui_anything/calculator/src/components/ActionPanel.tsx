import { useState, useCallback, type FormEvent } from 'react';
import { Play, AlertTriangle } from 'lucide-react';

type Param = {
  name: string;
  type: string;
  label: string;
  required?: boolean;
  default?: string;
  options?: string[];
};

type ActionEntry = [
  string,
  {
    label: string;
    description: string;
    params: Param[];
    confirm?: boolean;
  },
];

type Props = {
  actions: ActionEntry[];
  onSubmit: (actionId: string, params: Record<string, unknown>) => void;
};

export function ActionPanel({ actions, onSubmit }: Props) {
  const [formValues, setFormValues] = useState<Record<string, string>>({});

  const handleChange = useCallback((key: string, value: string) => {
    setFormValues((prev) => ({ ...prev, [key]: value }));
  }, []);

  const handleSubmit = useCallback(
    (e: FormEvent, actionId: string, params: Param[], needsConfirm?: boolean) => {
      e.preventDefault();
      if (needsConfirm && !window.confirm('Are you sure?')) return;

      const parsed: Record<string, unknown> = {};
      for (const p of params) {
        const raw = formValues[`${actionId}.${p.name}`] ?? p.default ?? '';
        if (p.type === 'number') parsed[p.name] = Number(raw);
        else parsed[p.name] = raw;
      }
      onSubmit(actionId, parsed);
    },
    [formValues, onSubmit],
  );

  if (actions.length === 0) {
    return <div className="empty-state">No actions in this group</div>;
  }

  return (
    <div className="action-panel">
      {actions.map(([id, action]) => (
        <form
          key={id}
          className="action-card"
          onSubmit={(e) => handleSubmit(e, id, action.params, action.confirm)}
        >
          <div className="action-header">
            <h3>{action.label}</h3>
            <p className="action-desc">{action.description}</p>
          </div>
          <div className="action-fields">
            {action.params.map((p) => {
              const fieldKey = `${id}.${p.name}`;
              if (p.type === 'select' && p.options) {
                return (
                  <label key={fieldKey} className="field">
                    <span className="field-label">{p.label}</span>
                    <select
                      value={formValues[fieldKey] ?? p.default ?? ''}
                      onChange={(e) => handleChange(fieldKey, e.target.value)}
                    >
                      {p.options.map((opt) => (
                        <option key={opt} value={opt}>
                          {opt}
                        </option>
                      ))}
                    </select>
                  </label>
                );
              }
              return (
                <label key={fieldKey} className="field">
                  <span className="field-label">{p.label}</span>
                  <input
                    type={p.type === 'number' ? 'number' : 'text'}
                    placeholder={p.label}
                    value={formValues[fieldKey] ?? ''}
                    onChange={(e) => handleChange(fieldKey, e.target.value)}
                    required={p.required}
                    step={p.type === 'number' ? 'any' : undefined}
                  />
                </label>
              );
            })}
          </div>
          <button type="submit" className="btn-primary">
            {action.confirm && <AlertTriangle size={16} />}
            <Play size={16} />
            <span>Run {action.label}</span>
          </button>
        </form>
      ))}
    </div>
  );
}
