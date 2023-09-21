import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

# 사용자 정보 데이터 로드
user_df = pd.read_csv('/workspaces/codespaces-jupyter/data/users.csv')  # 사용자 정보 파일 경로
ratings_df = pd.read_csv('/workspaces/codespaces-jupyter/data/ratings.csv')  # 아이템 평가 데이터 파일 경로

# 추천 대상 사용자 선택 (예시로 User1을 입력하여 테스트)
target_user = input()

# 사용자 간의 유클리디안 거리 계산 (사용자 정보 특성으로 계산)
user_features = user_df[['Age', 'Height', 'Weight', 'UpperBodyStrength', 'LowerBodyStrength']]
distances = euclidean_distances(user_features)

# 유사도를 기반으로 가장 유사한 사용자 선택
similar_user_index = distances[user_df[user_df['User'] == target_user].index[0]].argsort()[1]


# 추천할 아이템 찾기 (가장 유사한 사용자의 아이템 중에서 사용자가 아직 평가하지 않은 아이템)
target_user_ratings = ratings_df[ratings_df['User'] == target_user]
similar_user_ratings = ratings_df[ratings_df['User'] == user_df.iloc[similar_user_index]['User']]

unrated_items = similar_user_ratings[~similar_user_ratings['Item'].isin(target_user_ratings['Item'])]

# 추천 아이템 정렬
recommendations = unrated_items.sort_values(by='Rating', ascending=False)

# 결과 출력
print(f"사용자 {target_user}에게 추천하는 아이템은:")
for _, row in recommendations.iterrows():
    print(f"- {row['Item']} (예상 평점: {row['Rating']:.2f})")
