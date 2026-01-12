# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""deep-research-agent - AI Deep Research Agent with Citation Tracking."""

import argparse
import asyncio
import json
import os
import sys
import traceback
from pathlib import Path
from textwrap import dedent
from typing import Any

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.openrouter import OpenRouter
from agno.tools.exa import ExaTools
from agno.tools.reasoning import ReasoningTools
from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Global agent instance
agent: Agent | None = None
_initialized = False
_init_lock = asyncio.Lock()


class ExaKeyError(ValueError):
    """Exa API key is missing."""


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Try multiple possible locations for agent_config.json
    possible_paths = [
        Path(__file__).parent.parent / "agent_config.json",  # Project root
        Path(__file__).parent / "agent_config.json",  # Same directory
        Path.cwd() / "agent_config.json",  # Current working directory
    ]

    for config_path in possible_paths:
        if config_path.exists():
            try:
                with open(config_path) as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️  Error reading {config_path}: {e}")
                continue

    # If no config found, create a minimal default
    return {
        "name": "deep-research-agent",
        "description": "AI Deep Research Agent with Citation Tracking",
        "version": "1.0.0",
        "deployment": {
            "url": "http://127.0.0.1:3773",
            "expose": True,
            "protocol_version": "1.0.0",
            "proxy_urls": ["127.0.0.1"],
            "cors_origins": ["*"],
        },
        "environment_variables": [
            {"key": "OPENAI_API_KEY", "description": "OpenAI API key", "required": False},
            {"key": "OPENROUTER_API_KEY", "description": "OpenRouter API key", "required": False},
            {"key": "MODEL_NAME", "description": "Model ID for OpenRouter", "required": False},
            {"key": "EXA_API_KEY", "description": "Exa API key", "required": True},
        ],
    }


async def initialize_agent() -> None:
    """Initialize the deep research agent with Exa research tools."""
    global agent

    # Get API keys from environment
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    exa_api_key = os.getenv("EXA_API_KEY")
    model_name = os.getenv("MODEL_NAME", "openai/gpt-4o")

    if not exa_api_key:
        error_msg = "EXA_API_KEY is required. Get it from: https://exa.ai"
        raise ExaKeyError(error_msg)

    # Model selection logic
    if openai_api_key:
        model = OpenAIChat(id="gpt-4o", api_key=openai_api_key)
        print("✅ Using OpenAI GPT-4o")
    elif openrouter_api_key:
        model = OpenRouter(
            id=model_name,
            api_key=openrouter_api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        )
        print(f"✅ Using OpenRouter model: {model_name}")
    else:
        # Define error message separately to avoid TRY003
        error_msg = (
            "No LLM API key provided. Set OPENAI_API_KEY or OPENROUTER_API_KEY environment variable.\n"
            "For OpenRouter: https://openrouter.ai/keys\n"
            "For OpenAI: https://platform.openai.com/api-keys"
        )
        raise ValueError(error_msg)

    # Initialize Exa research tools - REMOVE invalid parameters
    exa_tools = ExaTools(
        api_key=exa_api_key,
    )

    reasoning_tools = ReasoningTools(add_instructions=True)

    # Create the deep research agent
    agent = Agent(
        name="Deep Research Agent",
        model=model,
        tools=[exa_tools, reasoning_tools],
        instructions=dedent("""
            You are an expert research analyst with access to advanced research tools.

            # Research Workflow:
            1. **Research Planning**: Use the think tool to plan your research approach
            2. **Deep Research**: Use the research tool with appropriate parameters
            3. **Analysis & Synthesis**: Use the analyze tool to process findings
            4. **Citation Management**: Always preserve and present citations

            # Tool Usage Guidelines:
            ## Research Tool Parameters:
            - **instructions** (str): The research topic/question
            - **output_schema** (dict, optional): JSON schema for structured output

            ## Schema Handling:
            - When given a schema, pass it as output_schema parameter to research tool
            - If no schema is provided, the tool will auto-infer an appropriate schema
            - Example: If user says "Research X. Use this schema {'type': 'object', ...}", call research tool with the schema

            ## Citation Requirements:
            - Always request citations when using the research tool
            - Preserve all citations provided by the research tool
            - Format citations clearly in your final output
            - Include citations for each data point when presenting tables

            ## Output Structure:
            - Present findings exactly as provided by the research tool
            - Maintain the structure and formatting of the research output
            - Include all citations in appropriate locations
            - Use markdown for clear formatting (tables, lists, headers)

            # Research Best Practices:
            - Be thorough and comprehensive in research
            - Verify information by checking multiple sources
            - Use structured queries when appropriate
            - Provide evidence-based conclusions
            - Acknowledge limitations or uncertainties in findings

            # Important:
            - Always use the research tool for deep research queries
            - The research tool automatically includes citations
            - For simple lookups, you can use other tools, but prefer the research tool for comprehensive analysis
        """),
        expected_output=dedent("""\
            # Research Report: {Research Topic}

            ## Executive Summary
            {High-level overview of research findings with key citations}

            ## Research Methodology
            - Search queries used
            - Sources analyzed
            - Research parameters
            - Date range covered

            ## Detailed Findings

            ### Section 1: {Topic Area 1}
            {Detailed research findings with inline citations [1][2]}

            ### Section 2: {Topic Area 2}
            {Detailed research findings with inline citations [3][4]}

            ### Section 3: {Topic Area 3}
            {Detailed research findings with inline citations [5][6]}

            ## Data & Analysis

            ### Structured Data (if applicable)
            | Metric/Parameter | Value | Source |
            |-----------------|-------|--------|
            | {Data point 1} | {Value 1} | [Citation] |
            | {Data point 2} | {Value 2} | [Citation] |

            ### Comparative Analysis
            {Comparative insights with supporting citations}

            ## Key Insights
            1. {Insight 1 with supporting evidence [citation]}
            2. {Insight 2 with supporting evidence [citation]}
            3. {Insight 3 with supporting evidence [citation]}

            ## Conclusions
            {Evidence-based conclusions with citations}

            ## Citations
            [1] {Full citation details with URL}
            [2] {Full citation details with URL}
            [3] {Full citation details with URL}
            [4] {Full citation details with URL}
            [5] {Full citation details with URL}
            [6] {Full citation details with URL}

            ## Research Limitations
            - Scope limitations
            - Date range limitations
            - Source availability
            - Any other relevant constraints
        """),
        add_datetime_to_context=True,
        markdown=True,
    )
    print("✅ Deep Research Agent initialized")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the agent with the given messages."""
    global agent
    if not agent:
        error_msg = "Agent not initialized"
        raise RuntimeError(error_msg)

    # Run the agent and get response
    response = await agent.arun(messages)
    return response


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages with lazy initialization."""
    global _initialized

    # Lazy initialization on first call
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing Deep Research Agent...")
            await initialize_agent()
            _initialized = True

    # Run the async agent
    result = await run_agent(messages)
    return result


