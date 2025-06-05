
#  Kuraz Tasks API  
 task manager built with Django REST Framework*  

Need a simple way to track tasks? This lightweight API lets you create, complete, and delete tasks with straightforward HTTP requests. Perfect for small projects or learning REST APIs!

---

##  API Endpoints Quick Reference

### **Get all tasks**  
`GET /api/tasks/`  
*Example response:*  
```json
[
    {
        "id": 1,
        "title": "Walk the dog",
        "completed": false,
        "created_at": "2023-08-25T09:30:00Z"
    }
]
```

### **Add a new task**  
`POST /api/tasks/`  
*Send this:*  
```json
{
    "title": "Buy milk",
    "description": "Almond milk, 1L"
}
```response
```json
{
    "id": 2,
    "title": "Buy milk",
    "completed": false,
    "created_at": "2023-08-25T10:15:00Z"
}
```

### **Complete a task**  
`PUT /api/tasks/2/`  


### **Delete a task**  
`DELETE /api/tasks/2/`  


---



### Setup in 3 steps:  
1. **Clone & install**  
   ```bash
   git clone https://github.com/yourusername/kuraz.git
   cd kuraz
   pip install -r requirements.txt
   ```

2. **Run migrations**  
   ```bash
   python manage.py migrate
   ```

3. **Start the server**  
   ```bash
   python manage.py runserver
   ```

now use postman or curl to test apis
---
