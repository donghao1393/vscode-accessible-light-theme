# 贡献指南

感谢您对 Accessible Light Theme 的关注！我们欢迎所有形式的贡献，特别是与无障碍性相关的改进。

## 🎯 贡献原则

### 无障碍优先
- 所有颜色变更必须符合 WCAG 2.1 AA 标准（对比度 ≥ 4.5:1）
- 不能仅依赖颜色传达信息，必须配合字体样式
- 考虑不同类型色盲用户的需求

### 测试驱动
- 所有变更都必须通过自动化测试
- 新功能需要添加相应的测试用例
- 手动测试覆盖主要使用场景

## 🚀 如何贡献

### 报告问题
1. 查看现有的 [Issues](https://github.com/donghao1393/vscode-accessible-light-theme/issues)
2. 使用适当的问题模板：
   - 🐛 [Bug报告](.github/ISSUE_TEMPLATE/bug-report.md)
   - ♿ [无障碍反馈](.github/ISSUE_TEMPLATE/accessibility-feedback.md)
   - 🚀 [功能请求](.github/ISSUE_TEMPLATE/feature-request.md)

### 提交代码
1. Fork 这个仓库
2. 创建功能分支：`git checkout -b feature/your-feature-name`
3. 进行更改并确保通过测试
4. 提交更改：`git commit -m "feat: your feature description"`
5. 推送到分支：`git push origin feature/your-feature-name`
6. 创建 Pull Request

## 🧪 开发环境设置

### 必需工具
- Python 3.x（用于运行测试脚本）
- Node.js 和 npm（用于构建VSIX包）
- VS Code（用于测试主题效果）

### 安装依赖
```bash
# 安装vsce用于构建
npm install -g vsce

# 克隆仓库
git clone https://github.com/donghao1393/vscode-accessible-light-theme.git
cd vscode-accessible-light-theme

# 运行测试
make test
```

## 🎨 颜色变更指南

### 修改颜色前
1. 运行当前测试：`make test-contrast`
2. 记录当前对比度值
3. 确定变更原因和目标

### 修改颜色
1. 编辑 `themes/accessible-light-theme.json`
2. 同时更新相关的UI颜色（终端、Git装饰等）
3. 考虑字体样式的配合

### 验证变更
```bash
# 检查新的对比度
make test-contrast

# 运行色盲模拟测试
make test-colorblind

# 运行完整测试套件
make test
```

### 更新文档
- 更新 README.md 中的颜色表格
- 更新 CHANGELOG.md
- 如有必要，更新 ACCESSIBILITY.md

## 📝 提交信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### 类型
- `feat`: 新功能
- `fix`: 修复问题
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

### 范围
- `accessibility`: 无障碍相关
- `colors`: 颜色变更
- `fonts`: 字体样式
- `ui`: UI元素
- `docs`: 文档
- `tests`: 测试

### 示例
```
feat(accessibility): 提高字符串颜色对比度

将字符串颜色从 #059669 更改为 #047857，
对比度从 3.70:1 提升到 5.39:1，符合 WCAG AA 标准。

Closes #123
```

## 🔍 代码审查

### Pull Request 要求
- [ ] 通过所有自动化测试
- [ ] 包含适当的测试用例
- [ ] 更新相关文档
- [ ] 遵循提交信息规范
- [ ] 描述清晰，包含变更原因

### 审查重点
1. **无障碍性**：是否符合WCAG标准
2. **一致性**：与现有设计的协调性
3. **兼容性**：不同环境下的表现
4. **测试覆盖**：是否有足够的测试

## 🏷️ 发布流程

### 版本号规则
遵循 [Semantic Versioning](https://semver.org/)：
- `MAJOR`: 不兼容的API变更
- `MINOR`: 向后兼容的功能性新增
- `PATCH`: 向后兼容的问题修正

### 发布步骤
1. 更新版本号和CHANGELOG
2. 运行完整测试套件
3. 执行发布前检查清单
4. 创建GitHub Release
5. 发布到VS Code Marketplace

## 🤝 社区准则

### 行为准则
- 尊重所有贡献者
- 建设性的反馈和讨论
- 专注于改进用户体验
- 优先考虑无障碍需求

### 沟通渠道
- GitHub Issues：问题报告和功能请求
- GitHub Discussions：一般讨论和问答
- Pull Request：代码审查和讨论

## 📚 学习资源

### 无障碍性
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Color Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)

### VS Code主题开发
- [VS Code Theme Guide](https://code.visualstudio.com/api/extension-guides/color-theme)
- [Theme Color Reference](https://code.visualstudio.com/api/references/theme-color)

感谢您的贡献！让我们一起为所有开发者创造更好的编程体验。
