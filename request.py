import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NzMxNzM0OSwianRpIjoiOTA3ODQ5NjctNDg1ZC00OGNkLWFiZWItNjUzNjFlNWZkMjAxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InN1c21pdGFAbWFuZG9sLmNvbSIsIm5iZiI6MTc0NzMxNzM0OSwiY3NyZiI6IjIwMjQzZDg3LTNiYjktNDhkMi1hMDkyLWRlYTYzYzczNDEwNyIsImV4cCI6MTc0NzMxNzk0OX0.557ZvWvkrHG5I7Co1DcTsP5UwZneMdoKYGTpTiQienc"
}

response = requests.get('http://localhost:5000/users/get_users', headers=headers)
data = response.json()
print(data)
