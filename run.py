from sqlalchemy import exc

from app import create_app,db
from app.auth.models import User
from app.catalog import Book, Publication

flask_app = create_app('prod')
with flask_app.app_context():
    p1 = Publication("Oxford Publications")
    p2 = Publication("Paramount Press")
    p3 = Publication("Oracle Books Inc")
    p4 = Publication("Vintage Books and Comics")
    p5 = Publication("Trolls Press")
    p6 = Publication("Broadway Press")
    p7 = Publication("Downhill Publishers")
    p8 = Publication("Kingfisher Inc")
    db.session.add_all([p2, p3, p4, p5, p6, p7, p8])

    b1 = Book("Miky's Delivery Service", "William Dobelli", 3.9, "ePub", "broom-145379.svg", 123, 1)
    b2 = Book("The Secret Life of Walter Kitty", "Kitty Stiller", 4.1, "Hardcover", "cat-150306.svg", 133, 1)
    b3 = Book("The Empty Book of Life", "Roy Williamson", 4.2, "eBook", "book-life-34063.svg", 153, 1)
    b4 = Book("Life After Dealth", "Nikita Kimmel", 3.8, "Paperback", "mummy-146868.svg", 175, 2)
    b5 = Book("The Legend of Dracula", "Charles Rowling", 4.6, "Hardcover", "man-37603.svg", 253, 2)
    b6 = Book("Taming Dragons", "James Vonnegut", 4.5, "MassMarket Paperback", "dragon-23164.svg", 229, 2)
    b7 = Book("The Singing Magpie", "Oscar Steinbeck", 5, "Hardcover", "magpie-147852.svg", 188, 3)
    b8 = Book("Mr. Incognito", "Amelia Funke", 4.2, "Hardcover", "incognito-160143.svg", 205, 3)
    b9 = Book("A Dog without purpose", "Edgar Dahl", 4.8, "MassMarket Paperback", "dog-159271.svg", 300, 4)
    b10 = Book("A Frog's Life", "Herman Capote", 3.9, "MassMarket Paperback", "amphibian-150342.svg", 190, 4)
    b11 = Book("Logan Returns", "Margaret Elliot", 4.6, "Hardcover", "wolf-153648.svg", 279, 5)
    b12 = Book("Thieves of Kaalapani", "Mohit Gustav", 4.1, "Paperback", "boat-1296201.svg", 270, 5)
    b13 = Book("As Men Thinketh", "Edward McPhee", 4.5, "Paperback", "cranium-2028555.svg", 124, 6)
    b14 = Book("Mathematics of Music", "Mary Turing", 4.5, "Hardcover", "music-306008.svg", 120, 6)
    b15 = Book("The Mystery of Mandalas", "Jack Morrison", 4.2, "Paperback", "mandala-1817599.svg", 221, 6)
    b16 = Book("The Sacred Book of Kairo", "Heidi Zimmerman", 3.8, "ePub", "book-1294676.svg", 134, 7)
    b17 = Book("Love is forever, As Long as it lasts", "Kovi O'Hara", 4.5, "Hardcover", "love-2026554.svg", 279, 8)
    b18 = Book("Order in Chaos", "Wendy Sherman", 3.5, "MassMarket Paperback", "chaos-1769656.svg", 140, 8)
    db.session.add_all([b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18])
    db.session.commit()
    db.create_all()
    try:
        if not User.query.filter_by(user_name = 'harshini').first():
            User.create_user(user='harshini',email= 'harshinis@gmail.com',password='python')

    except exc.IntegrityError:
        flask_app.run()
