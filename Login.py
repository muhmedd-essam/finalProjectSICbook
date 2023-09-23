# import json
# index=0
# logeIn_data = {"index": index}

login_data = [{"email": "12", "name": "Essam", "password": "12", "age": "20", "profile": "C:/Users/E S S A M/Desktop/315859822_1668378490224336_7890039000407411832_n.jpg", "Connect": "Done"}]

posts_data = [
    {"emailShare": "12", "name": "Essam", "Post": "hello world", "Like": 0, "Comment": 0, "x": 0, "y": 180, "profile": "C:/Users/E S S A M/Desktop/315859822_1668378490224336_7890039000407411832_n.jpg"},
    {"emailShare": "123", "name": "mohamed essam", "Post": "hello", "Like": 1, "Comment": 0, "x": 0, "y": 400, "profile": "C:/Users/E S S A M/Desktop/293452238_1565663177162535_8910620491206795250_n.jpg"},
    {"emailShare": "123", "name": "mohamed essam", "Post": "hello2", "Like": 1, "Comment": 0, "x": 0, "y": 620, "profile": "C:/Users/E S S A M/Desktop/293452238_1565663177162535_8910620491206795250_n.jpg"}
]

like_history_data = [{"from": "12", "like": 2, "to": "123"}, {"from": "123", "like": 1, "to": "12"}]

# Sort user_posts based on the number of likes for each "to" in like_history_data
posts_data = sorted(posts_data, key=lambda post: sum(history["like"] for history in like_history_data if history["to"] == post["emailShare"]), reverse=True)
for i, post in enumerate(posts_data):
    post["y"] = int(180 + (i * (620 - 180) / (len(posts_data) - 1)))
new_post = {"emailShare": "123", "name": "mohamed essam", "Post": "hello3", "Like": 3, "Comment": 0, "x": 0, "y": posts_data[-1]["y"] + 220, "profile": "C:/Users/E S S A M/Desktop/293452238_1565663177162535_8910620491206795250_n.jpg"}
# Print the sorted user_posts
print(posts_data)