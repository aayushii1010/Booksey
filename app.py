import streamlit as st
import random
import base64

# ----------------------------------
# BOOKSY DATABASE
# ----------------------------------

book_database = {
    "📖 Fiction": {
        "Cozy": [
            "The House in the Cerulean Sea by TJ Klune",
            "Legends & Lattes by Travis Baldree",
            "A Psalm for the Wild-Built by Becky Chambers",
            "Anne of Green Gables by L.M. Montgomery"
        ],
        "Romance": [
            "The Love Hypothesis by Ali Hazelwood",
            "Better Than the Movies by Lynn Painter",
            "Book Lovers by Emily Henry",
            "The Spanish Love Deception by Elena Armas"
        ],
        "Thrilling": [
            "The Silent Patient by Alex Michaelides",
            "Gone Girl by Gillian Flynn",
            "Behind Closed Doors by B.A. Paris",
            "The Girl on the Train by Paula Hawkins"
        ],
        "Fantasy": [
            "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
            "The Hobbit by J.R.R. Tolkien",
            "Fourth Wing by Rebecca Yarros",
            "Six of Crows by Leigh Bardugo"
        ],
        "Sci-Fi": [
            "Project Hail Mary by Andy Weir",
            "Dune by Frank Herbert",
            "The Martian by Andy Weir",
            "Ender's Game by Orson Scott Card"
        ]
    },

    "🧠 Non-Fiction": {
        "Inspiring": [
            "Atomic Habits by James Clear",
            "The Alchemist by Paulo Coelho",
            "Shoe Dog by Phil Knight",
            "Ikigai by Héctor García"
        ],
        "Self-Help": [
            "Think Like a Monk by Jay Shetty",
            "The Mountain Is You by Brianna Wiest",
            "Deep Work by Cal Newport",
            "The Psychology of Money by Morgan Housel"
        ],
        "Business": [
            "Zero to One by Peter Thiel",
            "The Lean Startup by Eric Ries",
            "Rich Dad Poor Dad by Robert Kiyosaki",
            "Good to Great by Jim Collins"
        ]
    }
}
# ----------------------------------
# BOOK COVERS
# ----------------------------------

book_covers = {

    # Cozy
    "The House in the Cerulean Sea by TJ Klune":
        "book_covers/house_cerulean_sea.jpg",

    "Legends & Lattes by Travis Baldree":
        "book_covers/legends_lattes.jpg",

    "A Psalm for the Wild-Built by Becky Chambers":
        "book_covers/psalm_wild_built.jpg",

    "Anne of Green Gables by L.M. Montgomery":
        "book_covers/anne_green_gables.jpg",


    # Romance
    "The Love Hypothesis by Ali Hazelwood":
        "book_covers/love_hypothesis.jpg",

    "Better Than the Movies by Lynn Painter":
        "book_covers/better_than_movies.jpg",

    "Book Lovers by Emily Henry":
        "book_covers/book_lovers.jpg",

    "The Spanish Love Deception by Elena Armas":
        "book_covers/spanish_love_deception.jpg",


    # Thrilling
    "The Silent Patient by Alex Michaelides":
        "book_covers/silent_patient.jpg",

    "Gone Girl by Gillian Flynn":
        "book_covers/gone_girl.jpg",

    "Behind Closed Doors by B.A. Paris":
        "book_covers/behind_closed_doors.jpg",

    "The Girl on the Train by Paula Hawkins":
        "book_covers/girl_on_train.jpg",


    # Fantasy
    "Harry Potter and the Sorcerer's Stone by J.K. Rowling":
        "book_covers/harry_potter.jpg",

    "The Hobbit by J.R.R. Tolkien":
        "book_covers/hobbit.jpg",

    "Fourth Wing by Rebecca Yarros":
        "book_covers/fourth_wing.jpg",

    "Six of Crows by Leigh Bardugo":
        "book_covers/six_of_crows.jpg",


    # Sci-Fi
    "Project Hail Mary by Andy Weir":
        "book_covers/project_hail_mary.jpg",

    "Dune by Frank Herbert":
        "book_covers/dune.jpg",

    "The Martian by Andy Weir":
        "book_covers/martian.jpg",

    "Ender's Game by Orson Scott Card":
        "book_covers/enders_game.jpg",


    # Inspiring
    "Atomic Habits by James Clear":
        "book_covers/atomic_habits.jpg",

    "The Alchemist by Paulo Coelho":
        "book_covers/alchemist.jpg",

    "Shoe Dog by Phil Knight":
        "book_covers/shoe_dog.jpg",

    "Ikigai by Héctor García":
        "book_covers/ikigai.jpg",


    # Self Help
    "Think Like a Monk by Jay Shetty":
        "book_covers/think_like_monk.jpg",

    "The Mountain Is You by Brianna Wiest":
        "book_covers/mountain_is_you.jpg",

    "Deep Work by Cal Newport":
        "book_covers/deep_work.jpg",

    "The Psychology of Money by Morgan Housel":
        "book_covers/psychology_money.jpg",


    # Business
    "Zero to One by Peter Thiel":
        "book_covers/zero_to_one.jpg",

    "The Lean Startup by Eric Ries":
        "book_covers/lean_startup.jpg",

    "Rich Dad Poor Dad by Robert Kiyosaki":
        "book_covers/rich_dad_poor_dad.jpg",

    "Good to Great by Jim Collins":
        "book_covers/good_to_great.jpg"
}

