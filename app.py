# 导入 Flask 和 jsonify (jsonify 是一个能帮我们把Python字典转换成标准JSON格式的工具)
from flask import Flask, jsonify

# Flask 应用初始化
app = Flask(__name__)

# ==================================================
# 我们的“假数据库” (V2.2 - 填充了更丰富的数据)
# ==================================================
mock_db = {
    "web-full-stack": {
        "roadmap_title": "Web 全栈开发者",
        "stages": [
            # --- 主干道技能 ---
            {
                "step": 1,
                "skill": "HTML",
                "prerequisites": [], # HTML是起点，没有前置技能
                "resources": [
                    {
                        "resource_name": "MDN Web Docs – HTML",
                        "resource_url": "https://developer.mozilla.org/zh-CN/docs/Web/HTML",
                        "resource_type": "官方文档",
                        "reason": "Mozilla官方教程，内容全面更新，提供面向新手的HTML基础引导"
                    },
                    {
                        "resource_name": "编程狮(W3Cschool) – HTML 教程",
                        "resource_url": "https://www.w3cschool.cn/html/",
                        "resource_type": "文字教程",
                        "reason": "国内知名中文教程，讲解直观易懂，提供大量交互示例和练习"
                    }
                ]
            },
            {
                "step": 2,
                "skill": "CSS",
                "prerequisites": ["HTML"], # 学习CSS的前置技能是HTML
                "resources": [
                    {
                        "resource_name": "MDN Web Docs - CSS",
                        "resource_url": "https://developer.mozilla.org/zh-CN/docs/Web/CSS",
                        "resource_type": "官方文档",
                        "reason": "权威教程，从基础原理、语法到现代布局全面覆盖，新手友好"
                    },
                    {
                        "resource_name": "菜鸟教程- CSS 教程",
                        "resource_url": "http://www.runoob.com/css/css-tutorial.html",
                        "resource_type": "文字教程",
                        "reason": "中文教程，内容简洁清晰，涵盖选择器、盒模型、布局等，拥有数百在线示例"
                    }
                ]
            },
            {
                "step": 3,
                "skill": "JavaScript",
                "prerequisites": ["HTML", "CSS"], # 学习JS的前置技能是HTML和CSS
                "resources": [
                    {
                        "resource_name": "MDN Web Docs – JavaScript 指南",
                        "resource_url": "https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity",
                        "resource_type": "教程",
                        "reason": "Mozilla官方教程，新手友好，介绍现代JavaScript基础语法、DOM操作、异步编程等内容"
                    },
                    {
                        "resource_name": "JavaScript.info",
                        "resource_url": "https://javascript.info/",
                        "resource_type": "文字教程, 类官方文档",
                        "reason": "涵盖现代JavaScript的免费在线教程，内容新颖完整，配有互动示例和实战练习"
                    }
                ]
            },
            {
                "step": 4,
                "skill": "React.js",
                "prerequisites": ["HTML", "CSS", "JavaScript"], # 学习React的前置技能是三件套
                "resources": [
                    {
                        "resource_name": "React 官方文档",
                        "resource_url": "https://zh-hans.react.dev/",
                        "resource_type": "官方文档",
                        "reason": "由React团队维护的权威教程，全面讲解组件、Hooks、路由等关键概念，具有中文版"
                    },
                    {
                        "resource_name": "Scrimba - Learn React 免费课程",
                        "resource_url": "https://v1.scrimba.com/playlist/p7P5Hd",
                        "resource_type": "互动式教程",
                        "reason": "交互式视频课程，包含59个互动单元，通过实战项目掌握React基础与进阶用法"
                    }
                ]
            },
             {
                "step": 5,
                "skill": "Node.js & Express.js",
                "prerequisites": ["JavaScript"], # 学习Node.js需要先懂JavaScript
                "resources": [
                    {
                        "resource_name": "Node.js 官方文档",
                        "resource_url": "https://nodejs.org/en/docs/",
                        "resource_type": "官方文档",
                        "reason": "Node.js官方权威文档，涵盖所有核心模块和API。"
                    },
                    {
                        "resource_name": "Express 官方文档",
                        "resource_url": "https://expressjs.com/zh-cn",
                        "resource_type": "官方文档",
                        "reason": "官方指南提供详尽示例，介绍Express核心功能和中间件用法。"
                    }
                ]
            },
            # --- 独立技能 (可以在任何时候学习) ---
            {
                "step": None, # step为None，表示不在线性主干道上
                "skill": "Git & GitHub",
                "prerequisites": [], # 独立技能，没有前置依赖
                "resources": [
                    {
                        "resource_name": "Learn Git Branching 互动教程",
                        "resource_url": "https://learngitbranching.js.org/",
                        "resource_type": "互动式教程",
                        "reason": "可视化的Git学习工具，通过动画演示分支操作，寓教于乐。"
                    },
                    {
                        "resource_name": "廖雪峰 - Git 教程",
                        "resource_url": "https://liaoxuefeng.com/books/git/what-is-git/index.html",
                        "resource_type": "文字教程",
                        "reason": "国内资深作者撰写的免费教程，从概念到命令逐步讲解，风格通俗幽默。"
                    }
                ]
            },
            {
                "step": None,
                "skill": "SQL",
                "prerequisites": [],
                "resources": [
                    {
                        "resource_name": "SQLBolt 互动 SQL 教程",
                        "resource_url": "https://sqlbolt.com/",
                        "resource_type": "互动式教程",
                        "reason": "界面极其简洁，通过一系列“先学后练”的交互式课程掌握SQL查询。"
                    },
                    {
                        "resource_name": "菜鸟教程- SQL 教程",
                        "resource_url": "http://www.runoob.com/sql/sql-tutorial.html",
                        "resource_type": "文字教程",
                        "reason": "标准化SQL语言教程，系统介绍关系型数据库基础操作，包含众多例子，新手易上手"
                    }
                ]
            }
        ]
    }
}
# ==================================================

# 这是我们新开发的、真正的业务API接口
@app.route("/api/roadmaps/<string:roadmap_slug>")
def get_roadmap_data(roadmap_slug):
    # 从我们的“假数据库”里，根据用户请求的 roadmap_slug 查找数据
    roadmap_data = mock_db.get(roadmap_slug)

    # 如果找到了数据
    if roadmap_data:
        # 使用 jsonify 把我们的字典数据转换成标准的JSON格式返回给前端
        # 同时返回 200 状态码，表示“成功”
        return jsonify(roadmap_data), 200
    # 如果没找到数据
    else:
        # 就返回我们API文档里定义的那个 404 错误信息
        # 同时返回 404 状态码，表示“未找到”
        return jsonify({"error": "Not Found", "message": "The requested learning roadmap was not found."}), 404

