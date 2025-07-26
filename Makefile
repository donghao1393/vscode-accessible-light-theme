.PHONY: help test build clean

help:
	@echo "Accessible Light Theme - Available Commands:"
	@echo ""
	@echo "  make test    - Test theme colors for accessibility"
	@echo "  make build   - Build VSIX package"
	@echo "  make clean   - Clean build files"
	@echo ""

test:
	@echo "🎨 Testing theme accessibility..."
	@python3 test_theme.py

build:
	@echo "📦 Building VSIX package..."
	@if command -v vsce >/dev/null 2>&1; then \
		vsce package; \
		echo "✅ Package built successfully"; \
	else \
		echo "❌ vsce not found. Install with: npm install -g vsce"; \
	fi

clean:
	@echo "🧹 Cleaning build files..."
	@rm -f *.vsix
	@echo "✅ Clean complete"