book_descriptions = {

    "The House in the Cerulean Sea by TJ Klune":
    "🌈 A heartwarming magical story about found family and acceptance.",

    "Legends & Lattes by Travis Baldree":
    "☕ Cozy fantasy about an orc opening a coffee shop.",

    "A Psalm for the Wild-Built by Becky Chambers":
    "🤖 A thoughtful journey about purpose, humanity, and friendship.",

    "Anne of Green Gables by L.M. Montgomery":
    "🌸 A charming classic following imaginative Anne through life.",

    "The Love Hypothesis by Ali Hazelwood":
    "💕 Fake dating, academic rivals, and plenty of chemistry.",

    "Better Than the Movies by Lynn Painter":
    "🎬 A sweet rom-com perfect for lovers of happy endings.",

    "Book Lovers by Emily Henry":
    "📚 A witty romance between two people who love books.",

    "The Spanish Love Deception by Elena Armas":
    "💃 Fake dating, slow burn romance, and lots of tension.",

    "The Silent Patient by Alex Michaelides":
    "🔪 A psychological thriller with a shocking twist.",

    "Gone Girl by Gillian Flynn":
    "🕵️ Dark, gripping thriller full of secrets and lies.",

    "Behind Closed Doors by B.A. Paris":
    "🚪 A chilling suspense novel that keeps you guessing.",

    "The Girl on the Train by Paula Hawkins":
    "🚆 Mystery and suspense told through unreliable memories.",

    "Harry Potter and the Sorcerer's Stone by J.K. Rowling":
    "⚡ The magical beginning of Harry's Hogwarts journey.",

    "The Hobbit by J.R.R. Tolkien":
    "🧙 An epic fantasy adventure filled with dragons and treasure.",

    "Fourth Wing by Rebecca Yarros":
    "🐉 Dragons, danger, romance, and thrilling competition.",

    "Six of Crows by Leigh Bardugo":
    "💰 A clever fantasy heist with unforgettable characters.",

    "Project Hail Mary by Andy Weir":
    "🚀 A thrilling space mission to save humanity.",

    "Dune by Frank Herbert":
    "🏜️ Political intrigue, destiny, and epic science fiction.",

    "The Martian by Andy Weir":
    "🌌 Survival, science, and humor on Mars.",

    "Ender's Game by Orson Scott Card":
    "🛰️ A brilliant young strategist prepares for an alien war.",

    "Atomic Habits by James Clear":
    "📈 Learn how tiny habits create remarkable results.",

    "The Alchemist by Paulo Coelho":
    "✨ An inspiring tale about following your dreams.",

    "Shoe Dog by Phil Knight":
    "👟 The fascinating story behind Nike's success.",

    "Ikigai by Héctor García":
    "🌿 Discover the Japanese secret to a meaningful life.",

    "Think Like a Monk by Jay Shetty":
    "🧘 Wisdom and habits inspired by monk life.",

    "The Mountain Is You by Brianna Wiest":
    "⛰️ A guide to overcoming self-sabotage and growing.",

    "Deep Work by Cal Newport":
    "🎯 Master focus and productivity in a distracted world.",

    "The Psychology of Money by Morgan Housel":
    "💰 Timeless lessons about wealth and financial behavior.",

    "Zero to One by Peter Thiel":
    "🚀 Learn how innovative startups create the future.",

    "The Lean Startup by Eric Ries":
    "📊 Build businesses smarter through experimentation.",

    "Rich Dad Poor Dad by Robert Kiyosaki":
    "🏦 Financial lessons that challenge traditional thinking.",

    "Good to Great by Jim Collins":
    "🏆 Discover what makes companies truly exceptional."
}

