# Change Log

All notable changes to the "vscode-accessible-light-theme" extension will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-01-26

### Added
- **WCAG AA Compliance**: All colors now meet 4.5:1 contrast ratio requirements
- **Enhanced Font Styles**: Added bold, italic, and underline styles for better syntax differentiation
- **Comprehensive Testing Suite**:
  - Automated contrast ratio checking
  - Color-blind simulation testing
  - Quick validation tools
- **Build System**: Makefile with testing and build commands
- **Accessibility Documentation**: Detailed usage guide for different visual conditions

### Changed
- **Color Updates for Better Contrast**:
  - Green strings: `#059669` → `#047857` (contrast: 3.70 → 5.39)
  - Orange numbers/types: `#d97706` → `#c2410c` (contrast: 3.13 → 5.09)
  - Gray comments: `#7c7c7c` → `#6b7280` (contrast: 4.10 → 4.75)
- **Enhanced Syntax Highlighting**:
  - Type definitions now use underline style
  - Constants and numbers use bold style
  - Variables use italic style for better distinction
- **Updated Documentation**: README with accessibility features and test results

### Fixed
- Color contrast issues that didn't meet accessibility standards
- Insufficient visual cues for color-blind users

## [1.0.0] - 2024-XX-XX

### Added
- Initial release based on Atom One X Github Light Gray theme
- Light theme optimized for accessibility and projector use
- Enhanced red-green contrast
- Built-in bracket pair colorization support
- Terminal integration with consistent colors
- Git integration with clear diff visualization
