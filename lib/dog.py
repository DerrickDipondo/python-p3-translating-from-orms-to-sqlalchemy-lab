from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)  # Add the Dog instance to the session
    session.commit()   # Commit the transaction to save the changes


def get_all(session):
    return session.query(Dog).all()  # Returns a list of all Dog instances


def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()


def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()


def update_breed(session, dog, new_breed):
    dog.breed = new_breed  # Update breed attribute
    session.commit()  # Commit changes to the database
