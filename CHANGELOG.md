# Changelog

## [0.1.9] - 2026-06-30
### Added
- Automated GitHub Release pipeline via `.github/workflows/release.yml`.
- Version tracking system using `VERSION` file in root.
- `requirements.txt` for documentation environment dependencies.
- `CHANGELOG.md` for project history tracking.

### Changed
- Refactored `docs/source/conf.py` to dynamically resolve version from root `VERSION` file.
- Updated `.gitignore` to refine build artifacts and system file exclusions.
