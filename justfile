# Accessible Light Theme - Modern task runner using Just + uv

# Show available commands
default:
    @just --list

# Test theme accessibility compliance
test:
    @echo "🎨 Testing theme accessibility..."
    uv run pytest tests/ -v

# Test with detailed output and coverage
test-verbose:
    @echo "🔍 Running detailed accessibility tests..."
    uv run pytest tests/ -v --tb=short

# Build VSIX package for VS Code
build:
    @echo "📦 Building VSIX package..."
    @if command -v vsce >/dev/null 2>&1; then \
        vsce package; \
        echo "✅ Package built successfully"; \
    else \
        echo "❌ vsce not found. Install with: npm install -g vsce"; \
    fi

# Install Python dependencies using uv
install:
    @echo "📥 Installing dependencies..."
    uv sync

# Clean build artifacts
clean:
    @echo "🧹 Cleaning build files..."
    @rm -f *.vsix
    @echo "✅ Clean complete"

# Validate theme JSON format
validate:
    @echo "✅ Validating theme JSON..."
    @python3 -m json.tool themes/accessible-light-theme.json > /dev/null && \
        echo "✅ Theme JSON is valid" || echo "❌ Theme JSON is invalid"

# Quick contrast check for main colors
quick-test:
    @echo "⚡ Quick accessibility check..."
    uv run python tests/test_accessibility.py
