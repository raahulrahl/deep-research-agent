<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">Deep Research Agent</h1>
<h3 align="center">AI-Powered Deep Research with Citation Tracking</h3>

<p align="center">
  <strong>AI-powered deep research agent that performs comprehensive research with automatic citation tracking and structured output.</strong><br/>
  Coordinates specialized research tools to discover sources, validate information, and provide evidence-based insights.
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/deep-research-agent/actions/workflows/main.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/Paraschamoli/deep-research-agent/main.yml?branch=main" alt="Build status">
  </a>
  <a href="https://codecov.io/gh/Paraschamoli/deep-research-agent">
    <img src="https://codecov.io/gh/Paraschamoli/deep-research-agent/branch/main/graph/badge.svg" alt="codecov">
  </a>
  <a href="https://img.shields.io/github/license/Paraschamoli/deep-research-agent">
    <img src="https://img.shields.io/github/license/Paraschamoli/deep-research-agent" alt="License">
  </a>
</p>

---

## 🎯 What is Deep Research Agent?

An AI-powered research analyst that performs comprehensive, multi-step investigations with automatic citation tracking. Think of it as having a team of research assistants who automatically discover sources, validate information, and synthesize accurate, structured insights from complex topics.

### Skills
The agent includes the `deep-research` skill for comprehensive research capabilities:
- **Primary Capability**: Performs comprehensive research with automatic citation tracking and structured output
- **Features**: Real-time web research using Exa tools, automatic citation tracking and validation, structured output with research report format
- **Limitations**: Focused on web-based research, processing time depends on query complexity

### Key Features
*   **🔍 Multi-Step Research** - Comprehensive investigation methodology
*   **📚 Automatic Citations** - Tracks and formats all source references
*   **🎯 Structured Output** - Consistent, well-organized research reports
*   **🧠 Reasoning Tools** - Uses planning and analysis for deeper insights
*   **⚡ Exa Integration** - Advanced search and research capabilities
*   **📊 Evidence-Based** - Validates information across multiple sources

### Built-in Tools
*   **ExaTools** - Advanced web search and research capabilities
*   **ReasoningTools** - Planning, analysis, and critical thinking
*   **Intelligent Workflow** - Multi-step research methodology

### Research Methodology
1.  **Planning Phase** - Strategy development using reasoning tools
2.  **Discovery Phase** - Source identification and validation
3.  **Analysis Phase** - Information synthesis and pattern recognition
4.  **Synthesis Phase** - Structured report generation with citations
5.  **Quality Phase** - Verification and evidence validation

---