book_explanations = {

    "The House in the Cerulean Sea by TJ Klune":
    "A heartwarming and magical story filled with found family, kindness, and comfort.",

    "Legends & Lattes by Travis Baldree":
    "Perfect for cozy readers who enjoy warm friendships, coffee shops, and low-stakes fantasy adventures.",

    "A Psalm for the Wild-Built by Becky Chambers":
    "A thoughtful and peaceful journey about purpose, self-discovery, and finding happiness in small moments.",

    "Anne of Green Gables by L.M. Montgomery":
    "A charming classic full of imagination, optimism, and wholesome comfort.",

    "The Love Hypothesis by Ali Hazelwood":
    "A fun and heartwarming romance with lovable characters and plenty of chemistry.",

    "Better Than the Movies by Lynn Painter":
    "A lighthearted rom-com that captures the excitement and awkwardness of first love.",

    "Book Lovers by Emily Henry":
    "A witty and emotional romance perfect for readers who love books and clever banter.",

    "The Spanish Love Deception by Elena Armas":
    "A slow-burn romance packed with tension, humor, and unforgettable moments.",

    "The Silent Patient by Alex Michaelides":
    "A gripping psychological thriller filled with twists that keep readers guessing.",

    "Gone Girl by Gillian Flynn":
    "A dark and suspenseful thriller known for its shocking surprises and unreliable characters.",

    "Behind Closed Doors by B.A. Paris":
    "A tense and addictive psychological thriller that keeps the suspense high.",

    "The Girl on the Train by Paula Hawkins":
    "A mystery filled with secrets, twists, and unreliable perspectives.",

    "Harry Potter and the Sorcerer's Stone by J.K. Rowling":
    "A magical adventure filled with friendship, wonder, and unforgettable discoveries.",

    "The Hobbit by J.R.R. Tolkien":
    "A timeless fantasy quest packed with adventure, courage, and imagination.",

    "Fourth Wing by Rebecca Yarros":
    "An action-packed fantasy featuring dragons, danger, and intense relationships.",

    "Six of Crows by Leigh Bardugo":
    "A thrilling fantasy heist with clever characters and high-stakes adventures.",

    "Project Hail Mary by Andy Weir":
    "A clever sci-fi adventure combining science, humor, and suspense.",

    "Dune by Frank Herbert":
    "An epic science fiction masterpiece exploring power, destiny, and survival.",

    "The Martian by Andy Weir":
    "A smart and entertaining survival story driven by science and determination.",

    "Ender's Game by Orson Scott Card":
    "A thought-provoking sci-fi novel about strategy, leadership, and sacrifice.",

    "Atomic Habits by James Clear":
    "Perfect for readers looking to build better habits through practical and proven techniques.",

    "The Alchemist by Paulo Coelho":
    "An inspiring story about dreams, purpose, and following your heart.",

    "Shoe Dog by Phil Knight":
    "A fascinating entrepreneurial journey behind the creation of Nike.",

    "Ikigai by Héctor García":
    "A calming exploration of finding meaning and joy in everyday life.",

    "Think Like a Monk by Jay Shetty":
    "Offers practical wisdom for mindfulness, happiness, and personal growth.",

    "The Mountain Is You by Brianna Wiest":
    "An insightful guide to overcoming self-sabotage and achieving growth.",

    "Deep Work by Cal Newport":
    "Perfect for improving focus, productivity, and meaningful work habits.",

    "The Psychology of Money by Morgan Housel":
    "Explains financial success through behavior, decision-making, and mindset.",

    "Zero to One by Peter Thiel":
    "A bold look at innovation, startups, and building the future.",

    "The Lean Startup by Eric Ries":
    "Teaches practical methods for building successful businesses efficiently.",

    "Rich Dad Poor Dad by Robert Kiyosaki":
    "Introduces key financial concepts and wealth-building principles.",

    "Good to Great by Jim Collins":
    "Explores what separates exceptional companies from average ones."
}
# ----------------------------------
# QUOTES
# ----------------------------------

