def positive_feedback_percentage(ratings):
    if not ratings:
        return 0

    positive = sum(1 for r in ratings if r >=4)


    percentage = (positive / len(ratings)) * 100
    return round(percentage, 2)

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(f"Positive Feedback: {positive_feedback_percentage(ratings)}%")