> **🌐 Join the Internet of Agents**
> Register your agent at [bindus.directory](https://bindus.directory) to make it discoverable worldwide and enable agent-to-agent collaboration. **It takes 2 minutes and unlocks the full potential of your agent.**

---

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/Paraschamoli/deep-research-agent.git
cd deep-research-agent

# Set up virtual environment with uv
uv venv --python 3.12
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API keys:
# OPENAI_API_KEY=sk-...      # For OpenAI GPT-4o
# OPENROUTER_API_KEY=sk-...  # For OpenRouter (cheaper alternative)
# EXA_API_KEY=sk-...         # Required: Get from https://exa.ai
```

### 3. Run Locally

```bash
# Start the deep research agent
python deep_research_agent/main.py

# Or using uv
uv run python deep_research_agent/main.py
```

### 4. Test with Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Access at: http://localhost:3773
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file:

```env
# Required APIs
EXA_API_KEY=sk-...           # Required: https://exa.ai

# Choose ONE LLM provider
OPENAI_API_KEY=sk-...        # OpenAI API key
OPENROUTER_API_KEY=sk-...    # OpenRouter API key (alternative)

# Optional configuration
MODEL_NAME=openai/gpt-4o     # Model ID for OpenRouter
MEM0_API_KEY=sk-...          # Optional: For memory operations
```

### Port Configuration
Default port: `3773` (can be changed in `agent_config.json`)

## 💡 Usage Examples

### Via JSON-RPC API

```bash
curl --location 'http://localhost:3773' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-or-v1-...' \
--data '{
  "jsonrpc": "2.0",
  "method": "message/send",
  "params": {
    "message": {
      "role": "user",
      "parts": [
        {
          "kind": "text",
          "text": "Analyze market trends in renewable energy storage technologies with citation tracking."
        }
      ],
      "kind": "message",
      "messageId": "af476c38-3f8b-48f7-b230-22f54cec4401",
      "contextId": "af476c38-3f8b-48f7-b230-22f54cec4402",
      "taskId": "af476c38-3f8b-48f7-b230-22f54cec4403"
    },
    "skillId": "deep-research-v1",
    "configuration": {
      "acceptedOutputModes": [
        "application/json"
      ]
    }
  },
  "id": "af476c38-3f8b-48f7-b230-22f54cec4404"
}'
```

### Sample Research Queries

```text
"Research the impact of AI regulation on global tech companies with structured output and citations"
"Analyze market trends in renewable energy storage technologies with academic citations"
"Conduct deep research on mRNA vaccine technology developments with comprehensive citations"
"Research competitive landscape of electric vehicle manufacturers with financial data and sources"
"Analyze geopolitical implications of semiconductor supply chain disruptions with evidence"
```

### Expected Output Format

```markdown
# Research Report: {Research Topic}

## Executive Summary
High-level overview of findings with key citations...

## Research Methodology
- Search strategy and parameters
- Sources analyzed and validation approach
- Date range and scope limitations

## Detailed Findings

### Section 1: {Topic Area 1}
Detailed research findings with inline citations [1][2]
Evidence-based analysis and data points

### Section 2: {Topic Area 2}
Comparative analysis with supporting evidence [3][4]
Trend identification and validation

## Data & Analysis

### Structured Data Table
| Metric/Parameter | Value | Source |
|-----------------|-------|--------|
| Market Size | $X billion | [Citation 1] |
| Growth Rate | Y% | [Citation 2] |
| Key Players | Company A, B, C | [Citation 3] |

### Key Insights
1. **Insight 1** - Supporting evidence with citations
2. **Insight 2** - Data-backed analysis with references
3. **Insight 3** - Validated conclusions with sources

## Conclusions
Evidence-based conclusions with supporting citations...

## Citations
[1] {Full citation details with URL and relevance}
[2] {Full citation details with URL and relevance}
[3] {Full citation details with URL and relevance}

## Research Limitations
- Scope and methodology constraints
- Source availability and verification
- Time frame and data freshness
```

## 🐳 Docker Deployment

### Quick Docker Setup

```bash
# Build the image
docker build -t deep-research-agent .

# Run container
docker run -d \
  -p 3773:3773 \
  -e EXA_API_KEY=your_exa_key \
  -e OPENAI_API_KEY=your_openai_key \
  --name deep-research-agent \
  deep-research-agent

# Check logs
docker logs -f deep-research-agent
```

### Docker Compose (Recommended)

`docker-compose.yml`:

```yaml
version: '3.8'
services:
  deep-research-agent:
    build: .
    ports:
      - "3773:3773"
    environment:
      - EXA_API_KEY=${EXA_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
    restart: unless-stopped
```

Run with Compose:

```bash
# Start with compose
docker-compose up -d

# View logs
docker-compose logs -f
```

## 📁 Project Structure

```text
deep-research-agent/
├── deep_research_agent/
│   ├── skills/
│   │   └── deep-research/
│   │       ├── skill.yaml          # Skill configuration
│   │       └── __init__.py
│   ├── __init__.py
│   └── main.py                     # Agent entry point
├── agent_config.json               # Bindu agent configuration
├── pyproject.toml                  # Python dependencies
├── Dockerfile                      # Multi-stage Docker build
├── docker-compose.yml              # Docker Compose setup
├── README.md                       # This documentation
├── .env.example                    # Environment template
└── uv.lock                         # Dependency lock file
```

## 🔌 API Reference

### Health Check

```bash
GET http://localhost:3773/health
```

Response:
```json
{"status": "healthy", "agent": "Deep Research Agent"}
```

### Chat Endpoint

```bash
POST http://localhost:3773/chat
Content-Type: application/json

{
  "messages": [
    {"role": "user", "content": "Your deep research query here"}
  ]
}
```

## 🧪 Testing

### Local Testing

```bash
# Install test dependencies
uv sync --group dev

# Run tests
pytest tests/

# Test with specific API keys
EXA_API_KEY=test_key python -m pytest
```

### Integration Test

```bash
# Start agent
python deep_research_agent/main.py &

# Test API endpoint
curl -X POST http://localhost:3773/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Research AI advancements"}]}'
```

## 🚨 Troubleshooting

### Common Issues & Solutions

**"EXA_API_KEY required"**
Get your key from: https://exa.ai

**"No LLM API key provided"**
Set either `OPENAI_API_KEY` or `OPENROUTER_API_KEY`

**"Port 3773 already in use"**
Change port in `agent_config.json` or kill the process:
```bash
lsof -ti:3773 | xargs kill -9
```

**Docker build fails**
```bash
docker system prune -a
docker-compose build --no-cache
```

**Research tool errors**
Check Exa API key validity and quota limits

## 📊 Dependencies

### Core Packages
*   **bindu** - Agent deployment framework
*   **agno** - AI agent framework
*   **exa-py** - Exa research API
*   **openai** - OpenAI client
*   **requests** - HTTP requests
*   **rich** - Console output
*   **python-dotenv** - Environment management

### Development Packages
*   **pytest** - Testing framework
*   **ruff** - Code formatting/linting
*   **pre-commit** - Git hooks

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1.  Fork the repository
2.  Create a feature branch: `git checkout -b feature/improvement`
3.  Make your changes following the code style
4.  Add tests for new functionality
5.  Commit with descriptive messages
6.  Push to your fork
7.  Open a Pull Request

**Code Style:**
*   Follow PEP 8 conventions
*   Use type hints where possible
*   Add docstrings for public functions
*   Keep functions focused and small

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Credits & Acknowledgments

*   **Developer:** Paras Chamoli
*   **Framework:** Bindu - Agent deployment platform
*   **Agent Framework:** Agno - AI agent toolkit
*   **Research Engine:** Exa - Advanced research API
*   **Reasoning Tools:** Agno ReasoningTools for critical analysis

## 🔗 Useful Links
*   🌐 **Bindu Directory:** [bindus.directory](https://bindus.directory)
*   📚 **Bindu Docs:** [docs.getbindu.com](https://docs.getbindu.com)
*   🐙 **GitHub:** [github.com/ParasChamoli/deep-research-agent](https://github.com/ParasChamoli/deep-research-agent)
*   💬 **Discord:** Bindu Community

<br/>

<p align="center">
  <strong>Built with ❤️ by Paras Chamoli</strong><br/>
  <em>Transforming research with AI-powered deep investigation</em>
</p>

<p align="center">
  <a href="https://github.com/ParasChamoli/deep-research-agent/stargazers">⭐ Star on GitHub</a> •
  <a href="https://bindus.directory">🌐 Register on Bindu</a> •
  <a href="https://github.com/ParasChamoli/deep-research-agent/issues">🐛 Report Issues</a>
</p>

---
*Note: This agent specializes in deep, comprehensive research with automatic citation tracking. It follows a multi-step methodology for thorough investigation and evidence-based conclusions. Powered by Exa for advanced research capabilities.*
