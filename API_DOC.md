# S4P2 项目 API 文档 (V0.2)

本文档用于说明 S4P2 项目后端 API 的使用方法。

---

## 学习路径 (Learning Roadmaps)

### 1. 获取特定学习路径下的所有资源

根据提供的路径标识符（如 `web-full-stack`），获取该学习路径下的所有教学资源节点，并按学习顺序排列。

* **接口路径**: `/api/roadmaps/{roadmap_slug}`
    * *路径参数 (Path Parameter)*:
        * `roadmap_slug` (string, required): 学习路径的唯一标识。例如: `web-full-stack`.

* **请求方法**: `GET`

* **请求参数**: 无

* **成功返回示例 (Success 200 OK)**:
    * 当 `roadmap_slug` 为 `web-full-stack` 时，返回的数据结构如下：

    ```json
    {
      "roadmap_title": "Web 全栈开发者",
      "resources": [
        {
          "step": 1,
          "skill": "HTML",
          "resource_name": "MDN Web Docs – HTML",
          "resource_url": "[https://developer.mozilla.org/zh-CN/docs/Web/HTML](https://developer.mozilla.org/zh-CN/docs/Web/HTML)",
          "resource_type": "官方文档",
          "reason": "Mozilla官方教程，内容全面更新，提供面向新手的HTML基础引导"
        },
        {
          "step": 2,
          "skill": "CSS",
          "resource_name": "MDN Web Docs - CSS",
          "resource_url": "[https://developer.mozilla.org/zh-CN/docs/Web/CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS)",
          "resource_type": "官方文档",
          "reason": "权威教程，从基础原理、语法到现代布局全面覆盖，新手友好"
        },
        {
          "step": 3,
          "skill": "JavaScript",
          "resource_name": "MDN Web Docs – JavaScript 指南",
          "resource_url": "[https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity](https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity)",
          "resource_type": "教程",
          "reason": "Mozilla官方教程，新手友好，介绍现代JavaScript基础语法、DOM操作、异步编程等内容"
        },
        {
          "step": 4,
          "skill": "Git & GitHub",
          "resource_name": "廖雪峰 - Git 教程",
          "resource_url": "[https://liaoxuefeng.com/books/git/what-is-git/index.html ](https://liaoxuefeng.com/books/git/what-is-git/index.html )",
          "resource_type": "文字教程",
          "reason": "国内资深作者撰写的免费教程，从概念到命令逐步讲解，风格通俗幽默，社区广泛使用"
        },
        {
          "step": 5,
          "skill": "React.js",
          "resource_name": "React 官方文档",
          "resource_url": "[https://zh-hans.react.dev/](https://zh-hans.react.dev/)",
          "resource_type": "官方文档",
          "reason": "由React团队维护的权威教程，全面讲解组件、Hooks、路由等关键概念，具有中文版"
        }，
        {
          "step": 6,
          "skill": "Node.js",
          "resource_name": "Node.js 官方文档",
          "resource_url": "[https://nodejs.org/en/docs/](https://nodejs.org/en/docs/)",
          "resource_type": "官方文档",
          "reason": "Node.js官方权威文档，涵盖所有核心模块和API，是学习服务器端JS的必备参考"
        }，
        {
          "step": 6,
          "skill": "Express.js",
          "resource_name": "Express 官方文档",
          "resource_url": "[https://nodejs.org/en/docs/](https://nodejs.org/en/docs/)",
          "resource_type": "官方文档",
          "reason": "官方指南提供详尽示例，介绍Express核心功能和中间件用法，支持多语言"
        }，
        {
          "step": 7,
          "skill": "SQL",
          "resource_name": "菜鸟教程- SQL 教程",
          "resource_url": "[http://www.runoob.com/sql/sql-tutorial.html](http://www.runoob.com/sql/sql-tutorial.html)",
          "resource_type": "文字教程",
          "reason": "标准化SQL语言教程，系统介绍关系型数据库基础操作，包含众多例子，新手易上手"
        }，
      ]
    }
   ```

* **失败返回示例 (Error 404 Not Found)**:
    * 当提供的 `roadmap_slug` 不存在时（例如 `/api/roadmaps/non-existent-path`），返回：

    ```json
    {
      "error": "Not Found",
      "message": "The requested learning roadmap was not found."
    }
    ```