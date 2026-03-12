import {
  Calculator,
  FlaskConical,
  Brain,
  Clock,
  Download,
} from 'lucide-react';

type Group = { id: string; label: string; icon: string };

const iconMap: Record<string, React.ComponentType<{ size?: number }>> = {
  calculator: Calculator,
  'flask-conical': FlaskConical,
  brain: Brain,
  clock: Clock,
  download: Download,
};

type Props = {
  groups: Group[];
  activeGroup: string;
  onGroupChange: (id: string) => void;
};

export function A2UIRenderer({ groups, activeGroup, onGroupChange }: Props) {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <Calculator size={28} />
        <span>Calculator</span>
      </div>
      <nav className="sidebar-nav">
        {groups.map((g) => {
          const Icon = iconMap[g.icon] ?? Calculator;
          const isActive = g.id === activeGroup;
          return (
            <button
              key={g.id}
              className={`nav-item ${isActive ? 'active' : ''}`}
              onClick={() => onGroupChange(g.id)}
              aria-current={isActive ? 'page' : undefined}
            >
              <Icon size={20} />
              <span>{g.label}</span>
            </button>
          );
        })}
      </nav>
      <div className="sidebar-footer">
        <span className="version">GUI-Anything v1.0</span>
      </div>
    </aside>
  );
}
