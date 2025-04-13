# Gmail Cleaner Pro – Deploy on Render.com

## 🌐 How to Deploy (No Coding Needed)

1. Go to https://render.com
2. Create a free account
3. Click “New” → “Web Service”
4. Connect your GitHub OR upload this zip manually
5. Use the following settings:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn api.server:app --host=0.0.0.0 --port=10000`

6. When deployed, open: https://your-service.onrender.com/docs

Enjoy your live Gmail Cleaner Pro API!
