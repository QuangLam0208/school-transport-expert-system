# HỆ CHUYÊN GIA QUYẾT ĐỊNH PHƯƠNG TIỆN ĐI HỌC

# Các quy tắc để ra quyết định dựa trên các yếu tố:
# - Khoảng cách đến trường (gần / trung bình / xa)
# - Thời gian (gấp / thoải mái)
# - Thời tiết (nắng / mưa / mát)


def knowledge_base(distance, time, weather):
    # khoảng cách xa
    if distance == "xa":
        return "Bạn nên đi xe bus."
    
    # thời gian gấp
    elif time == "gấp":
        if distance == "gần":
            return "Bạn nên đi xe máy."
        elif weather == "mưa": # trung bình, mưa
            return "Bạn nên đi xe bus."
        else: # trung bình, nắng
            return "Bạn nên đi xe máy."
    
    # thời gian thoải mái
    else:
        if weather == "mưa":
            return "Bạn nên đi xe bus."
        elif distance == "gần": # nắng / mát
            return "Bạn nên đi bộ hoặc đi xe đạp."
        else: # khoảng cách trung bình
            if weather == "mát":
                return "Bạn nên đi xe máy."
            else:
                return "Bạn nên đi xe bus."

def inference_engine():
    print("=== HỆ CHUYÊN GIA QUYẾT ĐỊNH PHƯƠNG TIỆN ĐI HỌC ===")

    # Dữ liệu người dùng nhập
    distance = input("Khoảng cách (gần (< 3km) / trung bình (3 - 7km) / xa (> 7km)): ").lower()
    time = input("Thời gian (gấp / thoải mái): ").lower()
    weather = input("Thời tiết (nắng / mưa / mát): ").lower()
    
    decision = knowledge_base(distance, time, weather)
    print(f"\nQuyết định đề xuất: {decision}")

if __name__ == "__main__":
    inference_engine()
