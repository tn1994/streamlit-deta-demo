from deta import Deta


class DetaService:
    """
    ref:
        https://docs.deta.sh/docs/base/py_tutorial/
        https://youtu.be/3egaMfE9388
    """

    def __init__(self, project_key: str, db_name: str):
        deta = Deta(project_key=project_key)  # configure your Deta project
        self.db = deta.Base(name=db_name)  # access your DB

    def create(self, name, age, hometown):
        return self.db.put({
            "name": name,
            "age": age,
            "hometown": hometown
        })

    def read(self, key):
        return self.db.get(key=key)

    def update(self, data, key):
        return self.db.put(data=data, key=key)

    def delete(self, key):
        return self.db.delete(key)

    def fetch(self, query=None, limit: int = 1000, last=None):
        return self.db.fetch(query=query, limit=limit, last=last)
