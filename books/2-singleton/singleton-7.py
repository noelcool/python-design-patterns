# 인프라 상태를 확인하는 서비스


class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("1")
        self._servers.append("2")
        self._servers.append("3")
        self._servers.append("4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("5")

    @property
    def servers(self):
        return self._servers


hc1 = HealthCheck()
hc2 = HealthCheck()

print("schedule health check for servers 1")
hc1.addServer()
for i in range(4):
    print("checking ", hc1.servers[i])

print("schedule health check for servers 2")
hc2.changeServer()
for i in range(4):
    print("checking", hc2._servers[i])