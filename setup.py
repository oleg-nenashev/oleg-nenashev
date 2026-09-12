from setuptools import setup, find_packages

setup(
    name="mkdocs-webmcp",
    version="0.1.0",
    description="WebMCP Model Context Protocol (MCP) plugin and server for MkDocs",
    packages=find_packages(),
    package_data={
        "mkdocs_webmcp": ["assets/*"],
    },
    include_package_data=True,
    entry_points={
        "mkdocs.plugins": [
            "webmcp = mkdocs_webmcp.plugin:WebMCPPlugin",
        ],
        "console_scripts": [
            "webmcp-server = mkdocs_webmcp.server:main",
        ],
    },
    install_requires=[
        "mkdocs>=1.5.0",
        "mcp>=1.0.0",
        "pyyaml>=6.0",
    ],
)