quotes = [
"📖 A reader lives a thousand lives before he dies.",
"🌸 Books and coffee make everything better.",
"✨ Reading is dreaming with open eyes.",
"💜 Between the pages of a book is a lovely place to be.",
"🌼 One more chapter never hurt anybody."
]

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Booksy",
    page_icon="📚",
    layout="centered"
)
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
bg_image = get_base64("assets/background.jpg")

st.markdown(f"""
<style>

[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    inset: 0;
    backdrop-filter: blur(8px);
    background: rgba(0,0,0,0.35);
    z-index: -1;
}}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Sidebar */

[data-testid="stSidebar"] {{
    background: rgba(20, 15, 10, 0.92);
    backdrop-filter: blur(12px);
}}
 /* Sidebar Shadow */

[data-testid="stSidebar"] {
    box-shadow: 5px 0 30px rgba(0,0,0,0.3);
    border-right: 1px solid rgba(255,255,255,0.1);
}           
section.main > div {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);

    border: 1px solid rgba(255,255,255,0.15);

    box-shadow:
        0 8px 32px rgba(0,0,0,0.25),
        inset 0 1px rgba(255,255,255,0.12);

    border-radius: 25px;
    padding: 2rem;
}
            div[data-testid="stVerticalBlock"] > div:has(img) {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 20px;

    padding: 10px;

    margin-bottom: 20px;

    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
}
            div[data-testid="stVerticalBlock"] > div:has(img):hover {
    transform: translateY(-4px);

    box-shadow: 0 15px 35px rgba(0,0,0,0.25);

    transition: all 0.3s ease;
}
h1 {
    color: #e8c86a !important;
    text-shadow:
        0 0 6px rgba(255,215,120,0.25),
        0 0 12px rgba(255,215,120,0.15);
}
[data-testid="stAppViewContainer"]::after {
    content: "";

    position: fixed;

    top: 0;
    left: 0;

    width: 100%;
    height: 100%;

    background-image:
        radial-gradient(circle at 15% 20%, rgba(255,215,120,0.08) 0%, transparent 8%),
        radial-gradient(circle at 80% 30%, rgba(255,180,220,0.08) 0%, transparent 10%),
        radial-gradient(circle at 60% 80%, rgba(255,230,180,0.06) 0%, transparent 8%);

    pointer-events: none;

        z-index: -1;
}
.stTextInput input {
    background: rgba(255,255,255,0.08) !important;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 15px;
}
.stTextInput input:focus {
    border: 1px solid #ffd76b !important;
    box-shadow: 0 0 15px rgba(255,215,120,0.4);
}
            .stTextInput input {
    background: rgba(255,255,255,0.08) !important;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 15px;
}

/* Mood Pills */

div[role="radiogroup"] {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 12px;
}

div[role="radiogroup"] label {
    background: rgba(255,255,255,0.08) !important;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 999px !important;

    padding: 10px 18px !important;

    transition: all 0.3s ease;
}

div[role="radiogroup"] label:hover {
    transform: translateY(-3px);
    background: rgba(255,215,120,0.15) !important;
    box-shadow: 0 6px 20px rgba(255,215,120,0.2);
}

div[role="radiogroup"] label:has(input:checked) {
    background: rgba(255,215,120,0.22) !important;
    border: 1px solid rgba(255,215,120,0.5);
    box-shadow: 0 0 18px rgba(255,215,120,0.25);
}

.stButton > button {
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(255,215,120,0.5);
}

[data-testid="stAlert"] {
    background: rgba(120,180,150,0.15);
    backdrop-filter: blur(10px);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.1);
}
            
/* Sidebar text */

[data-testid="stSidebar"] * {{
    color: #f5e6c8 !important;
}}
@keyframes twinkle {
    0% { opacity: 0.3; }
    50% { opacity: 1; }
    100% { opacity: 0.3; }
}

.sparkle {
    position: fixed;
    color: rgba(255,255,255,0.4);
    animation: twinkle 3s infinite;
    pointer-events: none;
    z-index: 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sparkle" style="top:12%; left:18%;">✨</div>
<div class="sparkle" style="top:22%; left:35%;">⭐</div>
<div class="sparkle" style="top:15%; left:62%;">✨</div>
<div class="sparkle" style="top:28%; left:82%;">⭐</div>

<div class="sparkle" style="top:45%; left:12%;">🌙</div>
<div class="sparkle" style="top:52%; left:30%;">✨</div>
<div class="sparkle" style="top:60%; left:72%;">⭐</div>

<div class="sparkle" style="top:78%; left:18%;">✨</div>
<div class="sparkle" style="top:82%; left:50%;">🌙</div>
<div class="sparkle" style="top:75%; left:88%;">⭐</div>
""", unsafe_allow_html=True)

