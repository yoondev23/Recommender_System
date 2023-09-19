
# 사용자-아이템 평점 데이터 (예제)
ratings = {
    'user1': {'item1': 5, 'item2': 3, 'item3': 4, 'item4': 4},
    'user2': {'item1': 3, 'item2': 1, 'item3': 3, 'item4': 3, 'item5': 5},
    'user3': {'item2': 2, 'item3': 3, 'item4': 4, 'item5': 2}
}

# 사용자 간의 유사도 계산
from math import sqrt


def euclidean_distance(user1, user2):
    common_items = set(user1.keys()) & set(user2.keys())
    if len(common_items) == 0:
        return 0  # 공통 평가한 아이템이 없으면 유사도 0
    squared_diff = sum([(user1[item] - user2[item])**2 for movie in common_items])
    return 1 / (1 + sqrt(squared_diff))


# 사용자 간의 유사도 행렬 계산
# ratings = 평가
def build_similarity_matrix(ratings):
    similarity_matrix = {}
    for user1 in ratings:
        similarity_matrix[user1] = {}
        for user2 in ratings:
            if user1 != user2:
                similarity_matrix[user1][user2] = euclidean_distance(ratings[user1], ratings[user2])
    return similarity_matrix


# 사용자에게 아이템 추천
def recommend_movies(user, ratings, similarity_matrix, num_recommendations=5):
    # 현재 사용자가 평가하지 않은 아이템 찾기
    unrated_items = set(ratings[user]) - set(user)
    
    # 다른 사용자들 중 유사도가 높은 순으로 정렬
    similar_users = sorted(similarity_matrix[user].items(), key=lambda x: x[1], reverse=True)
    
    recommendations = {}
    for similar_user, similarity in similar_users:
        for item in unrated_items:
            if item in ratings[similar_user]:
                if item not in recommendations:
                    recommendations[item] = 0
                recommendations[item] += ratings[similar_user][item] * similarity
    
    # 추천 아이템을 평점 순으로 정렬하여 반환
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations[:num_recommendations]


# 테스트
user_to_recommend = 'user1'
similarity_matrix = build_similarity_matrix(ratings)
recommendations = recommend_movies(user_to_recommend, ratings, similarity_matrix)

print(f"예상 평점이 높은 아이템 추천 (사용자: {user_to_recommend}):")
for movie, rating in recommendations:
    print(f"아이템: {movie}, 예상 평점: {rating}")




