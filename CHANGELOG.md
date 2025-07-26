# Change Log

All notable changes to the "Clean Light Theme" extension will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-07-26

### Added
- **Modern Development Infrastructure**: Rust-based toolchain with Just + uv + pytest
- **Professional Project Structure**: Organized assets into `assets/docs/`, `assets/icons/`, `assets/preview/`
- **New Minimalist Icon**: Clean "A" design with theme accent color (SVG + PNG)
- **Enhanced Testing**: 8 automated accessibility tests, all passing
- **Interactive Preview**: Updated preview.html with accurate theme colors

### Changed
- **Project Branding**: Repositioned from "Accessible Light Theme" to "Clean Light Theme"
- **README Rewrite**: Developer-friendly messaging with honest, direct communication
- **File Organization**: Moved all documentation and assets to organized subdirectories
- **Build System**: Replaced broken Makefile with modern Just-based workflow

### Fixed
- **WCAG AA Compliance**: Fixed color contrast issues from v1.0.0
  - Green strings: `#059669` → `#047857` (contrast: 3.70 → 5.39)
  - Orange numbers/types: `#d97706` → `#c2410c` (contrast: 3.13 → 5.09)
  - Gray comments: `#7c7c7c` → `#6b7280` (contrast: 4.10 → 4.75)
- **Color Accuracy**: Fixed all color mismatches between preview and actual theme
- **JSON Validation**: Cleaned theme file, removed all comments and errors
- **Documentation**: Updated all links and references to new file locations

## [1.0.0] - 2025-07-25

### Added
- **Initial Accessible Light Theme**: Clean light theme with accessibility focus
- **Enhanced Font Styles**: Bold, italic, and underline styles for better syntax differentiation
- **Multi-language Support**: Syntax highlighting for JavaScript, Python, HTML, CSS, Markdown
- **Terminal Integration**: Consistent color scheme in integrated terminal
- **Git Integration**: Enhanced diff view and git decoration colors

### Features
- Light color scheme optimized for readability
- Font style differentiation beyond just color
- Support for major programming languages
- Clean, minimal design approach


