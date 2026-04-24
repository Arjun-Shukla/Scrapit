# ♻️ ScrapIt

### Hassle-Free Scrap Selling Platform

ScrapIt is a web-based platform designed to **simplify scrap selling and collection** by connecting users with nearby scrap buyers. It streamlines the entire process - from booking a pickup to managing interactions - through a clean and user-friendly interface.

---

## 🚀 Key Features

* 📦 **Easy Scrap Pickup Booking**
  Users can schedule scrap collection with a single click using the *Book Now* feature.

* 🚚 **Doorstep Scrap Collection**
  Connects users with verified scrap sellers who visit directly for pickup.

* 🔐 **User Authentication System**
  Secure sign-up and login functionality with session management.

* 📧 **Automated Email Notifications**
  Sends confirmations and updates using an integrated email system.

* 🗺️ **Location-Based Services (Planned)**
  Future integration with Google Maps API to locate nearby scrap buyers.

---

## 🧑‍💻 Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Django (Python)
* **Database:** MySQL
* **Email Service:** Python-based mailing system

---

## 📂 Project Structure

```
ScrapIt/
│── templates/
│── static/
│── db.sqlite3 / MySQL config
│── manage.py
```

---

## ⚙️ Installation & Setup

1. Clone the repository

   ```
   git clone https://github.com/Arjun-Shukla/Scrapit.git
   cd scrapit
   ```

2. Create virtual environment

   ```
   python -m venv venv
   source venv/bin/activate   # (Windows: venv\Scripts\activate)
   ```

3. Install dependencies

   ```
   pip install -r requirements.txt
   ```

4. Run migrations

   ```
   python manage.py migrate
   ```

5. Start the server

   ```
   python manage.py runserver
   ```

---

## 🌐 Future Improvements

* 🗺️ Google Maps integration for real-time seller discovery
* 📱 Improved UI/UX and mobile responsiveness
* ⭐ Rating and review system
* 📊 Seller dashboard and analytics

---

## 👨‍💻 Author

**Arjun Shukla**
GitHub: https://github.com/Arjun-Shukla

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
