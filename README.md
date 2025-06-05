
#  Kuraz Tasks API  
 task manager built with Django REST Framework*  

It's just a demo for task management which implement only the following API End points and have a simple home Page

---

##  API Endpoints Quick Reference

### **Get all tasks**  
`GET /api/tasks/`  
*Example response:*  
```json
[
    {
        "id": 1,
        "title": "Task 1",
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
    "title": "task 2",
    "description": "bla bla"
}
```response
```json
{
    "id": 2,
    "title": "task 2",
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
   git clone https://github.com/yared-Habtamu/kuraz.git
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
