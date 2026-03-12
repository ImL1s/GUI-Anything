# Publishing GUI-Anything Plugin

## Claude Code Plugin Marketplace

### Prerequisites

1. All files pass `verify-plugin.sh`
2. README.md is up to date
3. HARNESS.md reflects current methodology

### Publishing Steps

1. **Verify plugin structure:**
   ```bash
   cd gui-anything-plugin
   bash verify-plugin.sh
   ```

2. **Ensure marketplace.json is correct:**
   ```bash
   cat ../.claude-plugin/marketplace.json
   ```

3. **Push to GitHub:**
   ```bash
   git add -A && git commit -m "release: gui-anything plugin vX.Y.Z" && git push
   ```

4. **Register with Claude marketplace:**
   The plugin is auto-discovered from `.claude-plugin/marketplace.json` when the repository is added.

## Codex Skill

### Install locally:
```bash
cd codex-skill
bash scripts/install.sh
```

### Verify:
```bash
ls "${CODEX_HOME:-$HOME/.codex}/skills/gui-anything/"
```

## OpenCode

Copy `opencode-commands/*.md` to your OpenCode commands directory.

## Version Checklist

- [ ] Update version in plugin.json
- [ ] Update HARNESS.md if methodology changed
- [ ] Run `verify-plugin.sh` — all checks pass
- [ ] Update QUICKSTART.md if workflow changed
- [ ] Tag release: `git tag vX.Y.Z && git push --tags`
