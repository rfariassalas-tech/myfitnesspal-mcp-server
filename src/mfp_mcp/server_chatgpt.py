import os
import logging

from mcp.server.fastmcp import FastMCP

# Importar el mcp ya definido (esto es clave)
from mfp_mcp.server import mcp

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mfp_mcp_chatgpt")

if __name__ == "__main__":
    logger.info("Starting MyFitnessPal MCP server for ChatGPT")

    # ⚠️ CRÍTICO: Railway necesita esto
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = int(os.getenv("PORT", "8000"))

    # Ejecutar en modo remoto
    mcp.run(transport="streamable-http")
