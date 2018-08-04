
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# metrix = np.random.rand(10, 10)
# metrix_1 = np.random.uniform(0, 100)
# arr = np.random.normal(1.75, 0.1, (2, 3))

# stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# print("====================")
# result = np.std(stus_score, axis=0)
# print(result)
#
# print("====================")
# result = np.std(stus_score, axis=1)
# print(result)

# stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# print(stus_score)
# # stus_score[:, 0] = stus_score[:, 0] * 0.5
# # print(stus_score)
# q = np.array([[0.4], [0.6]])
# result = np.dot(stus_score, q)
# print("Finally results:")
# print(result)

# data_3_4 = pd.DataFrame(np.arange(10, 22).reshape(3, 4))
# print(data_3_4)
# print(data_3_4[:1])
# print(data_3_4[:][0])

filename = "dataset/IMDB-Movie-Data.csv"
IMDB_1000 = pd.read_csv(filename)
# print(IMDB_1000.head(5))
print(IMDB_1000.dtypes)
print("=======================")
# IMDB_1000.sort_values(by="Rating", ascending="False")
# print(IMDB_1000.head(5))
# print(IMDB_1000[IMDB_1000["Runtime (Minutes)"]==IMDB_1000["Runtime (Minutes)"].max()])
# print(IMDB_1000[IMDB_1000["Runtime (Minutes)"]==IMDB_1000["Runtime (Minutes)"].min()])
# print(IMDB_1000["Runtime (Minutes)"].max())
# print(IMDB_1000["Runtime (Minutes)"].min())

rating_data = IMDB_1000.sort_values(by="Rating", ascending="False")["Rating"]
# print(rating_data)
revenue_data = IMDB_1000.sort_values(by="Rating", ascending="False")["Revenue (Millions)"]
# print(revenue_data)
rating_list = rating_data.values.tolist()
# print(rating_list)
revenue_list = revenue_data.values.tolist()

plt.figure(dpi=128, figsize=(10, 6))
plt.scatter(rating_list, revenue_list, s=20)

plt.xlabel("Movie Rating", fontsize=16)
plt.ylabel("Revenue", fontsize=16)

plt.xlim((0, 10))

plt.title("Relationship between rating and revenue", fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()