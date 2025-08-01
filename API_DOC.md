# S4P2 项目 API 文档 (V0.5 - AI Agent 工程师路径)

本文档用于说明 S4P2 项目后端 API 的使用方法。

---

## 学习路径 (Learning Roadmaps)

### 1. 获取特定学习路径下的所有资源

根据提供的路径标识符（如 `ai-agent-engineer`），获取该学习路径下的所有教学资源节点，并按学习顺序排列。

* **接口路径**: `/api/roadmaps/{roadmap_slug}`
    * *路径参数 (Path Parameter)*:
        * `roadmap_slug` (string, required): 学习路径的唯一标识。例如: `ai-agent-engineer`。

* **请求方法**: `GET`

* **请求参数**: 无

* **成功返回示例 (Success 200 OK)**:
    * 当 `roadmap_slug` 为 `ai-agent-engineer` 时，返回的数据结构如下：

    ```json
    {
      "roadmap_title": "AI Agent 工程师",
      "stages": [
        {
          "step": 1,
          "skill": "精通 Python 编程",
          "prerequisites": [],
          "resources": [
            {
              "resource_name": "Python 官方文档 - asyncio",
              "resource_url": "[https://docs.python.org/3/library/asyncio.html](https://docs.python.org/3/library/asyncio.html)",
              "resource_type": "官方文档",
              "reason": "最权威、最全面的第一手资料，定义了async/await，是理解所有异步框架的基础。"
            },
            {
              "resource_name": "ArjanCodes - \"A Complete Guide to Async/Await in Python\"",
              "resource_url": "[https://www.youtube.com/watch?v=16w3F22_18s](https://www.youtube.com/watch?v=16w3F22_18s)",
              "resource_type": "视频课程",
              "reason": "质量极高的视频教程，通过重构实战，让你直观感受异步编程带来的性能提升。"
            }
          ]
        },
        {
          "step": 1,
          "skill": "软件工程与 API 基础",
          "prerequisites": [
            "精通 Python 编程"
          ],
          "resources": [
            {
              "resource_name": "FastAPI 官方文档 - 入门教程",
              "resource_url": "[https://fastapi.tiangolo.com/tutorial/](https://fastapi.tiangolo.com/tutorial/)",
              "resource_type": "官方教程",
              "reason": "业界标杆级的交互式教程，让你在学习中即时获得一个带自动化文档的高性能API。"
            },
            {
              "resource_name": "freeCodeCamp - \"FastAPI Course for Beginners\"",
              "resource_url": "[https://www.youtube.com/watch?v=7t2alSnE2-I](https://www.youtube.com/watch?v=7t2alSnE2-I)",
              "resource_type": "视频课程",
              "reason": "完整的项目视频课程，手把手带你完成从零到一的搭建、测试和部署，快速建立全局观。"
            }
          ]
        },
        {
          "step": 2,
          "skill": "LLM 理论入门",
          "prerequisites": [
            "精通 Python 编程"
          ],
          "resources": [
            {
              "resource_name": "Jay Alammar - \"The Illustrated Transformer\"",
              "resource_url": "[https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)",
              "resource_type": "深度文章",
              "reason": "无法被超越的经典，用极其直观的动图和比喻解释了复杂的Attention机制，入门必读。"
            },
            {
              "resource_name": "3Blue1Brown - \"Attention in Transformers, visually explained\"",
              "resource_url": "[https://www.youtube.com/watch?v=mMa20_sJ4IU](https://www.youtube.com/watch?v=mMa20_sJ4IU)",
              "resource_type": "视频课程",
              "reason": "从数学思想的层面，让你对Attention机制的巧妙之处建立深刻的科学直觉。"
            }
          ]
        },
        {
          "step": 2,
          "skill": "高级提示工程",
          "prerequisites": [
            "LLM 理论入门"
          ],
          "resources": [
            {
              "resource_name": "OpenAI - \"Function calling\" 官方文档",
              "resource_url": "[https://platform.openai.com/docs/guides/function-calling](https://platform.openai.com/docs/guides/function-calling)",
              "resource_type": "官方文档",
              "reason": "理解模型原生的工具调用能力，是掌握现代Agent框架底层逻辑的关键一步。"
            },
            {
              "resource_name": "\"Let's build the GPT-4 function calling API from scratch\" by AI Jason",
              "resource_url": "[https://www.youtube.com/watch?v=tjYo4jU-i-s](https://www.youtube.com/watch?v=tjYo4jU-i-s)",
              "resource_type": "视频课程",
              "reason": "带你手写一个函数调用调度器，让你彻底告别“黑箱API调用者”的身份，理解其核心原理。"
            }
          ]
        },
        {
          "step": 3,
          "skill": "Agentic 框架入门 (LangChain)",
          "prerequisites": [
            "高级提示工程"
          ],
          "resources": [
            {
              "resource_name": "LangChain 官方教程 - \"Build an Agent\"",
              "resource_url": "[https://python.langchain.com/docs/tutorials/agents](https://python.langchain.com/docs/tutorials/agents)",
              "resource_type": "官方教程",
              "reason": "学习任何框架，官方的“Get Started”教程永远是第一选择，确保你使用的是最新的实践方式。"
            },
            {
              "resource_name": "James Briggs - \"Code a LangChain Agent From Scratch\"",
              "resource_url": "[https://www.youtube.com/watch?v=2y_uB1wK-e8](https://www.youtube.com/watch?v=2y_uB1wK-e8)",
              "resource_type": "视频课程",
              "reason": "通过“手搓”一个迷你版的Agent循环，能让你对框架的抽象（如AgentExecutor）有更深刻的体感。"
            }
          ]
        },
        {
          "step": 3,
          "skill": "掌握核心 Agent 模式 (ReAct)",
          "prerequisites": [
            "Agentic 框架入门 (LangChain)"
          ],
          "resources": [
            {
              "resource_name": "ReAct 论文官方实现",
              "resource_url": "[https://github.com/ysymyth/ReAct](https://github.com/ysymyth/ReAct)",
              "resource_type": "开源项目",
              "reason": "直接运行论文作者的<200行最小化实现，剥离所有框架封装，直击ReAct循环的本质。"
            },
            {
              "resource_name": "LangChain - \"Build a ReAct agent from scratch with LangGraph\"",
              "resource_url": "[https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/)",
              "resource_type": "官方教程",
              "reason": "学习LangGraph如何用“图”的思想来工程化地实现ReAct模式，深入理解框架的设计哲学。"
            }
          ]
        },
        {
          "step": 4,
          "skill": "向量数据库入门",
          "prerequisites": [
            "LLM 理论入门"
          ],
          "resources": [
            {
              "resource_name": "FAISS 官方Wiki - \"Guidelines to choose an index\"",
              "resource_url": "[https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index](https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index)",
              "resource_type": "官方文档",
              "reason": "压榨检索性能的“优化圣经”，指导你在不同数据规模下选择最优索引，实现毫秒级检索。"
            },
            {
              "resource_name": "ChromaDB 官方博客 - \"Scaling Chroma: A Technical Deep Dive\"",
              "resource_url": "[https://www.trychroma.com/blog/scaling-chroma](https://www.trychroma.com/blog/scaling-chroma)",
              "resource_type": "深度文章",
              "reason": "讲解ChromaDB的架构以及如何进行横向扩展，是向量数据库从“单机”走向“分布式服务”的蓝图。"
            }
          ]
        },
        {
          "step": 4,
          "skill": "检索增强生成 (RAG) 全流程",
          "prerequisites": [
            "向量数据库入门",
            "掌握核心 Agent 模式 (ReAct)"
          ],
          "resources": [
            {
              "resource_name": "LlamaIndex 官方文档 - \"RAG Techniques\"",
              "resource_url": "[https://docs.llamaindex.ai/en/stable/optimizing/production_rag/](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)",
              "resource_type": "官方教程",
              "reason": "RAG优化的“军火库”，详细介绍了分块策略、重排序、多路召回等所有你需要知道的高级技巧。"
            },
            {
              "resource_name": "\"Advanced RAG 01: The RAG Triad\" by AI Jason",
              "resource_url": "[https://www.youtube.com/watch?v=E2t1_aAayHw](https://www.youtube.com/watch?v=E2t1_aAayHw)",
              "resource_type": "视频课程",
              "reason": "用清晰的“RAG三元悖论”来解释RAG评估的核心，并介绍如何系统性地提升RAG质量。"
            }
          ]
        },
        {
          "step": 5,
          "skill": "状态管理与复杂流 (LangGraph)",
          "prerequisites": [
            "掌握核心 Agent 模式 (ReAct)"
          ],
          "resources": [
            {
              "resource_name": "LangGraph 官方文档",
              "resource_url": "[https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)",
              "resource_type": "官方文档",
              "reason": "理解LangGraph如何用图（Graph）来定义循环和状态，掌握其作为“状态机”的本质。"
            },
            {
              "resource_name": "Bilibili - \"LangGraph快速入门与智能体开发实战\" by 九天Hector",
              "resource_url": "[https://www.bilibili.com/video/BV1Kx3CzyE6Q?vd_source=14a017f1942e66549c878a8ddcc8bc2b/](hhttps://www.bilibili.com/video/BV1Kx3CzyE6Q?vd_source=14a017f1942e66549c878a8ddcc8bc2b/)",
              "resource_type": "视频教程",
              "reason": "优秀的中文社区实战教程，从零开始，用中文语境讲解，非常适合国内学习者快速上手。"
            }
          ]
        },
        {
          "step": 5,
          "skill": "多 Agent 协作 (CrewAI)",
          "prerequisites": [
            "掌握核心 Agent 模式 (ReAct)"
          ],
          "resources": [
            {
              "resource_name": "CrewAI 官方文档 - \"Examples\"",
              "resource_url": "[https://docs.crewai.com/examples/](https://docs.crewai.com/examples/)",
              "resource_type": "官方示例",
              "reason": "官方示例库是最好的学习材料，提供了各种协作模式的即用代码，是快速启动多Agent项目的“模板库”。"
            },
            {
              "resource_name": "GitHub - \"CrewAI Agent Templates\" by joaomdmoura",
              "resource_url": "[https://github.com/joaomdmoura/crewAI-examples](https://github.com/joaomdmoura/crewAI-examples)",
              "resource_type": "开源项目",
              "reason": "直接学习框架作者提供的项目模板，比任何教程都更贴近最佳实践，可直接复用，极大加速开发。"
            }
          ]
        },
        {
          "step": 6,
          "skill": "监控、评估与调试",
          "prerequisites": [
            "检索增强生成 (RAG) 全流程",
            "多 Agent 协作 (CrewAI)"
          ],
          "resources": [
            {
              "resource_name": "RAGAs: Retrieval-Augmented Generation Assessment",
              "resource_url": "[https://docs.ragas.io/](https://docs.ragas.io/)",
              "resource_type": "开源框架",
              "reason": "提供评估RAG系统性能的量化指标，让你能用数据驱动的方式优化Agent。"
            },
            {
              "resource_name": "LangSmith 官方文档 - \"Automated Evaluation\"",
              "resource_url": "[https://docs.smith.langchain.com/evaluation/automating](https://docs.smith.langchain.com/evaluation/automating)",
              "resource_type": "官方教程",
              "reason": "学习如何创建自定义评估器，在每次代码提交后自动运行评估，是CI/CD的关键一环。"
            }
          ]
        },
        {
          "step": 6,
          "skill": "安全与伦理",
          "prerequisites": [
            "监控、评估与调试"
          ],
          "resources": [
            {
              "resource_name": "OWASP Top 10 for Large Language Model Applications",
              "resource_url": "[https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)",
              "resource_type": "行业标准",
              "reason": "从关注Prompt注入，升级到关注OWASP总结的LLM应用十大安全风险，建立系统性安全思维。"
            },
            {
              "resource_name": "Rebuff.ai - \"The LLM Security Leaderboard\"",
              "resource_url": "[https://github.com/protectai/rebuff](https://github.com/protectai/rebuff)",
              "resource_type": "开源工具",
              "reason": "开源的Prompt注入“蜜罐”和“防火墙”，让你了解当前最新的攻击技术和防御效果。"
            }
          ]
        }
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
    