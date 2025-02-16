# TattleTell: Distributed Maintenance Logger

TattleTell is a mobile application designed to simplify the process of reporting and tracking public maintenance issues such as potholes, broken streetlights, litter, and overflowing trash cans.

## **MVP Features**
- **Location-Based Logging:** Uses GPS to automatically log maintenance issues based on the user's location.
- **User-Friendly Interface:** Streamlined experience—users only need to take a picture.
- **Automated Trash Can Detection:**
  - Uses an AI model to determine if a trash can is full.
  - Another AI model, in tandem with geolocation data, identifies which trash can is being photographed.

## **Future Extensions**
- **Litter Detection:** AI model to recognize and categorize litter in images.
- **Road and Pothole Detection:** AI-based identification of road damage.
- **Streetlight Status Detection:** Image analysis to determine if a streetlight is malfunctioning.

---

## **Project Structure**

### **TrashCanAPI Folder**
- Contains the Flask-based API responsible for:
  - Loading and running two machine learning models.
  - Receiving images, latitude, and longitude data from the mobile app.
  - Updating the database with new reports.

### **Trash Cans Cleaned Folder (Symlink)**
- Stores images of trash cans in the database for model training and validation.

### **Backend & Frontend Folders**
- **Backend:**
  - Manages communication between the mobile app and TrashCanAPI.
  - Handles data processing and retrieval.
- **Frontend:**
  - Mobile application interface.
  - Captures images and location data, then sends them to TrashCanAPI for processing and database updates.

---

## **Setup & Installation**
### **Prerequisites**
- Python 3.x
- Flask
- Machine Learning Model Dependencies (e.g., TensorFlow/PyTorch, OpenCV)
- Database (SQLite, PostgreSQL, or other as required)

### **Installation Steps**
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/tattletell.git
   cd tattletell
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Start the API server:
   ```sh
   python trashcan_api.py
   ```
4. Run the mobile app (setup instructions vary by platform).

---

## **Usage**
1. Open the TattleTell app.
2. Take a picture of the maintenance issue.
3. The app automatically logs the location and identifies the object.
4. The report is sent to the database for further action.

---

## **Contributing**
Pull requests are welcome. For major changes, please open an issue first to discuss proposed modifications.

---

## **License**
This project is licensed under the MIT License.

---

For any questions or support, please contact [kent.romero78@gmail.com](mailto:your-email@example.com).