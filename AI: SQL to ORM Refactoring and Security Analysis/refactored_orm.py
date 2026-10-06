from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.exc import SQLAlchemyError


# Base class for ORM models
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"


# Engine and table creation
DATABASE_URL = "mysql+mysqlconnector://root:yourpassword@localhost/example_db"
engine = create_engine(DATABASE_URL, echo=False)

Base.metadata.create_all(engine)


def create_user(username: str, email: str):
    """Create a new user."""
    if not username or not email:
        print("Username and email are required.")
        return

    with Session(engine) as session:
        try:
            user = User(username=username, email=email)
            session.add(user)
            session.commit()
            print(f"User '{username}' created successfully.")
            return user
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error creating user: {e}")


def get_user_by_username(username: str):
    """Fetch one user by username."""
    with Session(engine) as session:
        try:
            stmt = select(User).where(User.username == username)
            return session.scalar(stmt)
        except SQLAlchemyError as e:
            print(f"Error fetching user: {e}")
            return None


def update_user_email(username: str, new_email: str):
    """Update a user's email."""
    with Session(engine) as session:
        try:
            user = session.scalar(
                select(User).where(User.username == username)
            )

            if user is None:
                print(f"User '{username}' not found.")
                return

            user.email = new_email
            session.commit()
            print(f"Email updated for '{username}'.")
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error updating email: {e}")


def delete_user(username: str):
    """Delete a user by username."""
    with Session(engine) as session:
        try:
            user = session.scalar(
                select(User).where(User.username == username)
            )

            if user is None:
                print(f"User '{username}' not found.")
                return

            session.delete(user)
            session.commit()
            print(f"User '{username}' deleted.")
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error deleting user: {e}")


def list_users():
    """Return all users."""
    with Session(engine) as session:
        try:
            return session.scalars(select(User)).all()
        except SQLAlchemyError as e:
            print(f"Error listing users: {e}")
            return []


# Create and query a user
create_user("alice", "alice@example.com")

user = get_user_by_username("alice")
print(user)

# Other ORM operations
update_user_email("alice", "alice.new@example.com")
print(get_user_by_username("alice"))

print(list_users())

delete_user("alice")
