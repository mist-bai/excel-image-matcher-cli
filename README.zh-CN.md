# Excel 图片匹配 CLI

这是一个可以公开展示的 Python 命令行工具示例，用于把表格行和图片文件按指定字段进行匹配，并输出匹配结果、缺失图片日志、重复图片日志和运行摘要。

这个项目是一个小型但完整的办公自动化案例，适合用于 Fiverr、Contra、Upwork、Guru 等平台展示 Python 自动化能力。

仓库内容是公开安全的：

- 不包含真实客户数据
- 不包含真实商品、订单、价格或公司信息
- 不包含账号、密码、Token 或 API Key
- 示例图片是占位 SVG
- 示例表格是合成数据

## 项目能展示什么

- CSV / Excel 风格的表格处理
- 按指定字段匹配图片文件
- 缺失图片检查
- 重复图片检查
- dry-run 运行模式
- 可重复执行的命令行自动化流程
- 面向非技术用户的交付方式：源码、说明、输入样例、输出日志

## 快速运行

```bash
PYTHONPATH=src python3 -m excel_image_matcher_cli.cli \
  --input examples/input/products.csv \
  --images examples/images \
  --key-column image_key \
  --output-dir outputs
```

运行后会生成：

- `outputs/matched_rows.csv`
- `outputs/missing_images.csv`
- `outputs/duplicate_images.csv`
- `outputs/run_summary.md`

## 示例场景

这个工具可以扩展到以下真实业务场景：

- 产品目录图片匹配
- 检查报告图片整理
- Excel 行数据与附件文件匹配
- 批量图片校验
- 表格数据清洗和输出日志

实际接单时，需要客户提供匿名样例文件、图片命名规则、期望输出格式和异常处理规则。

## 示例数据说明

`examples/` 目录里的表格和图片全部是合成示例。`DEMO-001`、`Demo Item A` 等名称都是占位内容，不对应任何真实客户、产品、订单或公司。

## 简历说明

```text
构建了一个可公开展示的 Python 命令行工具，可按配置字段将表格行与图片文件匹配，自动识别缺失图片和重复图片，并输出匹配结果、异常日志和运行摘要。项目展示了表格批处理、文件校验、可重复执行流程和面向非技术用户的办公自动化交付能力。
```

## 安全边界

本项目只保留通用自动化逻辑和合成样例。真实客户数据、商品信息、订单金额、公司名称、内部路径和平台凭据都不应提交到公开仓库。
