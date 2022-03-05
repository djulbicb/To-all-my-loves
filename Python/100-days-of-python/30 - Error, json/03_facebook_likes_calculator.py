posts = [
    {"likes": 10, "comments": 2, "shares": 1},
    {"comments": 3, "shares": 3},
    {"likes": 1, "comments": 1, "shares": 2},
    {"likes": 4, "comments": 2, "shares": 1},
    {"comments": 5, "shares": 1}
]

total_likes = 0
for post in posts:
    try:
        total_likes += post["likes"]
    except KeyError as error:
        pass
print(total_likes)