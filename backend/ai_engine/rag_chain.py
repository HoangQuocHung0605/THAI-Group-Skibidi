def ask_ai(question: str):
    # Trả về 2 giá trị: 1 chuỗi (answer) và 1 danh sách (sources)
    answer = f"AI trả lời cho câu hỏi: {question}"
    sources = ["https://gitlab.com/vi-du-nguon-1", "tailieu_nien_luan.pdf"] 
    return answer, sources