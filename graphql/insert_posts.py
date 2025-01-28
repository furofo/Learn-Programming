from app import app, db
from api.models import Post
from datetime import datetime

with app.app_context():
    # Create some posts
    post1 = Post(title="First Post", description="This is the first post", created_at=datetime.now())
    post2 = Post(title="Second Post", description="This is the second post", created_at=datetime.now())

    # Add posts to the session
    db.session.add(post1)
    db.session.add(post2)

    # Commit the session to the database
    db.session.commit()

    print("Posts have been added to the database.")