# ----------------------------------
# THEME TOGGLE
# ----------------------------------

theme = st.sidebar.toggle(
    "🌙 Dark Academia Mode"
)
if theme:

    # DARK ACADEMIA

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #0f0b0b,
            #1a1410,
            #2d1f17
        );
    }

    h1 {
        color: #D4AF37 !important;
        text-align: center;
    }

    h2, h3 {
        color: #E6C78B !important;
    }

    p, label {
        color: #F5E6CC !important;
    }

    section[data-testid="stSidebar"] {
        background: #15100d;
    }

    .stButton > button {
        background: #6B4423 !important;
        color: white !important;
        border-radius: 12px !important;
    }

    </style>
    """, unsafe_allow_html=True)

else:

    # PASTEL THEME

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #FFF8FC 0%,
            #F6EDFF 50%,
            #FFF9D6 100%
        );
    }

    h1 {
        color: #B26CFF !important;
        text-align: center;
    }

    h2, h3 {
        color: #FF7EB6 !important;
    }

    p, label {
        color: #5F4B66 !important;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #FFEAF4,
            #F3E7FF
        );
    }

    .stButton > button {
        background: linear-gradient(
            90deg,
            #FFB7D5,
            #DAB6FF
        ) !important;

        color: #4A3A55 !important;
        border-radius: 12px !important;
    }

    </style>
    """, unsafe_allow_html=True)

# ----------------------------------
# SESSION STATE
# ----------------------------------

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.markdown(
    "## 📚🌸 Booksey"
)
st.sidebar.write("Your Personal AI Book Matcher")

st.sidebar.markdown("---")

st.sidebar.info(
    "Choose a category and vibe to discover your next favorite book!"
)

st.sidebar.markdown("---")

st.sidebar.subheader("❤️ Favorites")
st.sidebar.markdown("---")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Stats")

st.sidebar.metric(
    "❤️ Favorites",
    len(st.session_state.favorites)
)

st.sidebar.metric(
    "📚 Recommendations",
    len(st.session_state.recommendations)
)

st.sidebar.info(
    f"📚 {len(st.session_state.recommendations)} books recommended"
)
if st.session_state.favorites:
    for book in st.session_state.favorites:
        st.sidebar.write(f"📖 {book}")
else:
    st.sidebar.write("No favorites yet.")

# ----------------------------------
# MAIN PAGE
# ----------------------------------

