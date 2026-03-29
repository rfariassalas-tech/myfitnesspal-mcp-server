import os
import logging

from mcp.server.transport_security import TransportSecuritySettings

# Reutilizamos el MCP ya definido en el servidor original
from mfp_mcp.server import mcp

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mfp_mcp_chatgpt")

# Permitir el dominio público de Railway
mcp.transport_security = TransportSecuritySettings(
    enable_dns_rebinding_protection=True,
    allowed_hosts=[
        "127.0.0.1:*",
        "localhost:*",
        "myfitnesspal-mcp-server-production.up.railway.app",
    ],
    allowed_origins=[
        "http://127.0.0.1:*",
        "http://localhost:*",
        "https://myfitnesspal-mcp-server-production.up.railway.app",
    ],
)

if __name__ == "__main__":
    logger.info("Starting MyFitnessPal MCP server for ChatGPT")

    # Railway necesita escuchar en todas las interfaces y usar PORT dinámico
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = int(os.getenv("PORT", "8000"))

    # Ejecutar en modo remoto compatible con ChatGPT
    mcp.run(transport="streamable-http")
