# Changelog

## [0.2.0] - 2026-08-12
### Added
- **Design Principles:** Added comprehensive documentation for core design guidelines including Accessibility, Interactivity, Motion, Optimizations, and Touch.
- **Tokens:** Introduced new global JSON token files for `interaction` and `motion`.
- **License:** Added project `LICENSE` file.
### Changed
- **Documentation:** Updated `docs/source/index.rst` and color principles (`docs/source/principles/color.rst`).
- **Flutter Tokens:** Updated `asha_flutter_tokens/lib/src/tokens.dart` to support new definitions.
- **Versioning:** Bumped version to `v0.2.0` in `VERSION`.

## [0.1.9] - 2026-06-30
### Added
- Automated GitHub Release pipeline via `.github/workflows/release.yml`.
- Version tracking system using `VERSION` file in root.
- `requirements.txt` for documentation environment dependencies.
- `CHANGELOG.md` for project history tracking.
### Changed
- Refactored `docs/source/conf.py` to dynamically resolve version from root `VERSION` file.
- Updated `.gitignore` to refine build artifacts and system file exclusions.
