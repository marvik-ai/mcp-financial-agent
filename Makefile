start-server:
	PYTHONPATH=src fastmcp run src/server/app.py --transport sse --port 9000
start-agent:
	PYTHONPATH=src python  src/financial_agent/agent.py
db-up:
	docker-compose up -d
db-down:
	docker-compose down