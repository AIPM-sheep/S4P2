# 导入 Flask 和 jsonify (jsonify 是一个能帮我们把Python字典转换成标准JSON格式的工具)
from flask import Flask, jsonify

# Flask 应用初始化
app = Flask(__name__)

# ==================================================
# 我们的“假数据库”
# 这就是一个Python字典，它的结构和我们API文档里定义的一模一样
# ==================================================
mock_db = {
    "web-full-stack": {
        "roadmap_title": "Web 全栈开发者",
        "resources": [
            {
                "step": 1,
                "skill": "HTML",
                "resource_name": "MDN Web Docs – HTML",
                "resource_url": "https://developer.mozilla.org/zh-CN/docs/Web/HTML",
                "resource_type": "官方文档",
                "reason": "Mozilla官方教程，内容全面更新，提供面向新手的HTML基础引导"
            },
            {
                "step": 2,
                "skill": "CSS",
                "resource_name": "MDN Web Docs - CSS",
                "resource_url": "https://developer.mozilla.org/zh-CN/docs/Web/CSS",
                "resource_type": "官方文档",
                "reason": "权威教程，从基础原理、语法到现代布局全面覆盖，新手友好"
            },
            {
                "step": 3,
                "skill": "JavaScript",
                "resource_name": "MDN Web Docs – JavaScript 指南",
                "resource_url": "https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity",
                "resource_type": "教程",
                "reason": "Mozilla官方教程，新手友好，介绍现代JavaScript基础语法、DOM操作、异步编程等内容"
            },
            {
                "step": 4,
                "skill": "Git & GitHub",
                "resource_name": "廖雪峰 - Git 教程",
                "resource_url": "https://liaoxuefeng.com/books/git/what-is-git/index.html",
                "resource_type": "文字教程",
                "reason": "国内资深作者撰写的免费教程，从概念到命令逐步讲解，风格通俗幽默，社区广泛使用"
            },
            {
                "step": 5,
                "skill": "React.js",
                "resource_name": "React 官方文档",
                "resource_url": "https://zh-hans.react.dev/",
                "resource_type": "官方文档",
                "reason": "由React团队维护的权威教程，全面讲解组件、Hooks、路由等关键概念，具有中文版"
            },
            {
                "step": 6,
                "skill": "Node.js",
                "resource_name": "Node.js 官方文档",
                "resource_url": "https://nodejs.org/en/docs/",
                "resource_type": "官方文档",
                "reason": "Node.js官方权威文档，涵盖所有核心模块和API，是学习服务器端JS的必备参考"
            },
            {
                "step": 6,
                "skill": "Express.js",
                "resource_name": "Express 官方文档",
                "resource_url": "https://nodejs.org/en/docs/",
                "resource_type": "官方文档",
                "reason": "官方指南提供详尽示例，介绍Express核心功能和中间件用法，支持多语言"
            },
            {
                "step": 7,
                "skill": "SQL",
                "resource_name": "菜鸟教程- SQL 教程",
                "resource_url": "http://www.runoob.com/sql/sql-tutorial.html",
                "resource_type": "文字教程",
                "reason": "标准化SQL语言教程，系统介绍关系型数据库基础操作，包含众多例子，新手易上手"
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