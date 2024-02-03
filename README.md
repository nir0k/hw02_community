# Yatube: A Platform for Publishing Posts

## Choose Your Language

- [English](README.md)
- [Русский](README.ru.md)

---

## About The Project

Yatube is a platform designed for creating and editing entries, as well as publishing them in communities. It is a space where users can share their thoughts, ideas, and creativity with a wide audience. The platform allows authors to showcase their posts on a personal page, which is automatically created upon account registration. All posts on the author's page are sorted from newest to oldest, providing easy access to the latest publications.

### Key Features:

- **Post Creation and Editing:** Users can create new posts and edit existing ones.
- **Publication in Communities:** Posts can be published in various communities created by the site administrator.
- **Author's Personal Page:** The author's page displays general information about them and all their posts.
- **Post Sorting:** Posts on the personal page are displayed in order from newest to oldest.

### Technologies

- Django
- Python
- HTML & CSS

### Project Setup

1. **Clone the repository:**
    ```sh
    git clone git@github.com:nir0k/hw02_community.git
    cd hw02_community
    ```
2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```
3. **Install dependencies:**
    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. **Apply migrations:**
    ```sh
    cd yatube
    python3 manage.py migrate
    ```
5. **Start the project:**
    ```sh
    python3 manage.py runserver
    ```