st.markdown(
    "<h1>🌸📚 Booksey 📚🌸</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<div style='text-align:center;
font-size:22px;
letter-spacing:8px;
opacity:0.9;'>
☕ books • blankets • rainy days • magic ✨
</div>
""", unsafe_allow_html=True)

st.caption(
"🌸 Find your next favorite book in the cutest way possible 💜"
)


st.success(
"💖 Welcome to Booksy! Let's find your perfect read ✨"
)


st.subheader("Your Personal AI Book Matcher")

st.success(random.choice(quotes))

st.write(
    "Discover books based on your mood, interests, and reading preferences."
)
# ----------------------------------
# SEARCH BOOKS
# ----------------------------------

st.markdown("### 🔍 Find Your Next Favourite Book")

search = st.text_input(
    "Search by title"
)

if search:

    results = []

    for category in book_database:
        for vibe in book_database[category]:
            for book in book_database[category][vibe]:

                if search.lower() in book.lower():
                    results.append(book)

    if results:

        st.success(
            f"Found {len(results)} book(s)"
        )

        for book in results:
            st.write(f"📚 {book}")

    else:
        st.warning("No books found.")
# ----------------------------------
# MOOD
# ----------------------------------

st.markdown("### 🤖 How are you feeling today?")

mood = st.radio(
    "",
    ["😊 Happy", "😌 Relaxed", "🔥 Excited", "🥺 Emotional"]
)

if mood == "😊 Happy":
    st.success("Perfect day for Romance and Cozy reads!")

elif mood == "😌 Relaxed":
    st.success("Cozy books are calling your name!")

elif mood == "🔥 Excited":
    st.success("Thrillers and Fantasy await!")

elif mood == "🥺 Emotional":
    st.success("Romance and Inspiring reads might be perfect.")


# ----------------------------------
# READING COMPANION
# ----------------------------------

st.markdown("### ☕ What's your reading companion?")

drink = st.selectbox(
    "Choose your drink",
    [
        "☕ Coffee",
        "🍵 Tea",
        "🍫 Hot Chocolate",
        "🥤 Iced Drink"
    ],
    key="drink_select",
    label_visibility="collapsed"
)
# ----------------------------------
# READING CHALLENGE
# ----------------------------------

st.markdown("### 🎯 Reading Challenge")
books_read = st.slider(
    "Books read this year",
    0,
    50,
    5,
    key="reading_challenge"
)

st.progress(
    books_read / 50
)

st.write(
    f"📚 {books_read}/50 books completed"
)

# ----------------------------------
# CATEGORY
# ----------------------------------

category = st.selectbox(
    "Choose a Category",
    list(book_database.keys())
)

# ----------------------------------
# VIBE
# ----------------------------------

vibe = st.selectbox(
    "Choose a Vibe",
    list(book_database[category].keys())
)
# ----------------------------------
# SURPRISE ME
# ----------------------------------

if st.button("🎲 Surprise Me"):

    all_books = []

    for category in book_database:
        for vibe in book_database[category]:
            all_books.extend(
                book_database[category][vibe]
            )

    surprise_book = random.choice(all_books)

    st.success(
        f"✨ Surprise Pick: {surprise_book}"
    )
# ----------------------------------
# GENERATE RECOMMENDATIONS
# ----------------------------------

if st.button("✨ Find My Books"):

    st.session_state.recommendations = random.sample(
        book_database[category][vibe],
        min(4, len(book_database[category][vibe]))
    )

# ----------------------------------
# DISPLAY RECOMMENDATIONS
# ----------------------------------

    if st.session_state.recommendations:

        st.success("Here are your recommendations!")

        st.caption(
            f"Showing {len(st.session_state.recommendations)} recommendations"
        )

        for book in st.session_state.recommendations:

            st.markdown("---")

            st.markdown('<div class="book-card">', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 3])

            with col1:
                if book in book_covers:
                    st.image(book_covers[book], width=170)
                
            with col2:
                st.markdown(
                  f"<h3>📚 {book}</h3>",
                   unsafe_allow_html=True
    )
                
                if book in book_descriptions:
                 st.caption(book_descriptions[book])

                if book in book_explanations:
                 st.info(
                   f"✨ Why this book matches you\n\n{book_explanations[book]}"
        )


                if st.button(
                     "❤️ Add to Favorites",
                    key=f"fav_{book}"
                    ):
                        if book not in st.session_state.favorites:
                            st.session_state.favorites.append(book)
                            st.toast("📚 Added to Favorites!", icon="💖")
                        st.rerun()
                        
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("---")

st.markdown(
    "<center>Made with ❤️ by Yushi using Python & Streamlit</center>",
    unsafe_allow_html=True
)
