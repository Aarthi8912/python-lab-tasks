
# Patient Data

import numpy as np

np.random.seed(2)
health_data = np.random.randint(60, 180, (100, 3))
print(health_data)

avg_values = np.mean(health_data, axis=0)
print(avg_values)

avg_values = np.mean(health_data, axis=1)
print(avg_values)


min_col = np.min(health_data, axis=0)
print(min_col)

min_row = np.min(health_data, axis=1)
print(min_row)

max_col = np.max(health_data, axis=0)
print(max_col)

max_row = np.max(health_data, axis=1)
print(max_row)

col_min = np.min(health_data, axis=0)
col_max = np.max(health_data, axis=0)
normalized_col = (health_data - col_min) / (col_max - col_min)
print(normalized_col)

row_min = np.min(health_data, axis=1).reshape(-1,1)
row_max = np.max(health_data, axis=1).reshape(-1,1)
normalized_row = (health_data - row_min) / (row_max - row_min)
print(normalized_row)

print(np.std(health_data))

print(np.median(health_data))


print(np.percentile(health_data, 90))


total_score = np.sum(health_data, axis=1)
print(total_score)

total_score = np.sum(health_data, axis=0)
print(total_score)

high_sugar_patients = health_data[health_data[:, 1] > 150]

print(high_sugar_patients)