async def cleanup() -> None:
    """Clean up any resources."""
    print("🧹 Cleaning up Deep Research Agent resources...")


def main():
    """Run the main entry point for the Deep Research Agent."""
    parser = argparse.ArgumentParser(description="Bindu Deep Research Agent")
    parser.add_argument(
        "--openai-api-key",
        type=str,
        default=os.getenv("OPENAI_API_KEY"),
        help="OpenAI API key (env: OPENAI_API_KEY)",
    )
    parser.add_argument(
        "--openrouter-api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY)",
    )
    parser.add_argument(
        "--exa-api-key",
        type=str,
        default=os.getenv("EXA_API_KEY"),
        help="Exa API key (env: EXA_API_KEY)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-4o"),
        help="Model ID for OpenRouter (env: MODEL_NAME)",
    )
    args = parser.parse_args()

    # Set environment variables if provided via CLI
    if args.openai_api_key:
        os.environ["OPENAI_API_KEY"] = args.openai_api_key
    if args.openrouter_api_key:
        os.environ["OPENROUTER_API_KEY"] = args.openrouter_api_key
    if args.exa_api_key:
        os.environ["EXA_API_KEY"] = args.exa_api_key
    if args.model:
        os.environ["MODEL_NAME"] = args.model

    print("🔍 Deep Research Agent - AI Research with Citation Tracking")
    print("📚 Capabilities: Deep web research, structured output, automatic citations, analysis")

    # Load configuration
    config = load_config()

    try:
        # Bindufy and start the agent server
        print("🚀 Starting Bindu Deep Research Agent server...")
        print(f"🌐 Server will run on: {config.get('deployment', {}).get('url', 'http://127.0.0.1:3773')}")
        bindufy(config, handler)
    except KeyboardInterrupt:
        print("\n🛑 Agent stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        # Cleanup on exit
        asyncio.run(cleanup())


if __name__ == "__main__":
    main()