# Global Carbon Emission Visualization 🌍

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/Mars-aliens/carbon-visualization/actions/workflows/static.yml/badge.svg)](https://github.com/Mars-aliens/carbon-visualization/actions)

这是一个基于 **Vega-Lite** 框架开发的交互式全球碳排放可视化项目。本项目通过多维度的数据可视化，展示了全球各国历史碳排放趋势、人均排放量以及地理分布特征。

📍 **项目演示地址**: [https://mars-aliens.github.io/carbon-visualization/](https://mars-aliens.github.io/carbon-visualization/)

## 🚀 项目功能

- **交互式全球地图 (Choropleth Map)**: 通过颜色深浅展示各国碳排放总量，支持鼠标悬停查看详细数值。
- **历史趋势分析**: 集成折线图或面积图，展示从工业革命以来全球碳排放的增长曲线。
- **关联过滤**: 地图与图表之间联动，点击特定国家或年份，其他图表会同步更新对应数据。
- **人均 vs 总量**: 提供不同维度的切换，帮助深入理解排放结构。

## 🛠️ 技术栈

- **可视化框架**: [Vega-Lite](https://vega.github.io/vega-lite/) (声明式统计图形语法)
- **前端托管**: GitHub Pages
- **数据源**: 基于公开的全球碳排放数据集 (如 Our World in Data / Global Carbon Budget)
- **开发工具**: VS Code, GitHub

## 📂 目录结构

```text
carbon-visualization/
├── data/                   # 数据文件
│   ├── data_processed.csv  # 碳排放处理后数据
│   ├── owid-co2-data.csv   # 碳排放原始数据
│   └── countries-50m.json  # 地图数据
├── script.js               # 存放 Vega-Lite 的 JSON 配置文件 (Spec)
├── index.html              # 项目主入口页面
├── style.css               # 基础样式
└── README.md               # 项目文档