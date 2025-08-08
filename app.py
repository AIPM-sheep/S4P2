from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mock_db = {
    "backend-engineer": {
        "roadmap_title": "后端工程师",
        "stages": [
            {
                "stage_name": "阶段一: 编程与计算机科学基础 (CS & Language Fundamentals)",
                "steps": [
                    {
                        "step": 1,
                        "skill": "Python 高级编程 (OOP, 装饰器)",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Real Python: OOP in Python 3",
                                "resource_url": "https://realpython.com/python3-object-oriented-programming/",
                                "resource_type": "深度文章/教程系列",
                                "language": "EN",
                                "reason": "全球公认的高质量教程，用海量代码示例和图解透彻讲解Python OOP。"
                            },
                            {
                                "resource_name": "廖雪峰的Python教程-面向对象高级编程",
                                "resource_url": "https://www.liaoxuefeng.com/wiki/1016959663602400/1017496031529184",
                                "resource_type": "中文在线教程",
                                "language": "CN",
                                "reason": "国内广受好评的免费教程，简明扼要，直击Python高级OOP特性的重点。"
                            }
                        ]
                    },
                    {
                        "step": 2,
                        "skill": "数据结构与算法 (Data Structures & Algorithms)",
                        "prerequisites": ["Python 高级编程 (OOP, 装饰器)"],
                        "resources": [
                            {
                                "resource_name": "《Hello 算法》",
                                "resource_url": "https://github.com/krahets/hello-algo",
                                "resource_type": "开源电子书/动画图解",
                                "language": "CN/EN",
                                "reason": "国产优秀开源项目，通过动画图解生动展示算法原理，对国内学习者极其友好。"
                            },
                            {
                                "resource_name": "NeetCode.io",
                                "resource_url": "https://neetcode.io/",
                                "resource_type": "互动教程/刷题平台",
                                "language": "EN",
                                "reason": "LeetCode题目的精华路线图，提供清晰图解和多语言视频题解，实战性极强。"
                            }
                        ]
                    },
                    {
                        "step": 3,
                        "skill": "版本控制 (Git 核心工作流)",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Learn Git Branching",
                                "resource_url": "https://learngitbranching.js.org/?locale=zh_CN",
                                "resource_type": "互动教程/可视化学习",
                                "language": "EN/CN",
                                "reason": "革命性的可视化学习工具，通过网页虚拟操作，让分支等核心概念变得异常直观。"
                            },
                            {
                                "resource_name": "Pro Git (中文版)",
                                "resource_url": "https://git-scm.com/book/zh/v2",
                                "resource_type": "官方书籍/权威文档",
                                "language": "CN/EN",
                                "reason": "Git官方权威“圣经”，内容全面、严谨、深入，任何希望精通Git的工程师都应通读。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段二: API 开发与框架 (API Development & Frameworks)",
                "steps": [
                    {
                        "step": 4,
                        "skill": "RESTful API 设计原则",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Microsoft - RESTful web API design",
                                "resource_url": "https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design",
                                "resource_type": "官方最佳实践文档",
                                "language": "EN",
                                "reason": "业界关于RESTful API设计的最佳实践指南之一，构建专业API的必备参考。"
                            },
                            {
                                "resource_name": "阮一峰的网络日志 - RESTful API 设计指南",
                                "resource_url": "https://www.ruanyifeng.com/blog/2014/05/restful_api.html",
                                "resource_type": "中文博客文章",
                                "language": "CN",
                                "reason": "国内后端开发者的启蒙读物，用通俗易懂的语言快速建立对RESTful风格的理解。"
                            }
                        ]
                    },
                    {
                        "step": 5,
                        "skill": "Web 框架 (FastAPI 或 Flask)",
                        "prerequisites": ["Python 高级编程 (OOP, 装饰器)", "RESTful API 设计原则"],
                        "resources": [
                            {
                                "resource_name": "FastAPI Official Tutorial",
                                "resource_url": "https://fastapi.tiangolo.com/tutorial/",
                                "resource_type": "官方文档/互动教程",
                                "language": "EN",
                                "reason": "开源项目文档的典范，手把手教你构建完整API，实战性无出其右。"
                            },
                            {
                                "resource_name": "The Flask Mega-Tutorial by Miguel Grinberg",
                                "resource_url": "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world",
                                "resource_type": "博客教程系列",
                                "language": "EN",
                                "reason": "无法绕过的Flask经典教程，带领学习者从零构建一个功能完整的博客应用。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段三: 数据库技术 (Database Technologies)",
                "steps": [
                    {
                        "step": 6,
                        "skill": "关系型数据库 (PostgreSQL) 与 SQL 进阶",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "PGExercises",
                                "resource_url": "https://pgexercises.com/",
                                "resource_type": "互动练习平台",
                                "language": "EN",
                                "reason": "“做中学”提高SQL技能最有效的方法之一，提供难度递增的在线练习和即时反馈。"
                            },
                            {
                                "resource_name": "The Art of PostgreSQL",
                                "resource_url": "https://theartofpostgresql.com/",
                                "resource_type": "在线书籍/深度指南",
                                "language": "EN",
                                "reason": "深度挖掘PG能力的免费在线书籍，讲解如何写出更高效、更优雅的SQL。"
                            }
                        ]
                    },
                    {
                        "step": 7,
                        "skill": "NoSQL 数据库 (MongoDB)",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "MongoDB University - M001: MongoDB Basics",
                                "resource_url": "https://learn.mongodb.com/courses/m001-mongodb-basics",
                                "resource_type": "官方免费课程/互动实验",
                                "language": "EN",
                                "reason": "官方权威入门课程，结合视频、测验和云端实验，动手掌握核心概念。"
                            },
                            {
                                "resource_name": "freeCodeCamp - MongoDB Full Course",
                                "resource_url": "https://www.youtube.com/watch?v=E-1xI85Zog8",
                                "resource_type": "视频课程",
                                "language": "EN",
                                "reason": "提供了对MongoDB更全面的讲解，深入数据建模、索引策略和性能优化等高级主题。"
                            }
                        ]
                    },
                    {
                        "step": 8,
                        "skill": "缓存技术 (Redis)",
                        "prerequisites": ["数据结构与算法 (Data Structures & Algorithms)"],
                        "resources": [
                            {
                                "resource_name": "《Redis 设计与实现》Read the Docs",
                                "resource_url": "https://redisbook.readthedocs.io/en/latest/",
                                "resource_type": "开源在线书籍",
                                "language": "CN/EN",
                                "reason": "国产经典之作，从源码层面深度剖析Redis内部原理，助你从“会用”到“理解”。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段四: 容器化与 CI/CD (Containerization & CI/CD)",
                "steps": [
                    {
                        "step": 9,
                        "skill": "容器化 (Docker & Docker Compose)",
                        "prerequisites": [],
                        "resources": [
                            {
                                "resource_name": "Docker — From Zero to Hero (Prakhar Srivastav)",
                                "resource_url": "https://prakhar.me/docker-curriculum/",
                                "resource_type": "互动教程/博客系列",
                                "language": "EN",
                                "reason": "从零开始的Docker课程，通过实际操作讲解核心概念，非常适合初学者。"
                            },
                            {
                                "resource_name": "《Docker — 从入门到实践》",
                                "resource_url": "https://vuepress.mirror.docker-practice.com/",
                                "resource_type": "开源中文书籍",
                                "language": "CN",
                                "reason": "国内最受欢迎的Docker开源书籍之一，内容全面，覆盖了从基础到实践的方方面面。"
                            }
                        ]
                    },
                    {
                        "step": 10,
                        "skill": "CI/CD (GitHub Actions)",
                        "prerequisites": ["版本控制 (Git 核心工作流)", "容器化 (Docker & Docker Compose)"],
                        "resources": [
                            {
                                "resource_name": "GitHub Actions Documentation",
                                "resource_url": "https://docs.github.com/en/actions",
                                "resource_type": "官方文档",
                                "language": "EN/CN",
                                "reason": "学习任何技术的最佳起点，官方文档最权威、最准确。"
                            },
                            {
                                "resource_name": "CI/CD with GitHub Actions - Full Course",
                                "resource_url": "https://www.youtube.com/watch?v=R8_veQiY-c8",
                                "resource_type": "视频课程",
                                "language": "EN",
                                "reason": "freeCodeCamp出品的免费课程，系统性地讲解了如何使用GitHub Actions构建完整的CI/CD流水线。"
                            }
                        ]
                    }
                ]
            },
            {
                "stage_name": "阶段五: 可观测性与监控 (Observability & Monitoring)",
                "steps": [
                    {
                        "step": 11,
                        "skill": "日志 (Logging)",
                        "prerequisites": ["Web 框架 (FastAPI 或 Flask)"],
                        "resources": [
                            {
                                "resource_name": "Python Logging HOWTO",
                                "resource_url": "https://docs.python.org/3/howto/logging.html",
                                "resource_type": "官方文档/指南",
                                "language": "EN",
                                "reason": "Python官方的日志指南，是理解和正确使用logging模块的最权威资料。"
                            }
                        ]
                    },
                    {
                        "step": 12,
                        "skill": "监控 (Prometheus & Grafana)",
                        "prerequisites": ["Web 框架 (FastAPI 或 Flask)", "容器化 (Docker & Docker Compose)"],
                        "resources": [
                            {
                                "resource_name": "Prometheus - Overview",
                                "resource_url": "https://prometheus.io/docs/introduction/overview/",
                                "resource_type": "官方文档",
                                "language": "EN",
                                "reason": "Prometheus官方文档，快速理解其架构和核心概念。"
                            },
                            {
                                "resource_name": "Grafana Fundamentals",
                                "resource_url": "https://grafana.com/tutorials/grafana-fundamentals/",
                                "resource_type": "官方教程",
                                "language": "EN",
                                "reason": "Grafana官方的基础教程，手把手教你创建第一个Dashboard。"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

@app.route('/api/roadmaps/<string:roadmap_name>', methods=['GET'])
def get_roadmap(roadmap_name):
    roadmap = mock_db.get(roadmap_name)
    if not roadmap:
        return jsonify({"error": "Roadmap not found"}), 404
    return jsonify(roadmap)

if __name__ == '__main__':
    app.run(debug=True, port=5001)