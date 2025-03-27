from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional

class Group(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, nullable=False)
    header: str = Field(max_length=255, nullable=False)
    footer: str = Field(max_length=255, nullable=False)

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.database = name
        self.user = user
        self.password = password
        self.engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{name}")
        self.session = None

    def get_group_list(self):
        group_list = []
        with Session(self.engine) as session:
            statement = select(Group)
            results = session.exec(statement)
            for group in results:
                group_list.append(Group(
                    id=str(group.id),
                    name=group.name,
                    header=group.header,
                    footer=group.footer
                ))
        return group_list

    def destroy(self):
        if hasattr(self, 'session') and self.session:
            self.session.close()
        if hasattr(self, 'engine') and self.engine:
            self.engine.dispose()