import matplotlib.pyplot as plt

bst_result = {
    "insert_time": 0.002006053924560547,
    "search_time": 0.0,
    "delete_time": 0.0
}

avl_result = {
    "insert_time": 0.0030107498168945312,
    "search_time": 0.0,
    "delete_time": 0.0
}

operations = ["Insert", "Search", "Delete"]
bst_times = [bst_result["insert_time"], bst_result["search_time"], bst_result["delete_time"]]
avl_times = [avl_result["insert_time"], avl_result["search_time"], avl_result["delete_time"]]

fig, ax = plt.subplots()

bar_width = 0.35
index = range(len(operations))

bar1 = ax.bar(index, bst_times, bar_width, label='BST', color='b')
bar2 = ax.bar([i + bar_width for i in index], avl_times, bar_width, label='AVL', color='g')

ax.set_xlabel('Operations')
ax.set_ylabel('Time (seconds)')
ax.set_title('Performance Comparison: BST vs AVL Tree')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(operations)
ax.legend()


plt.tight_layout()
plt.show()
