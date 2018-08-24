from operator import attrgetter

from gino import Gino


db = Gino()


def get_members_query():
    return '''
WITH RECURSIVE graph AS (
  SELECT
    p.id AS person,
    pp.parent AS team,
    p.name AS name,
    p.is_team AS is_team,
    array[parent] AS all_parents
  FROM people p JOIN person_x_person pp
  ON p.id = pp.parent
  WHERE pp.parent = $1

  UNION ALL

  SELECT
    people.id,
    person_x_person.parent,
    people.name,
    people.is_team,
    graph.all_parents
  FROM (people JOIN person_x_person
    ON people.id = person_x_person.child
  ), graph WHERE person_x_person.parent = graph.person
  AND person_x_person.child <> ALL (graph.all_parents)
)
SELECT DISTINCT person, name FROM graph WHERE is_team = false ORDER BY name
'''


class Person(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    is_team = db.Column(db.Boolean, default=False)

    async def get_teams(self, order_by=None):
        relations = await PersonXPerson.query.where(
            PersonXPerson.child == self.id
        ).gino.all()

        team_ids = list(map(attrgetter('parent'), relations))
        query = Person.query

        if order_by:
            query = query.order_by(order_by)

        query = query.where(
            Person.id.in_(team_ids)
        )

        return await query.gino.all()

    async def get_members(self):
        if not self.is_team:
            raise RuntimeError('Attempted to get members of a non-team')

        return await db.bind.all(get_members_query(), self.id)


class PersonXPerson(db.Model):
    __tablename__ = 'person_x_person'

    parent = db.Column(db.Integer, db.ForeignKey('people.id'))
    child = db.Column(db.Integer, db.ForeignKey('people.id'))


async def init_db(app):
    db_config = app['config']['db']

    await db.set_bind(
        'postgresql://{user}:{password}@{host}/{name}'.format(**db_config))
    await db.gino.create_all()
