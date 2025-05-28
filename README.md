# ComfyUI API Client

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)  
用于与ComfyUI服务端交互的API客户端库，支持工作流编排、任务状态监听和结果获取。

---

## ✨ 核心特性
1. **统一任务接口** - 通过`POST /prompt`下发文生图等工作流任务
2. **异步结果获取** - 通过`GET /history/{prompt_id}`获取生成结果和进度通知
3. **生成图片下载** - 通过`GET /view`自动下载生图片

---

## 🚀 快速开始

### 前置条件
```
# 安装Python3依赖
pip install pillow requests
```

### 运行脚本
```
python ComfyUIClient.py
```

## 📁 API工作流导出流程

### 1. 启用开发模式
```
# 在ComfyUI界面操作
1. 点击左下角「设置」按钮（齿轮图标）
2. 勾选「启用开发模式选项（API保存等」复选框
```

### 2. 通过GUI导出
```
1. 加载已创建的工作流模板
2. 点击右上角工作流菜单的「导出(API)」按钮
3. 保存为*.json文件（推荐命名规范：workflow_api.json）
```