
from agents.mcp import MCPServerSse, MCPServerStdio


class ExtendedMCPServerStdio(MCPServerStdio):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Initialize the parent class

    async def list_resources(self):
        return (await self.session.list_resources()).resources

    async def get_resource(self, uri):
        return (await self.session.read_resource(uri)).contents

class ExtendedMCPServerSse(MCPServerSse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Initialize the parent class

    async def list_resources(self):
        return (await self.session.list_resources()).resources

    async def get_resource(self, uri):
        return (await self.session.read_resource(uri)).contents