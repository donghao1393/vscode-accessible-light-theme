# VS Code Accessible Light Theme - 测试和构建工具

.PHONY: help test test-accessibility test-contrast test-colorblind build clean install

# 默认目标
help:
	@echo "VS Code Accessible Light Theme - 可用命令:"
	@echo ""
	@echo "测试命令:"
	@echo "  make test              - 运行所有测试"
	@echo "  make test-accessibility - 运行完整的无障碍性测试"
	@echo "  make test-contrast     - 运行快速对比度检查"
	@echo "  make test-colorblind   - 运行色盲模拟测试"
	@echo ""
	@echo "构建命令:"
	@echo "  make build             - 构建VSIX包"
	@echo "  make install           - 安装到VS Code"
	@echo "  make clean             - 清理构建文件"
	@echo ""
	@echo "开发命令:"
	@echo "  make check-color COLOR1 COLOR2  - 检查两个颜色的对比度"
	@echo "  make preview           - 在浏览器中预览主题"

# 运行所有测试
test: test-accessibility test-contrast test-colorblind
	@echo "✅ 所有测试完成"

# 完整的无障碍性测试
test-accessibility:
	@echo "🔍 运行无障碍性测试..."
	@python3 scripts/accessibility-test.py

# 快速对比度检查
test-contrast:
	@echo "🎨 运行对比度检查..."
	@python3 scripts/quick-contrast-check.py

# 色盲模拟测试
test-colorblind:
	@echo "👁️ 运行色盲模拟测试..."
	@python3 scripts/colorblind-simulation.py

# 检查特定颜色对的对比度
check-color:
	@if [ -z "$(COLOR1)" ] || [ -z "$(COLOR2)" ]; then \
		echo "用法: make check-color COLOR1=#ff0000 COLOR2=#ffffff"; \
	else \
		python3 scripts/quick-contrast-check.py $(COLOR1) $(COLOR2); \
	fi

# 构建VSIX包
build:
	@echo "📦 构建VSIX包..."
	@if command -v vsce >/dev/null 2>&1; then \
		vsce package; \
		echo "✅ VSIX包构建完成"; \
	else \
		echo "❌ 请先安装vsce: npm install -g vsce"; \
	fi

# 安装到VS Code
install: build
	@echo "🚀 安装到VS Code..."
	@VSIX_FILE=$$(ls -t *.vsix 2>/dev/null | head -n1); \
	if [ -n "$$VSIX_FILE" ]; then \
		code --install-extension "$$VSIX_FILE"; \
		echo "✅ 主题已安装到VS Code"; \
	else \
		echo "❌ 找不到VSIX文件，请先运行 make build"; \
	fi

# 清理构建文件
clean:
	@echo "🧹 清理构建文件..."
	@rm -f *.vsix
	@echo "✅ 清理完成"

# 在浏览器中预览主题
preview:
	@echo "🌐 在浏览器中预览主题..."
	@if command -v open >/dev/null 2>&1; then \
		open preview.html; \
	elif command -v xdg-open >/dev/null 2>&1; then \
		xdg-open preview.html; \
	else \
		echo "请手动打开 preview.html 文件"; \
	fi

# 验证主题JSON格式
validate:
	@echo "✅ 验证主题JSON格式..."
	@python3 -m json.tool themes/accessible-light-theme.json > /dev/null && \
		echo "✅ JSON格式正确" || echo "❌ JSON格式错误"

# 生成颜色报告
color-report:
	@echo "📊 生成颜色使用报告..."
	@python3 -c "
import json
with open('themes/accessible-light-theme.json', 'r') as f:
    theme = json.load(f)

colors = set()
if 'colors' in theme:
    for v in theme['colors'].values():
        if isinstance(v, str) and v.startswith('#'):
            colors.add(v)

if 'tokenColors' in theme:
    for token in theme['tokenColors']:
        if 'settings' in token and 'foreground' in token['settings']:
            fg = token['settings']['foreground']
            if isinstance(fg, str) and fg.startswith('#'):
                colors.add(fg)

print(f'主题中使用的颜色总数: {len(colors)}')
for color in sorted(colors):
    print(f'  {color}')
"
