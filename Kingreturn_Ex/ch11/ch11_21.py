# 在函數內修訂串列的內容
def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop()
        # 模擬出餐過程
        print("菜單：", current_meal)
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)


def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)


def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("==== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***", "\n")
    for served_meal in served:
        print(served_meal)


order_list = ['大麥克', '勁辣雞腿堡', '麥克雞塊']  # 所點餐點
served_list = []  # 已服務餐點

# 列出餐廳處理前的點餐內容
show_unserved_meal(order_list)  # 列出未服務的餐點
show_served_meal(served_list)  # 列出已服務餐點
kitchen(order_list, served_list)  # 餐廳處理流程
print("\n", "=== 廚房處理結束 ===")

# 列出餐廳處理後的點餐內容
show_unserved_meal(order_list)  # 列出未服務的餐點
show_served_meal(served_list)  # 列出已服務餐點
