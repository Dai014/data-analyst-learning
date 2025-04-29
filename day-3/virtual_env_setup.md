# Virtual Environment Setup Instructions

To set up a virtual environment for your data analyst learning project, follow these steps:

1. **Install Virtualenv** (if not already installed):
   Open your terminal and run the following command:
   ```
   pip install virtualenv
   ```

2. **Create a Virtual Environment**:
   Navigate to your project directory and create a virtual environment by running:
   ```
   virtualenv venv
   ```
   This will create a new directory named `venv` in your project folder.

3. **Activate the Virtual Environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install Required Packages**:
   Once the virtual environment is activated, you can install the necessary packages for your project. For this project, you will need Pandas and Flask. Run the following command:
   ```
   pip install pandas flask
   ```

5. **Deactivate the Virtual Environment**:
   When you are done working, you can deactivate the virtual environment by simply running:
   ```
   deactivate
   ```

6. **Reactivating the Virtual Environment**:
   Whenever you return to your project, remember to activate the virtual environment again using the activation command from step 3.

By following these steps, you will have a clean environment to work on your data analyst learning project without interfering with other Python projects on your system.